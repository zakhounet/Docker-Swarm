# UniFi Protect — NVR & Caméras

> Généré automatiquement depuis l'API UniFi Protect
> Dernière mise à jour : juin 2026

---

## 📦 NVR — UNVR4

| Propriété | Valeur |
|---|---|
| Modèle | UNVR4 |
| IP | 192.168.30.100 (VLAN 30 — Camera) |
| Firmware | 5.1.15 |
| Version Protect | 7.1.83 |
| État disques | ✅ OK |
| Stockage RAID | RAID (3× HDD actifs) |
| Capacité totale | ~22.2 To |
| Utilisé | ~20.9 To (94.3%) |
| Disponible | ~1.3 To |
| Débit enregistrement | ~5.3 Mbps |
| Mode allocation | Balanced (50% HQ) |
| Recyclage actif | Oui |

### Disques (4 slots)
| Slot | Modèle | Taille | État |
|---|---|---|---|
| 1 | Toshiba MG08ADA800E | 8 To | ✅ Good |
| 2 | WDC WD85PURZ-85C4WY0 | 8 To | ✅ Good |
| 3 | — | — | ❌ DOWN (disque défaillant) |
| 4 | Toshiba HDWG480 | 8 To | ✅ Good |

---

## 📷 Caméras (12)

| Nom | Modèle | IP | MAC | État | Résolution max | FPS | Enregistrement | Smart Detect |
|---|---|---|---|---|---|---|---|---|
| Entrée Principale | UVC G6 PTZ | 192.168.30.142 | 84:78:48:B2:CA:00 | ✅ | 3840×2160 | 30 | always | person, vehicle, animal, face, plate |
| Entrée Maison | UVC G4 Pro | 192.168.30.141 | D0:21:F9:93:41:B1 | ✅ | 3840×2160 | 24 | detections | person, vehicle, animal |
| Entrée Jardin | UVC G5 Flex | 192.168.30.148 | F4:E2:C6:0F:FA:B4 | ✅ | 2688×1512 | 30 | always | person, vehicle |
| Entrée Haut | UVC G5 Flex | 192.168.30.147 | F4:E2:C6:0B:C2:D0 | ✅ | 2688×1512 | 30 | detections | person, vehicle, animal |
| Jardin derrière | UVC G6 Bullet | 192.168.30.140 | 84:78:48:54:27:16 | ✅ | 3840×2160 | 30 | always | person, vehicle, animal, face, plate |
| Jardin côté | UVC G6 Bullet | 192.168.30.144 | 84:78:48:54:27:28 | ✅ | 3840×2160 | 30 | always | person, vehicle, animal, face, plate |
| Piscine | UVC G6 PTZ | 192.168.30.146 | 84:78:48:B2:D1:D5 | ✅ | 3840×2160 | 30 | always | person, vehicle, animal, face, plate |
| Abri de Jardin | UVC G6 Instant | 192.168.30.149 | 84:78:48:28:58:84 | ✅ | 3840×2160 | 30 | always | person, vehicle, animal, face, plate |
| Chambre enfants | UVC G4 Instant | 192.168.30.145 | D0:21:F9:95:3B:B5 | ❌ DISCONNECTED | 2688×1512 | 30 | always | person, vehicle, animal |
| Bureau | UVC G3 Flex | 192.168.30.143 | D0:21:F9:95:09:17 | ✅ | 1920×1080 | 25 | always | — |
| C210 | C210 | 192.168.30.150 | 7C:F1:7E:B9:66:45 | ✅ | — | — | always | — |
| C110 | C110 | 192.168.30.151 | DC:62:79:41:3E:B8 | ✅ | — | — | always | — |

### Channels disponibles par caméra (RTSP)
- **G6 PTZ / G6 Bullet / G6 Instant / G4 Pro** : High 3840×2160, Medium 1280×720, Low 640×360
- **G5 Flex** : High 2688×1512, Medium 1280×720, Low 640×360
- **G4 Instant** : High 2688×1512, Medium 1280×720, Low 640×360
- **G3 Flex** : High 1920×1080, Medium 1024×576, Low 640×360

---

## 🔴 Points d'attention

- **Chambre enfants (G4 Instant)** — DISCONNECTED (192.168.30.145)
- **Stockage à 94.3%** — recyclage actif, surveiller la rétention
- **C210 / C110** — firmware non renseigné, pas de smart detect configuré

---

## 🌐 Réseau

- VLAN : **30 — Camera** (192.168.30.0/24)
- Zone ZBF : **Untrusted** — accès sortant bloqué par défaut
- Exception firewall : NVR 192.168.30.100 → ports 443 + ICMP depuis WireGuard VPN
- Accès Protect : `https://192.168.30.100`
