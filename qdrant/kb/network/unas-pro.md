# UNAS Pro — Snapshot KB

> Généré automatiquement par cron `unas-kb-refresh` — **2026-06-15**
> Sources : API `/api/system` + SSH root@192.168.0.17

---

## Identité

| Paramètre | Valeur |
|---|---|
| Nom | UNAS Pro |
| Modèle | UniFi Network Attached Storage Pro (UNASPRO) |
| Hostname | UNAS-Pro |
| IP principale | 192.168.0.17 |
| MAC | 0C:EA:14:EA:08:D4 |
| Firmware | 5.1.16 (canal : release-candidate) |
| Dernier firmware stable | v4.1.11 (canal release) |
| Firmware RC dispo | v5.1.16+a5860d5 (2026-06-08) |
| OS | Debian Bullseye (ARM) |
| Serial | 0cea14ea08d4 |
| Localisation | Jonage, Rhône, France |
| SSH | Activé |
| Propriétaire | Franck Boutboul |

---

## Réseau

| Interface | Type | Mode | IP | Vitesse |
|---|---|---|---|---|
| enp0s1 | ETH (RJ45) | static | 192.168.0.17 | auto-nego (non connectée) |
| enp0s2 | SFP+ | dhcp | 192.168.0.17 (active) | **10 Gbps** |

- Gateway : 192.168.0.1
- DNS : 192.168.0.36 (primaire), 1.1.1.1, 192.168.0.104, 192.168.50.61, 192.168.50.62
- Interface active : **enp0s2** (SFP+ 10G, MAC 0C:EA:14:EA:08:D5)

---

## Stockage — RAID

| Paramètre | Valeur |
|---|---|
| Type RAID | **RAID 5** |
| Périphérique MD | md3 |
| Membres actifs | 6 (sda5 sdc5 sdd5 sde5 sdf5 sdg5) |
| Hot spare | 1 (sdb, slot 7) |
| Total disques | 7 × 6 To |
| Capacité brute | ~42 To |
| Capacité utilisable | **~27,3 Tio** (29 962 Go) |
| Utilisé | **~17 Tio** (18 645 Go) |
| Libre | **~10 Tio** (11 317 Go) |
| Utilisation | **63%** |
| État RAID | **healthy** |
| Erreurs | 0 |
| Point de montage | `/volume/200f81cd-9825-4c5a-94f8-39107848b9b5` |

---

## Disques

| Slot | Nœud | Modèle | Série | Taille | State | Santé | Secteurs défectueux | Power-on (h) | Temp (°C) | Rôle |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | sdg | TOSHIBA HDWG460 | 23H0A02JFA4H | 6 To | normal | **good** | 0 | 15 944 | 41 | data |
| 2 | sde | TOSHIBA HDWG460 | 92E0A00YFR1H | 6 To | normal | **good** | 0 | 17 173 | 42 | data |
| 3 | sdc | TOSHIBA HDWG460 | 23H0A039FA4H | 6 To | normal | **good** | 0 | 15 941 | 42 | data |
| 4 | sdf | TOSHIBA HDWG460 | 23G0A06DFA4H | 6 To | normal | **good** | 0 | 15 990 | 41 | data |
| 5 | sdd | TOSHIBA HDWG460 | 23H0A043FA4H | 6 To | normal | **good** | 0 | 16 255 | 42 | data |
| 6 | sda | TOSHIBA HDWG460 | Y4U0A00JFA4H | 6 To | normal | **good** | 0 | 11 345 | 42 | data |
| 7 | sdb | TOSHIBA HDWG460 | Y4U0A00XFA4H | 6 To | normal | **good** | 0 | 11 315 | 41 | **hot spare** |

- Firmware disques : 0601 (slots 1-5), 0602 (slots 6-7)
- Interface : SATA 3.3, 7200 RPM, type HDD
- Tous les disques : aucun secteur défectueux, santé good

---

## Espaces système

| Volume | Taille | Utilisé | Dispo | Type |
|---|---|---|---|---|
| md3 (RAID5 principal) | 28 T | 17 T | 11 T | primary |
| overlayfs-root (/) | 24 G | 6,4 G | 16 G | root |
| /boot/firmware | 2,0 G | 1,3 G | 592 M | root partition |
| /var/log | 974 M | 165 M | 743 M | logs |
| /persistent | 2,0 G | 182 M | 1,7 G | persistant |
| /tmp | 2,0 G | ~0 | 2,0 G | tmpfs |
| swap (md0) | RAID1 7× | 0 | 0 | swap |

---

## Partages SMB

| Partage | Chemin | Utilisateurs | Time Machine |
|---|---|---|---|
| Shared_Drive_Example | `/volume/200f81cd-9825-4c5a-94f8-39107848b9b5/.srv/.unifi-drive/Shared_Drive_Example/.data` | kyftherock, kyfran, unifi-drive-backup | **Oui** |

- Config : `/etc/samba/share.conf`
- Guest ok : non
- Force group : `unifi-drive`
- `fruit:time machine = yes` → compatible Time Machine macOS

---

## Partages NFS

Aucun export NFS configuré (`/etc/exports` vide).

---

## Services actifs

| Service | État | Détail |
|---|---|---|
| smbd | **running** | 5 processus (multi-worker) |
| nfsd | **running** | 8 threads kernel |
| rclone | **running** | UniFi Drive backup daemon (`/data/unifi-drive/rclone/rclone.conf`) via unix socket |

Commandes de contrôle SSH :
```bash
ssh root@192.168.0.17
systemctl status smbd nfsd
```

---

## Applications UniFi OS

| App | Type | État | Version |
|---|---|---|---|
| unifi-drive (Drive) | controller | **active** | 4.3.6 |
| identity | app | **active** | standard |

- Drive API prefix : `/proxy/drive/`
- Canal de mise à jour Drive : release-candidate
- Rollback disponible : Drive 4.2.6

---

## Accès et credentials

| Méthode | Paramètres |
|---|---|
| API login | `POST https://192.168.0.17/api/auth/login` → JSON `{"username":"kyftherock","password":"***"}` |
| SSH | `root@192.168.0.17` — password ou clé SSH |
| Interface Web | `https://192.168.0.17` |
| Clé SSH | `~/.ssh/id_rsa` (M4 Pro) |

> ⚠️ `/proxy/nas/api/v1/*` et `/proxy/unas/api/v1/*` retournent 404 HTML. Utiliser `/api/system` uniquement.

---

## Watchdog

Script : `~/.hermes/scripts/unas_disk_watch.py`
Fréquence : toutes les 5 minutes (no_agent)
Surveille : état disques, température >55°C, utilisation volume >80%, services SMB/NFS/rclone

Seuils d'alerte :
- Utilisation actuelle : **63%** (seuil alerte : 80%)
- Température max actuelle : **42°C** (seuil alerte : 55°C)
- Secteurs défectueux : **0** sur tous les disques
