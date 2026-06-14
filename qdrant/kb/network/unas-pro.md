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

## 🔒 Sécurité

- SSH activé
- Accès local : https://192.168.0.17
- Accès interne : https://unas.test.teamfnb.com
- Connecté au réseau Main (192.168.0.0/24) via 10G SFP+

---

## ⚠️ Points d'attention

- **CPU à 81°C** — températures à surveiller
- **Disque slot 2** : 17 149h (le plus usé de l'ensemble)
- **enp0s1 (ETH)** non connecté — seul le SFP+ 10G est actif
