# Apple TV — Concentrateur Matter (192.168.0.34)

> Dernière mise à jour : juin 2026

---

## 📦 Matériel & Rôle

| Propriété | Valeur |
|---|---|
| IP | 192.168.0.34 (Main — 192.168.0.0/24) |
| Rôle principal | **Concentrateur Matter** pour le homelab |
| Intégration HA | `apple_tv` (chargé ✅) — entity `media_player.homepod_droite` et autres |
| Réseau | Main (192.168.0.0/24) |

---

## 🏠 Rôle Matter

L'Apple TV à 192.168.0.34 est le **Thread Border Router** et **concentrateur Matter** du homelab :
- Toute commande Matter transitant depuis Home Assistant passe par cet Apple TV
- Il héberge le réseau **Thread** (protocole bas-niveau Matter sur 802.15.4)
- Intégration HA : `matter` (✅ chargé) + `thread` (✅ chargé)

---

## 📱 Écosystème Apple Home

Appareils visibles depuis HA via Apple/Matter :
- **HomePod Droite** (`media_player.homepod_droite`)
- **HomePod Droit** (`media_player.homepod_droit`)
- **HomePod Gauche** (`media_player.homepod_gauche`)
- **HomePod Bridge** Portail (via `homekit`)
- **Eve Energy Strip** (via `homekit_controller`)

---

## ⚠️ Points d'attention

- Si l'Apple TV est éteint ou en veille, **Matter et Thread sont indisponibles** pour tout le homelab
- Vérifier que l'Apple TV ne passe pas en veille profonde (désactiver la mise en veille dans les réglages)
- L'intégration `apple_tv` dans HA permet aussi le contrôle média
