# Fichier : vardefs.php

**Chemin :** `modules/FP_Event_Locations/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `fp_event_locations` pour le framework SugarCRM. Champs specifiques : `address` (required), et la relation vers `FP_events` via `fp_event_locations_fp_events_1`.

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `address` | varchar, required | Adresse du lieu |
| `fp_event_locations_fp_events_1` | link | Relation vers evenements (cote droit) |

## Impacte par / impacte
- Consomme par `FP_Event_Locations.php`, BeanFactory
- Relation avec `FP_events` : `fp_event_locations_fp_events_1`

## Points d'attention
- Table auditee.
- La relation avec FP_events est de type `link` (cote `right`).
