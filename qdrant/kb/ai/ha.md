# Home Assistant — HAOS sur Mac mini Intel 2017

> **Source** : sessions Claude juin 2026
> **Hôte** : Mac mini Intel 2017 dédié (192.168.0.25), HAOS, HA Core 2026.6.1
> **Accès** : http://192.168.0.25:8123 en direct, https://ha.test.teamfnb.com via Traefik (rule 50-unifi.yml, sans serversTransport — backend HTTP)
> **Dernière mise à jour** : 2026-06-10

---

## Vue d'ensemble des entités (état juin 2026)

Environ 770 sensors (dont ~70 unavailable), 344 switches, 283 binary sensors, 80 lights, 30 covers, 18 caméras (9 en enregistrement), 7 climates, 11 automations (9 actives), 2 locks, 4 personnes. Timezone Europe/Paris.

**Point d'attention** : ~70 sensors et ~30 binary sensors en état unavailable — candidats à un nettoyage d'entités orphelines.

---

## ha-mcp : add-on installé sur HAOS (pas sur le Swarm)

Le serveur MCP Home Assistant (ha-mcp, 89 outils) est déployé comme **add-on HAOS** directement sur le Mac mini Intel. Décision prise après comparaison avec l'option container Swarm :

- Add-on : connexion HA automatique sans token, mises à jour avec l'écosystème HA, zéro service sur le Swarm — mais charge sur le Mac mini Intel vieillissant et hors monitoring Grafana/Dozzle.
- Container Swarm : HA native, monitoring unifié, mais token Long-Lived à gérer.

ha-mcp propose aussi un **Webhook Proxy add-on** qui route le trafic MCP via le reverse proxy existant (Traefik/Cloudflare) — URL MCP unique sans port forwarding supplémentaire.

---

## Connexion clients : URL et rechargement de config

- La variable d'environnement côté client est `HOMEASSISTANT_URL` (valeur en place : `https://ha.test.teamfnb.com`).
- **Leçon Claude Desktop/M4** : après modification de `claude_desktop_config.json`, fermer COMPLÈTEMENT l'application (⌘Q ou `pkill -f "Claude"`) — fermer la fenêtre ne suffit pas. Et tester dans un NOUVEAU chat : un chat existant garde l'ancienne config MCP.
- Même principe que la leçon Hermes Desktop (Reload MCP manuel) : les clients MCP ne rechargent jamais leurs serveurs à chaud.

---

## Intégration Hermes

Hermes (M1) est connecté à HA via ha-mcp avec l'URL directe `http://192.168.0.25:8123`. C'est l'un des 5 MCP servers de la stack Hermes (avec Portainer, Proxmox, UniFi Network, UniFi Protect).

---

## Lien Homebridge (pont HomeKit, séparé de HA)

Homebridge tourne sur le Swarm (réseau host, port UI 8581, update stop-first pour libérer le port physique) — c'est un pont HomeKit distinct de HA, qui expose UniFi Protect, Samsung The Frame, Govee et Levoit. HA et Homebridge coexistent : HA est le hub domotique principal, Homebridge sert l'écosystème Apple Home.
