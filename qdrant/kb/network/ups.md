# UPS Eaton Ellipse ECO 1200 — via Raspberry Pi NUT (192.168.0.239)

> Données via NUT direct (192.168.0.239:3493)
> Dernière mise à jour : juin 2026

---

## 📦 Architecture

| Composant | Détail |
|---|---|
| **UPS** | Eaton Ellipse ECO 1200VA / 720W |
| **Superviseur NUT** | Raspberry Pi — 192.168.0.239:3493 |
| **Connexion** | USB (driver `usbhid-ups`, vendorID 0463) |
| **NUT ID** | `ellipse` |
| Intégration HA | NUT (`nut` — chargé ✅) |

Le Raspberry Pi (192.168.0.239) est connecté à l'Eaton Ellipse via USB et expose les métriques NUT sur le port 3493.

---

## 📊 État actuel

| Métrique | Valeur |
|---|---|
| État | **ALARM OL** (Online, alarme active) |
| Charge batterie | **100%** (seuil bas : 20%) |
| Autonomie | **~7 min** (443s) ⚠️ |
| Type batterie | PbAc (Plomb-Acide) |
| Tension sortie | 230V / 50Hz |
| Puissance nominale | **1200VA / ~720W** |
| Puissance réelle actuelle | **470W (65% de charge)** |
| Charge | 49% |
| Tension sortie prise principale | 230V |
| Plage transfert | 184V – 264V |

### Prises PowerShare
| Prise | Description | État | Commutable |
|---|---|---|---|
| Main Outlet | Prise principale | ✅ on | Non |
| Outlet 1 | PowerShare Outlet 1 | ✅ on | Non |
| Outlet 2 | PowerShare Outlet 2 | ✅ on | Non |
| Puissance prise principale | 25W | — | — |

---

## ⚠️ Points d'attention

- **Alarme `Battery voltage too low`** — fausse alarme NUT connue (batterie à 100%), probablement lié au driver `usbhid-ups` ou au firmware `02` de l'Ellipse ECO
- **Autonomie de seulement ~7 min** (443s) à 470W — faible pour un UPS à 100% de charge, à surveiller (batterie vieillissante ?)
- **470W sur 720W nominaux** — 65% de charge, il reste de la marge
- Numéro de série `000000000` — non renseigné dans le firmware Eaton
