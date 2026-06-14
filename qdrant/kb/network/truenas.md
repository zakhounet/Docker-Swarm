# TrueNAS Scale — Serveur NAS

> Généré automatiquement depuis l'API TrueNAS Scale v2
> Dernière mise à jour : juin 2026

---

## 📦 Matériel & Système

| Propriété | Valeur |
|---|---|
| Hostname | truenas |
| IP | 192.168.50.55 (bond007 — VLAN 50 Swarm) |
| Accès | https://truenas.test.teamfnb.com |
| Version | TrueNAS Scale 25.10.3 |
| CPU | AMD Ryzen 5 PRO 5650G (Radeon intégré) |
| RAM | 125.2 Go |
| Uptime | ~57 jours |
| Timezone | Europe/Paris |

---

## 💾 Pools ZFS

### Pool `tank` — Données principales

| Propriété | Valeur |
|---|---|
| État | ✅ ONLINE / healthy |
| Capacité totale | 43.6 To |
| Utilisé | 27.8 To |
| Libre | 15.9 To (~36%) |
| Dernier scan | FINISHED |

### Pool `VmApps` — VMs & Apps

| Propriété | Valeur |
|---|---|
| État | ✅ ONLINE / healthy |
| Capacité totale | 3.6 To |
| Utilisé | 0.1 To |
| Libre | 3.5 To (~97%) |

---

## 🖥️ Disques (15)

| Disque | Modèle | Taille | Série |
|---|---|---|---|
| sda | Samsung SSD 870 EVO 1TB | 0.91 To | S75CNX0WB10150H |
| sdb | Samsung SSD 870 EVO 1TB | 0.91 To | S75CNX0WB05982T |
| sdc | Samsung SSD 870 EVO 1TB | 0.91 To | S75CNX0WB00556N |
| sdd | Toshiba HDWG460 | 5.46 To | 9380A00SFA4H |
| sde | Toshiba HDWG460 | 5.46 To | 9340A005FA4H |
| sdf | Samsung SSD 870 QVO 1TB | 0.91 To | S5RRNF1W405033N |
| sdg | Crucial CT240BX500SSD1 | 0.22 To | 2337E876E749 |
| sdh | Toshiba HDWG460 | 5.46 To | 7370A0KNFA4H |
| sdi | Toshiba HDWG460 | 5.46 To | 73X0A006FA4H |
| sdj | Toshiba HDWG460 | 5.46 To | 73G0A0G3FA4H |
| sdk | Toshiba HDWG460 | 5.46 To | 73F0A04EFA4H |
| sdl | Toshiba HDWG460 | 5.46 To | 73E0A00QFA4H |
| sdm | Toshiba HDWG460 | 5.46 To | Z330A06RFR1H |
| sdn | Kingston SA400S37240G | 0.22 To | 50026B77859C592E |
| nvme0n1 | Samsung SSD 970 EVO Plus 2TB | 1.82 To | S6P1NF0W910187X |

---

## 📁 Datasets

| Dataset | Utilisé | Type | Usage |
|---|---|---|---|
| `tank` | 20.2 To total | FILESYSTEM | Racine |
| `tank/multimedia` | 15.7 To | FILESYSTEM | Médias (Plex) |
| `tank/arr-stack` | 2.9 To | FILESYSTEM | Stack *arr + qBittorrent |
| `tank/pbs` | 293.7 Go | FILESYSTEM | Proxmox Backup Server |
| `tank/TimeMachine` | 1.0 To | FILESYSTEM | Time Machine (macmini) |
| `tank/Proxmox` | 276.9 Go | FILESYSTEM | Stockage VMs Proxmox |
| `tank/nextcloud` | 12.6 Go | FILESYSTEM | Nextcloud |
| `tank/SauvegardeHA` | 2.0 Go | FILESYSTEM | Sauvegarde Home Assistant |
| `tank/HomeAssistant` | 0 | FILESYSTEM | Données HA (NFS) |
| `VmApps` | 88.2 Go total | FILESYSTEM | VMs & Apps TrueNAS |
| `VmApps/docker` | 0 | FILESYSTEM | Docker |
| `VmApps/proxmox-ssd` | 0 | FILESYSTEM | Proxmox SSD pool |

---

## 🔗 Partages SMB

| Nom | Chemin | État |
|---|---|---|
| multimedia | `/mnt/tank/multimedia` | ✅ |
| macmini | `/mnt/tank/TimeMachine/macmini` | ✅ (Time Machine) |
| pbs-prod | `/mnt/tank/pbs/pbs` | ✅ |
| SauvegardeHA | `/mnt/tank/SauvegardeHA` | ✅ |
| qbittorrent | `/mnt/tank/arr-stack/qbittorrent` | ✅ |
| pbs_MS-01 | `/mnt/tank/pbs/pbs_MS-01` | ✅ |

---

## 📤 Exports NFS

| Chemin | Accès |
|---|---|
| `/mnt/tank/multimedia` | Réseau ouvert |
| `/mnt/tank/Proxmox` | Réseau ouvert |
| `/mnt/VmApps/proxmox-ssd` | Réseau ouvert |
| `/mnt/VmApps/docker` | Réseau ouvert |
| `/mnt/tank/nextcloud` | Réseau ouvert |
| `/mnt/tank/arr-stack/qbittorrent` | Réseau ouvert |
| `/mnt/tank/HomeAssistant` | Réseau ouvert |

---

## ⚙️ Services

| Service | État | Autostart |
|---|---|---|
| SMB (CIFS) | ✅ RUNNING | ✅ |
| NFS | ✅ RUNNING | ✅ |
| FTP | ✅ RUNNING | ✅ |
| SSH | ✅ RUNNING | ✅ |
| SNMP | ✅ RUNNING | ✅ |
| UPS | ✅ RUNNING | ✅ |
| iSCSI | ⛔ STOPPED | ❌ |
| NVMeT | ⛔ STOPPED | ❌ |

---

## 🖥️ VMs

| Nom | État | vCPU | RAM |
|---|---|---|---|
| Ubuntu_Desktop | ⛔ STOPPED | 1 | 2 Go |

---

## 📱 Applications TrueNAS

| App | État | Version |
|---|---|---|
| Plex | ✅ RUNNING | 1.3.10 |
| Tautulli | ✅ RUNNING | 1.3.8 |

---

## 📸 Tâches de snapshots ZFS

| Dataset | Rétention | Actif |
|---|---|---|
| `tank` | 2 semaines | ✅ |
| `VmApps` | 2 semaines | ✅ |

---

## 🌐 Réseau

| Interface | IP | Notes |
|---|---|---|
| bond007 | 192.168.50.55 | Interface principale — VLAN 50 (Swarm) |
| enp38s0 | — | |
| enp39s0 | — | |
| enp36s0f0np0 | — | |
| enp36s0f1np1 | — | |
| enxbe5b2f037f9f | — | |

---

## ⚠️ Points d'attention

- **NFS sans restriction IP** — tous les exports NFS sont ouverts (hosts=[], networks=[]), pas de restriction par IP/subnet
- **FTP actif** — service FTP en autostart, à vérifier si nécessaire
- **tank à 64%** — 15.9 To libres, à surveiller avec multimedia (~15.7 To)
