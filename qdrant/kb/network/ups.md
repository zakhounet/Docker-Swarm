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

- **Alarme `Battery voltage too low`** active malgré 100% de charge — anomalie à investiguer (possible fausse alarme NUT ou batterie vieillissante)
- 470W de charge sur l'UPS — à identifier quels équipements sont branchés dessus
