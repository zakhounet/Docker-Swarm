# UniFi UNAS Pro — NAS

> Généré automatiquement depuis l'API UniFi OS — 192.168.0.17
> Dernière mise à jour : juin 2026

---

## 📦 Matériel

| Propriété | Valeur |
|---|---|
| Modèle | UNAS Pro (UNASPRO) |
| Hostname | UNAS-Pro |
| IP | 192.168.0.17 (Main — 192.168.0.0/24) |
| Accès | https://unas.test.teamfnb.com |
| MAC | 0C:EA:14:EA:08:D4 |
| Firmware OS | 5.1.16 |
| UniFi Drive | 4.3.6 (release-candidate) |
| RAM | 8 Go (libre : ~6.1 Go) |
| CPU temp | 81°C |
| Uptime | ~4.9 jours |
| SSH | Activé |

---

## 💾 Stockage — RAID 5

| Propriété | Valeur |
|---|---|
| Configuration | RAID 5 + 1 disque hot spare |
| Capacité totale | ~27.2 To (29 962 Go) |
| Utilisé | ~17.0 To (18 645 Go) |
| Disponible | ~10.3 To (11 315 Go) |
| Utilisation | ~62% |
| Point de montage | `/volume/200f81cd-9825-4c5a-94f8-39107848b9b5` |
| Santé RAID | ✅ healthy |

### Disques (7 slots)

| Slot | Modèle | Taille | Rôle | Santé | Temp | Heures |
|---|---|---|---|---|---|---|
| 1 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 48°C | 15 920h |
| 2 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 49°C | 17 149h |
| 3 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 48°C | 15 917h |
| 4 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 48°C | 15 965h |
| 5 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 48°C | 16 230h |
| 6 | Toshiba HDWG460 | 6 To | RAID member | ✅ Good | 48°C | 11 320h |
| 7 | Toshiba HDWG460 | 6 To | **Hot spare** | ✅ Good | 46°C | 11 290h |

---

## 🌐 Réseau

| Interface | Type | IP | Vitesse |
|---|---|---|---|
| enp0s1 | ETH (WAN1) | — | GbE (non connecté) |
| enp0s2 | SFP+ (WAN2) | 192.168.0.17 | **10G SFP+** ✅ |

DNS configurés : 192.168.0.36, 192.168.0.104, 1.1.1.1, 192.168.50.61, 192.168.50.62

---

## 📱 Applications installées

| App | Version | État |
|---|---|---|
| UniFi Drive | 4.3.6 | ✅ Running |
| Users (Identity) | 1.13.5 | ✅ Running |

---

## ⚙️ Configuration

- **Auto-backup** : activé
- **Mise à jour auto** : quotidienne à 4h (firmware uniquement)
- **Canal firmware** : release-candidate
- **Timezone** : Europe/Paris

---

## 📂 Partages & Services

### Services actifs
| Service | État |
|---|---|
| SMB (Samba) | ✅ Actif |
| NFS | ✅ Actif |
| rclone daemon | ✅ Actif (`/data/unifi-drive/rclone/rclone.conf`) |

### Partages SMB

| Nom | Chemin | Accès | Time Machine |
|---|---|---|---|
| Personal-Drive | `%H/.data` (home de chaque user) | Utilisateurs UniFi Drive | ✅ |
| Shared_Drive_Example | `/volume/.../Shared_Drive_Example/.data` | kyftherock, kyfran | ✅ |
| unifi-drive-backup-only | `/srv/.unifi-drive/homes/` | unifi-drive-backup (backup distant) | — |

### Exports NFS

| Chemin exporté | Client | Options |
|---|---|---|
| `Shared_Drive_Example/.data` | 192.168.0.125 | rw, root_squash, all_squash |
| `Shared_Drive_Example/.data` | 192.168.0.25 (Home Assistant) | rw, root_squash, all_squash |

### Utilisateurs UniFi Drive
| Username | Rôle |
|---|---|
| kyftherock | Admin |
| kyfran | Utilisateur |
| uisys-muiq4bdm0l1hh70q12djv0hn8c | Compte système SSO (Franck Boutboul) |

---

## 💽 Système de fichiers

| Point de montage | Dispositif | Taille | Utilisé | Dispo |
|---|---|---|---|---|
| `/volume/200f81cd-...` | `/dev/md3` (RAID 5) | 28 To | 17 To | 11 To (63%) |
| `/` (overlay) | overlayfs | 24 Go | 6.3 Go | 17 Go |
| `/boot/firmware` | eMMC | 2 Go | 1.3 Go | 592 Mo |
| `/var/log` | partition log | 974 Mo | 170 Mo | 737 Mo |

Structure du volume principal :
```
/volume/200f81cd-.../
└── .srv/
    └── .unifi-drive/
        ├── Shared_Drive_Example/
        │   └── .data/         ← partage SMB + NFS
        ├── homes/
        │   ├── kyftherock/
        │   ├── kyfran/
        │   └── uisys-.../
        └── .archives/         ← archives chiffrées
```

---

## 🔒 Sécurité & Accès

- SSH activé — user `root`, password auth
- Accès local : https://192.168.0.17
- Accès interne : https://unas.test.teamfnb.com
- Réseau Main (192.168.0.0/24) via 10G SFP+
- SMB : authentification obligatoire (`map to guest = never`)
- NFS : restricted to 192.168.0.125 et 192.168.0.25

---

## ⚠️ Points d'attention

- **CPU à 81°C** — températures à surveiller
- **Disque slot 2** : 17 149h (le plus usé de l'ensemble)
- **enp0s1 (ETH)** non connecté — seul le SFP+ 10G est actif
- **Volume à 63%** — encore de la marge mais à surveiller avec rclone
