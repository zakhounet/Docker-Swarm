# TrueNAS SCALE — Snapshot KB

> Généré automatiquement par cron `truenas-kb-refresh` — lundi 3h  
> Source : API REST v2 `https://192.168.50.55`  
> Dernière mise à jour : 2026-06-15

---

## Système

| Champ | Valeur |
|---|---|
| **Version** | TrueNAS SCALE 25.10.3 |
| **Hostname** | truenas |
| **IP principale** | 192.168.0.241 (1G) |
| **IP stockage/gestion** | 192.168.50.55 (LAGG SFP+ bond007) |
| **CPU** | AMD Ryzen 5 PRO 5650G with Radeon Graphics — 12 cœurs |
| **RAM** | 125 GiB |
| **Carte mère** | ASRock X570D4U-2L2T/BCM |
| **Uptime** | ~58 jours |
| **Licence** | Community (null) |

---

## Réseau

| Interface | Type | État | IP | Description |
|---|---|---|---|---|
| `enp38s0` | Physical | UP | 192.168.0.241 | 1G management |
| `enp36s0f0np0` | Physical | UP | — | SFP+ membre bond007 |
| `enp36s0f1np1` | Physical | UP | — | SFP+ membre bond007 |
| `bond007` | LAGG | UP | 192.168.50.55 | LAGG 2×10G SFP+ |
| `enp39s0` | Physical | DOWN | — | — |
| `enxbe5b2f037f9f` | Physical | DOWN | — | — |

---

## Pools ZFS

### `tank` — HDD principal

| Attribut | Valeur |
|---|---|
| **Status** | ONLINE ✅ |
| **Healthy** | true |
| **Taille brute** | 43.7 TiB |
| **Alloué** | 27.8 TiB |
| **Libre** | 15.9 TiB |
| **Autotrim** | off |
| **Dernier scrub** | FINISHED — 0 erreurs |

### `VmApps` — SSD applications/VMs

| Attribut | Valeur |
|---|---|
| **Status** | ONLINE ✅ |
| **Healthy** | true |
| **Taille brute** | 3.6 TiB |
| **Alloué** | 121 GiB |
| **Libre** | 3.5 TiB |
| **Autotrim** | off |
| **Dernier scrub** | FINISHED — 0 erreurs |

---

## Disques (15 total)

### HDD — Toshiba HDWG460 6 To (×8)

| Device | Modèle | Taille | RPM | Numéro de série |
|---|---|---|---|---|
| sdd | TOSHIBA_HDWG460 | 6 To | 7200 | 9380A00SFA4H |
| sde | TOSHIBA_HDWG460 | 6 To | 7200 | 9340A005FA4H |
| sdh | TOSHIBA_HDWG460 | 6 To | 7200 | 7370A0KNFA4H |
| sdi | TOSHIBA_HDWG460 | 6 To | 7200 | 73X0A006FA4H |
| sdk | TOSHIBA_HDWG460 | 6 To | 7200 | 73F0A04EFA4H |
| sdj | TOSHIBA_HDWG460 | 6 To | 7200 | 73G0A0G3FA4H |
| sdl | TOSHIBA_HDWG460 | 6 To | 7200 | 73E0A00QFA4H |
| sdm | TOSHIBA_HDWG460 | 6 To | 7200 | Z330A06RFR1H |

### SSD — Samsung 870 EVO 1 To (×3)

| Device | Modèle | Taille | Numéro de série |
|---|---|---|---|
| sda | Samsung_SSD_870_EVO_1TB | 1 To | S75CNX0WB10150H |
| sdb | Samsung_SSD_870_EVO_1TB | 1 To | S75CNX0WB05982T |
| sdc | Samsung_SSD_870_EVO_1TB | 1 To | S75CNX0WB00556N |

### SSD — Samsung 870 QVO 1 To (×1)

| Device | Modèle | Taille | Numéro de série |
|---|---|---|---|
| sdf | Samsung_SSD_870_QVO_1TB | 1 To | S5RRNF1W405033N |

### NVMe — Samsung 970 EVO Plus 2 To (×1)

| Device | Modèle | Taille | Numéro de série |
|---|---|---|---|
| nvme0n1 | Samsung SSD 970 EVO Plus 2TB | 2 To | S6P1NF0W910187X |

### SSD divers

| Device | Modèle | Taille | Numéro de série |
|---|---|---|---|
| sdg | CT240BX500SSD1 (Crucial) | 240 Go | 2337E876E749 |
| sdn | KINGSTON_SA400S37240G | 240 Go | 50026B77859C592E |

---

## Datasets

### Pool `tank`

| Dataset | Utilisé | Disponible | Mountpoint |
|---|---|---|---|
| `tank` | 19.7 TiB | 11.2 TiB | /mnt/tank |
| `tank/multimedia` | 15.3 TiB | 11.2 TiB | /mnt/tank/multimedia |
| `tank/TimeMachine` | 1.01 TiB | 11.2 TiB | /mnt/tank/TimeMachine |
| `tank/TimeMachine/macmini` | 1.01 TiB | 11.2 TiB | /mnt/tank/TimeMachine/macmini |
| `tank/arr-stack` | 2.87 TiB | 11.2 TiB | /mnt/tank/arr-stack |
| `tank/arr-stack/qbittorrent` | 2.87 TiB | 11.2 TiB | /mnt/tank/arr-stack/qbittorrent |
| `tank/pbs` | 293 GiB | 11.2 TiB | /mnt/tank/pbs |
| `tank/pbs/pbs_MS-01` | 147.8 GiB | 11.2 TiB | /mnt/tank/pbs/pbs_MS-01 |
| `tank/pbs/pbs_prod` | ~0 | 11.2 TiB | /mnt/tank/pbs/pbs_prod |
| `tank/Proxmox` | 279.5 GiB | 11.2 TiB | /mnt/tank/Proxmox |
| `tank/nextcloud` | 12.6 GiB | 11.2 TiB | /mnt/tank/nextcloud |
| `tank/SauvegardeHA` | 2.0 GiB | 11.2 TiB | /mnt/tank/SauvegardeHA |
| `tank/HomeAssistant` | ~0 | 11.2 TiB | /mnt/tank/HomeAssistant |

### Pool `VmApps`

| Dataset | Utilisé | Disponible | Mountpoint |
|---|---|---|---|
| `VmApps` | 88.2 GiB | 2.46 TiB | /mnt/VmApps |
| `VmApps/docker` | ~0 | 2.46 TiB | /mnt/VmApps/docker |
| `VmApps/proxmox-ssd` | ~0 | 2.46 TiB | /mnt/VmApps/proxmox-ssd |

---

## Partages SMB (CIFS)

| Nom | Chemin | Commentaire | Activé |
|---|---|---|---|
| `multimedia` | /mnt/tank/multimedia | Multimedia files | ✅ |
| `macmini` | /mnt/tank/TimeMachine/macmini | Mac mini Time Machine | ✅ |
| `pbs-prod` | /mnt/tank/pbs/pbs | Proxmox Backups Server | ✅ |
| `SauvegardeHA` | /mnt/tank/SauvegardeHA | — | ✅ |
| `qbittorrent` | /mnt/tank/arr-stack/qbittorrent | — | ✅ |
| `pbs_MS-01` | /mnt/tank/pbs/pbs_MS-01 | Proxmox Backup Server 3 MS-01 | ✅ |

---

## Partages NFS (7)

| Commentaire | Activé | R/W | Maproot |
|---|---|---|---|
| Multimedia NFS | ✅ | R/W | — |
| Proxmox NFS | ✅ | R/W | — |
| Proxmox ssd disk pool | ✅ | R/W | — |
| NFS docker ssd volume | ✅ | R/W | — |
| Next Cloud NFS | ✅ | R/W | nextcloud/nextcloud |
| arr stack volume | ✅ | R/W | — |
| (sans commentaire) | ✅ | R/W | — |

---

## Services

| Service | État | Autostart |
|---|---|---|
| SMB (cifs) | RUNNING ✅ | ✅ |
| NFS | RUNNING ✅ | ✅ |
| SSH | RUNNING ✅ | ✅ |
| FTP | RUNNING ✅ | ✅ |
| SNMP | RUNNING ✅ | ✅ |
| UPS | RUNNING ✅ | ✅ |
| iSCSI Target | STOPPED ❌ | ❌ |
| NVMeT | STOPPED ❌ | ❌ |

---

## Applications TrueNAS

| App | Version | État | MAJ dispo |
|---|---|---|---|
| `plex` | 1.3.10 | RUNNING ✅ | Non |
| `tautulli` | 1.3.8 | RUNNING ✅ | Non |

---

## VMs

| Nom | État | vCPU | RAM | Autostart |
|---|---|---|---|---|
| Ubuntu_Desktop | STOPPED | 1 | 2 GiB | Non |

---

## Tâches de snapshot automatique

| Dataset | Récursif | Rétention | Planning | Activé |
|---|---|---|---|---|
| `tank` | Non | 2 semaines | Quotidien 00:00 | ✅ |
| `VmApps` | Non | 2 semaines | Quotidien 00:00 | ✅ |

---

## Accès & API

- **IP management** : 192.168.0.241 (VLAN 0 / LAN principal)
- **IP stockage** : 192.168.50.55 (VLAN 50 / stockage, LAGG SFP+)
- **WebUI** : `https://192.168.50.55` ou `https://truenas.test.teamfnb.com`
- **API** : `https://192.168.50.55/api/v2.0/` — `Authorization: Bearer <TRUENAS_API_KEY>`
- **SSH** : `root@192.168.50.55` ou `root@192.168.0.241`
