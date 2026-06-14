# PiKVM — Accès KVM TrueNAS (192.168.0.38)

> Généré automatiquement depuis l'API PiKVM
> Dernière mise à jour : juin 2026

---

## 📦 Matériel & Système

| Propriété | Valeur |
|---|---|
| IP | 192.168.0.38 (Main — 192.168.0.0/24) |
| Accès | https://192.168.0.38 |
| Hostname | pikvm |
| Hardware | Raspberry Pi 4 Model B Rev 1.5 |
| Modèle PiKVM | v2 |
| Série RPi | 10000000E325F97A |
| OS Kernel | Linux 6.12.56-1-rpi (aarch64) |
| KVMD version | 4.121 |
| Streamer | ustreamer |
| Vidéo | HDMI |

---

## 🎯 Cible

**TrueNAS Scale** (192.168.0.241 / https://truenas.test.teamfnb.com)

Accès console physique au serveur TrueNAS — BIOS, boot, récupération hors OS.

---

## 💻 État système

| Métrique | Valeur |
|---|---|
| CPU | 2% |
| RAM | 18.3% utilisée (1.5 Go libre / 1.8 Go total) |
| Temp CPU | 39.4°C |
| Throttling | ❌ aucun (undervoltage/throttle OK) |

---

## ⚙️ Services actifs

| Service | État |
|---|---|
| Janus WebRTC Gateway | ✅ actif |
| KVMD Media Proxy | ✅ actif |
| Web Terminal (ttyd) | ✅ actif |
| IPMI daemon | ❌ désactivé |
| VNC (port 5900) | ❌ désactivé |

---

## 🔑 Accès

- Interface web : **https://192.168.0.38**
- Auth API : `X-KVMD-User: admin` / `X-KVMD-Passwd: admin` ⚠️ mot de passe API par défaut non changé
- Auth web : `admin` / `12fev65`
- Réseau : Main (192.168.0.0/24)

---

## ⚠️ Points d'attention

- **Mot de passe API par défaut** (`admin:admin`) — à changer via `kvmd-htpasswd set admin`
- **VNC désactivé** — accès uniquement via interface web ou WebRTC
- **IPMI désactivé** — pas d'accès IPMI distant
- Connecté au **TrueNAS** (192.168.0.241) — seul accès console physique si TrueNAS est inaccessible réseau
