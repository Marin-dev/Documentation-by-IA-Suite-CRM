# Fichier AOR_Field.php

**Chemin :** `modules/AOR_Fields/AOR_Field.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle d'un champ de résultat associé à un rapport AOR. Chaque enregistrement représente une colonne du rapport : champ source, label, affichage, fonction d'agrégation, tri, format de date, groupement. Gère la sauvegarde en masse depuis le formulaire POST avec validation des fonctions et directions de tri.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php` — utilitaires partagés
- `modules/AOR_Reports/aor_utils.php` — `getAorAllowedFieldFunctions()`, `getAorAllowedSortDirections()`, `fixUpFormatting()`
- `BeanFactory`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_Field` | classe | Bean champ de rapport |
| `save_lines()` | méthode | Sauvegarde/supprime les lignes de champs depuis POST avec validation |

### Champs importants
| Champ | Rôle |
|---|---|
| `aor_report_id` | Lien vers le rapport parent |
| `field_order` | Ordre d'affichage dans le tableau |
| `field` | Nom technique du champ |
| `display` | Si 1 : colonne visible dans le résultat |
| `label` | Libellé affiché |
| `field_function` | Fonction SQL (COUNT, SUM, AVG, MIN, MAX) |
| `sort_by` | Direction de tri (ASC/DESC) |
| `format` | Format date (si applicable) |
| `group_by` | Inclure dans le GROUP BY |
| `group_display` | Niveau de groupement (1..N pour groupements imbriqués) |
| `link` | Si 1 : rendre le champ cliquable (lien DetailView) |
| `total` | Type de total de colonne (SUM/COUNT/AVG) |
| `module_path` | Chemin de module sérialisé base64 |

## Interactions
- **Appelé par :** `AOR_Report::save()`, `AOR_Report::build_report_query_select()`, `AOR_Report::getReportFields()`
- **Table BD :** `aor_fields`

## Notes
- `save_lines()` valide `field_function` et `sort_by` via `getAorAllowedFieldFunctions()` / `getAorAllowedSortDirections()` — valeurs invalides sont rejetées (log warning + null).
- `module_path` est sérialisé en base64 identiquement à AOR_Condition.
- Le champ `group_display` utilise un mécanisme spécial : le POST envoie les numéros de ligne qui ont le groupement activé, pas un simple booléen par ligne.
