# Fichier vardefs.php

**Chemin :** `modules/AOR_Reports/vardefs.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Définit le schéma de base de données et les métadonnées du bean `AOR_Report`. Déclare les champs, relations et options du module AOR_Reports.

## Type
config

---

## Paramètres clés

| Paramètre | Valeur | Effet |
|---|---|---|
| `table` | `aor_reports` | Table principale |
| `audited` | `true` | Piste d'audit activée |
| `report_module` | enum `aor_moduleList` | Module cible du rapport |
| `graphs_per_row` | int (défaut 2) | Nombre de graphiques par ligne |
| `field_lines` | function non-db | Affiche le widget de champs via `display_field_lines()` |
| `condition_lines` | function non-db | Affiche le widget de conditions via `display_condition_lines()` |
| `aor_fields` | link one-to-many | Relation vers AOR_Fields |
| `aor_conditions` | link one-to-many | Relation vers AOR_Conditions |
| `aor_charts` | link one-to-many | Relation vers AOR_Charts |
| `aor_scheduled_reports` | link one-to-many | Relation vers AOR_Scheduled_Reports |

## Relations déclarées

| Relation | Type | Modules |
|---|---|---|
| `aor_reports_aor_fields` | one-to-many | AOR_Reports → AOR_Fields |
| `aor_reports_aor_conditions` | one-to-many | AOR_Reports → AOR_Conditions |
| `aor_scheduled_reports_aor_reports` | one-to-many | AOR_Reports → AOR_Scheduled_Reports |

## Notes
- Utilise le template `VardefManager::createVardef` avec mixins `basic`, `assignable`, `security_groups`.
- `optimistic_locking` et `unified_search` activés.
