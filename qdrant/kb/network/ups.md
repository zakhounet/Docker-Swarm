# UPS Eaton Ellipse — 192.168.0.239

> Données via intégration NUT dans Home Assistant
> Dernière mise à jour : juin 2026

---

## 📦 Matériel

| Propriété | Valeur |
|---|---|
| Modèle | Eaton Ellipse (nom HA : Ellipse) |
| IP NUT | 192.168.0.239:3493 |
| Intégration HA | NUT (`nut` — chargé ✅) |

---

## 📊 État actuel

| Métrique | Valeur |
|---|---|
| État | **Alarm, Online** |
| Code d'état | `ALARM OL` |
| **⚠️ Alarme active** | `Battery voltage too low!` |
| Charge batterie | **100%** |
| Autonomie | **443 min** (~7h) |
| Consigne batterie faible | 20% |
| Tension sortie | 230V |
| Charge actuelle | 49% (470W) |
| Signal sonore | Activé |

---

## ⚠️ Points d'attention

- **Alarme NUT `Battery voltage too low`** active alors que la batterie est à 100% — probablement une fausse alarme ou un souci de calibration NUT. La charge à 49% (470W) est normale.
- 470W sur une capacité nominale → vérifier quelle est la puissance nominale de l'Ellipse pour estimer la marge restante
