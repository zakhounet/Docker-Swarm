# Traefik — Reverse proxy du cluster (stack "proxy")

> **Source** : sessions Claude + fichiers de config en production
> **Version** : traefik:v3.6.5, mode Global sur les 3 managers
> **Dernière mise à jour** : 2026-06-10

---

## Règle invariante : le nom de stack DOIT rester "proxy"

La stack Traefik est déployée sous le nom `proxy`. Ce nom ne doit jamais changer : le réseau overlay externe `proxy` y est lié, et tous les services du Swarm référencent ce réseau (`traefik.swarm.network=proxy`). Renommer la stack casserait le routage de l'ensemble des services.

---

## Double provider : Swarm (labels) + File (rules/)

Traefik utilise deux méthodes de découverte complémentaires :

- **Provider Swarm** (labels dans les docker-compose) : pour les apps conteneurisées du Swarm (Vaultwarden, Portainer, Homarr, Dozzle, Grafana, whoami...). `exposedByDefault=false` — chaque service doit déclarer `traefik.enable=true`.
- **Provider File** (`/mnt/cephfs/docker-cluster/Docker-Swarm/traefik/rules/`, rechargé à chaud) : pour les services hors-Swarm ou hybrides (Proxmox, TrueNAS, Technitium, UniFi, Home Assistant, Plex, PBS).

Organisation des fichiers rules :
- `00-transports.yml` — serversTransports (insecureSkipVerify pour certs self-signed Technitium et PVE)
- `01-middlewares.yml` — default-headers (HSTS, CSP, X-Frame), dashboard-redirect
- `05-traefik-dash.yml` — dashboard Traefik
- `10-proxmox.yml` — Tom/Zakh/Ilan (:8006) + PBS (192.168.50.100:8007)
- `20-truenas.yml` — TrueNAS (192.168.50.55:443)
- `30-technitium.yml` — cluster DNS + accès directs par nœud
- `40-homebridge.yml` — Homebridge (VIP + 3 managers :8581) + Plex
- `50-unifi.yml` — UDM-SE, UNAS, NVR, Home Assistant

---

## Certificats : wildcard Cloudflare DNS challenge

Résolveur unique `cloudflare` en DNS challenge, wildcard `*.test.teamfnb.com` + apex. Stockage ACME : `/etc/traefik/acme.json` (monté depuis CephFS). Propagation : delaybeforechecks 60s, propagation check désactivé, resolvers 1.1.1.1/1.0.0.1.

---

## Middleware default-headers : la CSP est le point sensible

Le middleware `default-headers@file` centralise HSTS, X-Frame, XSS, et une Content-Security-Policy. La CSP autorise explicitement :
- `*.ui.com` / `*.ubnt.com` (icônes et stats UniFi)
- `*.grafana.com`, jsdelivr, gravatar... (assets Grafana/Homarr)
- `frame-src 'self' https://*.test.teamfnb.com` (iframes croisées entre services internes, ex. widgets Homarr)

**Leçon** : une interface qui s'affiche cassée derrière Traefik (icônes manquantes, iframes vides) est presque toujours un blocage CSP — ajuster `img-src` / `frame-src` dans 01-middlewares.yml plutôt que désactiver le middleware.

---

## Load balancing Technitium : sticky session obligatoire

Le service `technitium-cluster` répartit l'UI entre Pi4 (.104:443) et les instances Swarm Tom (.61:53443) / Zakh (.62:53443), avec cookie sticky `technitium_session`. Sans sticky, la session admin saute d'un nœud à l'autre et déconnecte l'utilisateur. Health check : path /, interval 15s, timeout 5s (large pour éviter les 504 au démarrage).

---

## Ports publiés en mode host

Les entrypoints 80/443 sont publiés en `mode: host` (pas ingress) sur chaque manager — nécessaire pour préserver les IPs sources réelles et pour Keepalived/VIP. Conséquence : Traefik doit tourner en mode Global (une instance par manager).
