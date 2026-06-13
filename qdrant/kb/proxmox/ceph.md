# Ceph — Cluster MS-01 (Tom / Zakh / Ilan)

> **Source** : sessions Claude 2025-2026, validées en production
> **Version Ceph** : Squid
> **Dernière mise à jour** : 2026-06-10
> **Contexte matériel** : 3× Minisforum MS-01, OSD sur Samsung 990 Pro NVMe 2 To (1 par nœud), réseau cluster sur mesh Thunderbolt 4 (10.100.0.0/24, OpenFabric/FRR)

---

## Architecture réseau Ceph

Le cluster Ceph utilise le mesh Thunderbolt 4 comme réseau cluster dédié (réplication et backfill), distinct du réseau public. Le routage entre les nœuds passe par OpenFabric (FRR). Les adresses des interfaces dummy sont : Tom 10.100.0.102, Zakh 10.100.0.103, Ilan 10.100.0.104.

Les pools actifs sont CephFS (stockage partagé Docker Swarm, monté sur /mnt/cephfs) et RBD (disques VM).

---

## cluster_addr : pinner sur les interfaces dummy, jamais sur les liens point-à-point

Le paramètre `cluster_addr` de chaque OSD doit être explicitement fixé sur l'adresse de l'interface dummy OpenFabric du nœud (10.100.0.10x), et non sur les adresses des liens point-à-point Thunderbolt 4.

**Raison** : lors d'une recalculation de routes OpenFabric (reboot d'un nœud, lien TB4 instable), les adresses point-à-point deviennent temporairement injoignables, ce qui provoque des timeouts de heartbeat OSD et des flapping d'OSD marqués down à tort. Les adresses dummy restent stables quelle que soit la topologie des routes.

**Symptôme observé** : OSD marqués down/up en boucle pendant les recalculs de routes, alors que les disques étaient sains.

---

## mClock : profil et particularités (Squid)

Le scheduler mClock est configuré avec le profil `high_client_ops` : priorité aux I/O clients (VMs, CephFS) sur les opérations de fond (scrub, backfill, recovery).

**Particularité Squid** : `osd_scrub_sleep` est TOUJOURS écrasé à 0 par mClock. Inutile de le régler — c'est le profil mClock qui gouverne la priorisation du scrub, pas ce paramètre.

---

## osd_deep_scrub_interval : appliquer sur OSD ET MGR

Le paramètre `osd_deep_scrub_interval` doit être appliqué aux deux tiers de démons : OSD et MGR.

**Raison** : le MGR évalue les warnings de santé (« pgs not deep-scrubbed in time ») de façon indépendante, avec sa propre lecture du paramètre. Si seul le tier OSD est modifié, le MGR continue d'émettre des warnings basés sur l'ancienne valeur.

```bash
ceph config set osd osd_deep_scrub_interval <valeur_secondes>
ceph config set mgr osd_deep_scrub_interval <valeur_secondes>
```

---

## Migration de VM : offline préférable pour les workloads actifs

Pour les VMs à charge active dont les disques sont sur CephFS/RBD, la migration offline (stop → migrate → start) est largement préférable à la live migration.

**Raison** : le stockage étant partagé (Ceph), il n'y a aucun transfert de disque — seule la RAM serait transférée en live, ce qui est long et fragile pour une VM chargée. En offline, le downtime se réduit à quelques secondes (stop + start), sans risque d'instabilité.

**Procédure** :
1. Arrêter la VM
2. Migrer (transfert de configuration quasi instantané, stockage déjà partagé)
3. Redémarrer la VM sur le nœud cible

---

## Reboot de nœud : attendre HEALTH_OK avant toute migration

Après le redémarrage d'un nœud Proxmox du cluster, attendre systématiquement :
1. Le retour de Ceph à l'état `HEALTH_OK` (`ceph -s`)
2. La stabilisation des heartbeats OSD (plus aucun flapping dans `ceph osd tree` / logs)

avant de migrer des VMs vers ou depuis ce nœud.

**Raison** : pendant la phase de peering/recovery post-reboot, les latences I/O sont dégradées et les heartbeats instables. Une migration lancée dans cette fenêtre risque blocages et timeouts.

---

## Incident résolu : duplicate IP (VM 101 / Ilan)

La VM 101 sur Ilan a présenté des problèmes réseau dont la cause racine était une IP dupliquée héritée d'un ancien cluster. Le correctif appliqué : fix multiqueue sur la NIC + sysctl buffers. À retenir : en cas de comportement réseau erratique d'une VM, vérifier les conflits d'IP avec d'anciennes machines avant d'optimiser la pile réseau.

---

## Points de vigilance ouverts

- **PBS retention** : politique de rétention sous-configurée. Recommandation validée : keep-daily 7, keep-weekly 4, keep-monthly 3. Datastore PBS (VM 900, 192.168.50.100) sur CIFS vers TrueNAS Scale.
