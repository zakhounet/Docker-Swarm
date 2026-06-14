# JetKVM — Accès IPMI-like (×3 MS-01)

> Généré automatiquement depuis /metrics Prometheus
> Dernière mise à jour : juin 2026

---

## Vue d'ensemble

| Nœud | IP | Version | Cloud | Dernière connexion depuis |
|---|---|---|---|---|
| **Ilan** | 192.168.0.242 | 0.5.9-dev202606110823 | ❌ désactivé | — (jamais connecté) |
| **Zakh** | 192.168.0.243 | 0.5.8 | ❌ désactivé | 192.168.0.93 (Mac mini M4) |
| **Tom** | 192.168.0.244 | 0.5.8 | ❌ désactivé | 192.168.0.93 (Mac mini M4) |

Accès local uniquement (Cloud désactivé sur les 3). Interface web sur `http://192.168.0.24x`.

---

## Détail par JetKVM

### JetKVM Ilan (192.168.0.242)
- **Nœud Proxmox** : Ilan (192.168.0.52)
- **Firmware** : 0.5.9-dev (branche dev, go1.25.1, arm/linux)
- **Cloud** : ❌ désactivé (`jetkvm_cloud_connection_status=0`)
- **Sessions locales** : aucune session active enregistrée
- **WoL** : disponible (0 paquets envoyés)
- **Uptime process** : ~5.6h (démarré récemment)

### JetKVM Zakh (192.168.0.243)
- **Nœud Proxmox** : Zakh (192.168.0.54)
- **Firmware** : 0.5.8 (go1.25.1, arm/linux)
- **Cloud** : ❌ désactivé
- **Client actif** : 192.168.0.93 (Mac mini M4) — 11 sessions, ping latency ~1.6ms
- **WoL** : disponible (0 paquets envoyés)
- **RAM process** : ~43 Mo

### JetKVM Tom (192.168.0.244)
- **Nœud Proxmox** : Tom (192.168.0.45)
- **Firmware** : 0.5.8 (go1.25.1, arm/linux)
- **Cloud** : ❌ désactivé
- **Client actif** : 192.168.0.93 (Mac mini M4) — 2 sessions, ping latency ~1.3ms
- **WoL** : disponible (0 paquets envoyés)
- **RAM process** : ~44 Mo

---

## Capacités

| Fonctionnalité | Support |
|---|---|
| KVM (Clavier/Vidéo/Souris) | ✅ 1080p@60fps H.264, ~30-60ms latence |
| Wake-on-LAN | ✅ (via `jetkvm_wol`) |
| Accès local (LAN) | ✅ |
| Accès cloud (JetKVM Cloud) | ❌ désactivé |
| Tailscale | ✅ supporté (non configuré) |
| BIOS / boot management | ✅ accès pré-OS complet |

---

## Accès

- Interface web locale : `http://192.168.0.242` (Ilan), `http://192.168.0.243` (Zakh), `http://192.168.0.244` (Tom)
- Métriques Prometheus : `http://192.168.0.24x/metrics`
- Réseau : Main (192.168.0.0/24)

---

## ⚠️ Points d'attention

- **Ilan (0.5.9-dev)** : firmware de développement — moins stable que 0.5.8 stable
- **Cloud désactivé** sur les 3 : accès uniquement depuis le LAN ou VPN WireGuard
- **Sessions actives uniquement depuis 192.168.0.93** (Mac mini M4) — pas depuis le M4 Pro (192.168.0.37)
