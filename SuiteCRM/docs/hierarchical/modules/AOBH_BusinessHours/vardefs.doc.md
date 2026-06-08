# ⚙️ vardefs.php (AOBH_BusinessHours)

**Chemin :** `modules/AOBH_BusinessHours/vardefs.php`
**Configure :** Schéma de la table `aobh_businesshours`
**Dernière mise à jour doc :** 2026-05-31

## 🎯 Ce que ce fichier configure
Définit les champs du module Business Hours : `day` (nom du jour), `opening_hours` (int heure d'ouverture), `closing_hours` (int heure de fermeture), `open_status` (bool ouvert/fermé).

## 🔑 Paramètres clés
| Paramètre | Valeur probable | Effet |
|---|---|---|
| `day` | string (Monday..Sunday) | Identifie le jour |
| `opening_hours` / `closing_hours` | int (0-23) | Plage d'ouverture |
| `open_status` | bool | Ce jour est-il ouvert |

## 💡 Points d'attention
- Fichier non lu intégralement — détails INCONNU.
