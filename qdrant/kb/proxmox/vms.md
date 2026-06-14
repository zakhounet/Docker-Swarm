# Proxmox — VMs & Conteneurs LXC

> Généré automatiquement via pvesh sur Tom (192.168.0.45)
> Dernière mise à jour : juin 2026

---

## Vue d'ensemble

| VMID | Nom | Type | Nœud | CPU | RAM | Disque | Status | Tags |
|---|---|---|---|---|---|---|---|---|
| 105 | Terramaster-Cloudflare | LXC | Zakh | 2 | 1 Go | 10 Go | ⚠️ running (à fermer) | 235 |
| 110 | Docker | VM | Tom | 6 | 24 Go | 250 Go | ⚠️ running (à fermer) | 50-97 |
| 199 | test-ssh | VM | Ilan | 2 | 4 Go | 32 Go | ⚠️ running (tests uniquement) | — |
| 400 | Plex | LXC | Zakh | 4 | 8 Go | 20 Go | ✅ running | oci |
| 601 | docker-manager-01 | VM | Tom | 4 | 16 Go | 100 Go | ✅ running | swarm |
| 602 | docker-manager-02 | VM | Zakh | 4 | 16 Go | 100 Go | ✅ running | swarm |
| 603 | docker-manager-03 | VM | Ilan | 4 | 16 Go | 100 Go | ✅ running | swarm |
| 900 | pbs-server | VM | Tom | 4 | 8 Go | 32 Go | ✅ running | pbs |

---

## Détail par VM / LXC

### VM 110 — Docker (Tom) ⚠️ À fermer
- **Rôle** : VM Docker standalone — **à supprimer**
- **CPU** : 6 vCPU | **RAM** : 24 Go | **Disque** : 250 Go (CephRBD, SSD, discard, iothread)
- **Réseau** : `vmbr1` (VLAN prod 20 Gbps), MAC `BC:24:11:26:79:DD`
- **onboot** : ✅ (sera désactivé à la suppression)

### VM 199 — test-ssh (Ilan) ⚠️ Tests uniquement
- **Rôle** : VM de test SSH — non critique, pas de service en production
- **CPU** : 2 vCPU | **RAM** : 4 Go | **Disque** : 32 Go (TrueNAS NFS, qcow2)
- **Réseau** : `vmbr0` (admin), firewall activé, MAC `BC:24:11:B8:A5:2F`
- **onboot** : ✅

### LXC 105 — Terramaster-Cloudflare (Zakh) ⚠️ À fermer
- **Rôle** : Tunnel Cloudflare uniquement (le NAS Terramaster n'est plus utilisé) — **à supprimer**
- **CPU** : 2 vCPU | **RAM** : 1 Go | **Disque** : 10 Go (CephRBD)
- **Réseau** : `vmbr0`, DHCP, firewall activé
- **onboot** : ✅ (sera désactivé à la suppression)
- **Note** : Le tunnel Cloudflare est désormais assuré par le service launchd sur le M4 Pro (`hermes-webhook.teamfnb.com`)

### LXC 400 — Plex (Zakh)
- **Rôle** : Serveur Plex **de backup** (OCI container — tag `oci`)
- **OS** : Ubuntu (unprivileged, nesting=1)
- **CPU** : 4 vCPU | **RAM** : 8 Go + 512 Mo swap | **Disque** : 20 Go (CephRBD)
- **Réseau** : `vmbr0`, IP fixe **192.168.0.135/24**, gateway 192.168.0.1, firewall activé
- **GPU passthrough** : `/dev/dri/renderD128` (Intel Iris Xe — transcodage hardware), uid/gid=911
- **Montage médias** : `/mnt/pve/Multimedia` → monté sur `/media/library` dans le conteneur
- **onboot** : ✅

### VM 601 — docker-manager-01 (Tom)
- **Rôle** : Manager Docker Swarm #1 — tag `swarm`
- **CPU** : 4 vCPU | **RAM** : 16 Go | **Disque** : 100 Go (CephRBD, SSD, discard, iothread)
- **Réseau** : `vmbr1`, MTU 9000, queues=4, MAC `BC:24:11:DD:2E:1F`
- **HA** : `hastate=started` | **onboot** : ❌ (géré par HA)
- **IP** : 192.168.50.61

### VM 602 — docker-manager-02 (Zakh)
- **Rôle** : Manager Docker Swarm #2 — tag `swarm`
- **CPU** : 4 vCPU | **RAM** : 16 Go | **Disque** : 100 Go (CephRBD, SSD, discard, iothread)
- **Réseau** : `vmbr1`, MTU 9000, queues=4, MAC `BC:24:11:5C:F1:58`
- **HA** : `hastate=started` | **onboot** : ❌ (géré par HA)
- **IP** : 192.168.50.62

### VM 603 — docker-manager-03 (Ilan)
- **Rôle** : Manager Docker Swarm #3 — tag `swarm`
- **CPU** : 4 vCPU | **RAM** : 16 Go | **Disque** : 100 Go (CephRBD, SSD, discard, iothread)
- **Réseau** : `vmbr1`, MTU 9000, queues=4, MAC `BC:24:11:2A:82:80`
- **HA** : `hastate=started` | **onboot** : ❌ (géré par HA)
- **IP** : 192.168.50.63

### VM 900 — pbs-server (Tom)
- **Rôle** : Proxmox Backup Server — tag `pbs`
- **CPU** : 4 vCPU | **RAM** : 8 Go | **Disque** : 32 Go (CephRBD, SSD, discard, iothread)
- **Réseau** : `vmbr1`, MTU 9000, queues=4, MAC `BC:24:11:DB:FC:62`
- **IP** : 192.168.50.100
- **onboot** : ✅

---

## Stockage utilisé

| Storage | Type | Utilisé par |
|---|---|---|
| `cephtb4-storage` | CephRBD | VMs 110, 105, 400, 601, 602, 603, 900 |
| `TrueNas-NFS` | NFS → TrueNAS | VM 199 |

---

## Réseau

| Bridge | Usage | MTU |
|---|---|---|
| `vmbr0` | Admin / accès 192.168.0.x | 1500 |
| `vmbr1` | Production Swarm / 192.168.50.x | 9000 (jumbo) |
