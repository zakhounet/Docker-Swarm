# Technitium DNS — Cluster hybride Pi4 + Swarm

> **Source** : sessions Claude 2025-2026
> **Topologie** : Pi4 (192.168.50.104) = primaire ; instances Swarm sur Tom et Zakh = slaves (mode global, contrainte node.labels.dns_node == true) ; Ilan exclu de Technitium
> **Dernière mise à jour** : 2026-06-10

---

## API : port 443 (pas 5380) et accès indirect depuis le M1

L'API Technitium du Pi4 est accessible sur `https://192.168.50.104` (port 443), PAS sur le port 5380 par défaut. Le M1 (192.168.0.37) n'a pas de route directe vers le réseau 192.168.50.x — les appels API doivent passer par SSH via docker-manager-01 (192.168.50.61).

**Authentification** : obtenir un token frais avant chaque session d'appels :

```
/api/user/login?user=admin&pass=<password>
```

---

## ⚠️ Action ouverte : mot de passe admin

Le mot de passe admin est encore `password` (valeur par défaut du compose). À changer en priorité — c'est dans la liste des actions de sécurité ouvertes, avec la révocation du token Portainer exposé.

---

## Versionnage des images : semver 3 chiffres

Les tags Docker Technitium utilisent un semver à 3 chiffres : `15.2.0` est valide, `15.2` n'existe pas. Toujours vérifier le tag exact sur les releases GitHub avant un `docker service update --image`.

---

## webServiceReverseProxyAddresses : API uniquement (v15.2)

Le paramètre `webServiceReverseProxyAddresses` n'apparaît PAS dans l'UI web (Settings → General) en 15.2 — il n'est configurable que via l'API. Les valeurs par défaut autorisent déjà tous les réseaux privés (192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8) : aucune action nécessaire pour que les instances passent derrière Traefik.

---

## Persistance : un dossier de config par nœud (exception SQLite)

Chaque instance Swarm monte un dossier dédié : `technitium/config-{{.Node.Hostname}}`. Raison : SQLite gère mal les verrous de fichiers sur stockage réseau (CephFS) — partager un même dossier entre instances corromprait la base. Même logique que Portainer (base déplacée hors CephFS sur /mnt/portainer-db/data).

---

## Exposition réseau

Ports publiés en mode host sur les nœuds labellisés : 53/udp, 53/tcp (résolution) et 53443/tcp (UI HTTPS). L'UI cluster est servie par Traefik via `technitium.test.teamfnb.com` (load balancing sticky) et les accès directs `dns-pi4`, `dns-tom`, `dns-zakh`.
