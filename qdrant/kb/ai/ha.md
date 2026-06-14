# Home Assistant — HAOS sur Mac mini Intel 2017

> Généré automatiquement depuis l'API HA
> Dernière mise à jour : juin 2026

---

## 📦 Système

| Propriété | Valeur |
|---|---|
| Hôte | Mac mini Intel 2017 — 192.168.0.25 |
| Version | HA Core 2026.6.3 |
| Accès local | http://192.168.0.25:8123 |
| Accès interne | https://ha.test.teamfnb.com (Traefik) |
| Timezone | Europe/Paris |
| Localisation | Jonage, Rhône-Alpes (45.799°N, 5.052°E) |
| Personnes | Franck, Katia |

---

## 📊 Entités (2 175 total)

| Domaine | Nombre |
|---|---|
| sensor | 786 |
| switch | 344 |
| binary_sensor | 288 |
| button | 158 |
| number | 86 |
| select | 82 |
| light | 80 |
| media_player | 63 |
| update | 58 |
| event | 58 |
| scene | 58 |
| cover | 30 |
| camera | 18 |
| automation | 11 |
| climate | 7 |
| **Total unavailable/unknown** | **487** ⚠️ |

---

## 🔌 Intégrations (49 domaines)

### ✅ Actives
| Intégration | Détail |
|---|---|
| anker_solix | Panneaux solaires Anker |
| apple_tv | HomePod Droite |
| bambu_lab | Imprimante 3D (03919D4B2000399) |
| brother | MFC-9330CDW (imprimante) |
| cast | Google Cast |
| daikin_onecta | Climatisation Daikin |
| dlna_dms | Media server kyfran Ubuntu |
| esphome | ESPHome (everything-presence-one) |
| go2rtc | Streams caméras |
| hacs | HACS |
| homekit | HASS Bridge Portail |
| homekit_controller | Eve Energy Strip |
| hue | Philips Hue Bridge |
| ibeacon | Trackers iBeacon |
| matter | Matter |
| meross_lan | Prises Meross |
| meteo_france | Météo Jonage |
| mobile_app | Mac mini de Franck |
| mqtt | Mosquitto broker |
| music_assistant | Music Assistant |
| nissan_connect | Véhicule Nissan |
| nut | UPS (192.168.0.239:3493) |
| overkiz | Somfy/overkiz (volets) |
| samsungtv | Samsung The Frame 75 |
| sonos | Enceintes Sonos |
| spook | Spook (utilitaires) |
| sun | Soleil |
| tapo_control | Caméras Tapo (192.168.30.150) |
| technitiumdns | DNS Technitium Pi4 |
| thread | Thread |
| tplink | Sèche-linge P110M |
| unifiprotect | UniFi Protect (caméras) |
| vesync | Levoit (purificateurs) |
| youtube | YouTube Franck |
| fontawesome | Icônes |
| radio_browser | Radio Browser |
| backup | Backup HA |
| hassio | Supervisor |
| analytics | Analytics |

### ⚠️ En erreur / dégradé
| Intégration | Problème |
|---|---|
| androidtv_remote | SHIELD inaccessible |
| bluetooth | Bluetooth hci0 en erreur |
| dlna_dmr | Samsung The Frame 75 |
| ipp | Imprimante Brother |
| oralb | Brosse IO Series 68FE |
| switchbot | Hub3 (50E8) |
| unifi | UDM-SE (cloud URL) |
| upnp | UDM-SE UPnP |
| wyoming | Piper (TTS local) |
| zha | Sonoff Zigbee dongle |

---

## 🤖 Automations (11)

| Automation | État |
|---|---|
| Notifiy: send dynamique notif | ✅ |
| Sésame ouvre toi (portail) | ✅ |
| Sésame ferme toi (portail) | ✅ |
| temp < 24 | ⛔ désactivée |
| temp > 27 | ⛔ désactivée |
| Offline detection Z2M devices (last_seen KYF) | ✅ |
| Gestion du cycle de lavage | ✅ |
| Bouton Lave-Linge (Hue) | ✅ |
| Début Lave-Linge - Enregistrement Heure | ✅ |
| Gestion luminaire Allée | ✅ |
| Gestion lumière Appartement | ✅ |

---

## 🔗 Connexion MCP Hermes

- **ha-mcp add-on** installé sur HAOS (89 outils)
- URL Hermes → HA : `http://192.168.0.25:8123`
- URL Claude Desktop → HA : `https://ha.test.teamfnb.com`
- Token : Long-Lived Access Token (`HASS_TOKEN` dans `.env`)

---

## 🏠 Appareils notables

- **Domotique** : Hue, Meross, Levoit (Vesync), Overkiz (volets Somfy), TPLink Tapo
- **Multimédia** : Sonos, Samsung The Frame 75, HomePod, Music Assistant
- **IoT** : ESPHome (presence sensor), Zigbee (Sonoff dongle ZHA), Matter, iBeacon
- **Véhicule** : Nissan Connect
- **Énergie** : Anker Solix (solaire), UPS (NUT 192.168.0.239)
- **Sécurité** : UniFi Protect (caméras), Homebridge (portail HomeKit)
- **Réseau** : Technitium DNS

---

## ⚠️ Points d'attention

- **487 entités unavailable/unknown** — nettoyage entités orphelines recommandé
- **ZHA en erreur** — Sonoff Zigbee dongle à vérifier
- **Wyoming/Piper** en erreur — TTS local HS
- **SwitchBot Hub3** inaccessible
- **Bluetooth** en erreur — USB BT controller Apple
