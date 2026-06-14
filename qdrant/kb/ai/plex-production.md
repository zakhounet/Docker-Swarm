# Serveur Plex Principal — Ubuntu Desktop (192.168.0.125)

> Généré automatiquement via SSH (kyfran@192.168.0.125)
> Dernière mise à jour : juin 2026

---

## 📦 Matériel & Système

| Propriété | Valeur |
|---|---|
| Hostname | ubuntu |
| IP | 192.168.0.125 (Main — 192.168.0.0/24) |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | 6.8.0-124-generic |
| CPU | Intel Core (CoffeeLake-S) — 1 socket |
| GPU | Intel UHD Graphics 630 (transcodage hardware) |
| RAM | 16 Go (2.6 Go utilisé, 12 Go disponible) |
| Stockage OS | NVMe 465 Go (nvme0n1) |
| Interface réseau | enx5c857e3f1902 — 192.168.0.125/24 |
| VPN | ExpressVPN (daemon actif) |

---

## 💾 Stockage Médias — RAID 5 local

| Propriété | Valeur |
|---|---|
| Array | `/dev/md0` |
| Type | RAID 5 (4 disques) |
| Disques | sda + sdb + sdc + sdd — 4× 7.3 To |
| Capacité totale | ~21.8 To |
| État | ✅ [UUUU] — 4/4 disques actifs |
| Point de montage | `/home/kyfran/Multimedia` |
| Filesystem | ext4 (noatime, discard) |

### Montage TrueNAS supplémentaire
| Chemin | Source | Type |
|---|---|---|
| `/mnt/truenas` | `//192.168.50.55/multimedia` | CIFS (SMB 3.1.1) |

---

## 🎬 Plex Media Server (Production)

| Propriété | Valeur |
|---|---|
| Version | 1.43.2.10687-563d026ea |
| Service | `plexmediaserver.service` — ✅ actif, enabled |
| Actif depuis | 5 juin 2026 (~9 jours) |
| RAM utilisée | 3.8 Go (peak 11.2 Go) |
| CPU cumulé | 3h 05min |
| Config | `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/` |
| Librairies | `/home/kyfran/Multimedia` (RAID local) + `/mnt/truenas` (TrueNAS SMB) |
| GPU transcodage | Intel UHD 630 |
| Rôle | **Production** (le LXC 400 sur Proxmox/Zakh est le backup) |

---

## ⚙️ Services notables

| Service | État |
|---|---|
| plexmediaserver | ✅ RUNNING |
| ExpressVPN | ✅ RUNNING |
| GNOME / GDM | ✅ RUNNING (Ubuntu Desktop) |
| GNOME Remote Desktop | ✅ RUNNING |
| Avahi (mDNS) | ✅ RUNNING |
| mdmonitor (RAID) | ✅ RUNNING |
| NFS server (fsidd) | ✅ RUNNING |
| CUPS | ✅ RUNNING |

---

## 🌐 Réseau

- IP fixe : **192.168.0.125/24** — réseau Main
- NFS export actif (fsidd) — NVR Protect exporte vers cette machine (cf. `unifi-protect.md`)
- Montage SMB vers TrueNAS : `//192.168.50.55/multimedia` → `/mnt/truenas`

---

## ⚠️ Points d'attention

- **ExpressVPN actif en permanence** — vérifier que Plex reste accessible depuis le LAN (split tunnel ?)
- **RAID md0 bitmap activé** — normal pour les reprises après crash
- **Ubuntu Desktop** (pas Server) — GDM/GNOME actif, consomme de la RAM inutilement pour un serveur
- **Pas de Tautulli** sur cette machine — statistiques Plex absentes localement
