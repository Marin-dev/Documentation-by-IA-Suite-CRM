# AOR_Field.php

**Chemin :** `modules/AOR_Fields/AOR_Field.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele representant un champ (colonne) selectionne pour affichage dans un rapport AOR. Chaque instance correspond a une colonne de resultat avec ses options (label, fonction d'agregation, tri, groupement, total, format).

## Role technique
Etend `Basic`. La methode `save_lines` parse le POST et cree/met a jour les champs. Valide les fonctions (`field_function`) et les directions de tri (`sort_by`) via les listes autorisees de `aor_utils.php`.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aor_report_id` | FK vers le rapport parent |
| `field_order` | Ordre de la colonne |
| `field` | Nom du champ technique |
| `display` | Booleen — afficher cette colonne |
| `label` | Libelle de la colonne |
| `field_function` | Fonction SQL (COUNT, SUM, AVG, MIN, MAX) |
| `sort_by` | Direction de tri (ASC, DESC) |
| `format` | Format d'affichage (ex: pour les dates) |
| `group_by` | Booleen — grouper par ce champ (GROUP BY) |
| `group_display` | Niveau de groupement hierarchique (entier) |
| `total` | Type de total (SUM, AVG, COUNT) |
| `module_path` | Chemin de module serialise en base64 |
| `link` | Booleen — ajouter un lien cliquable sur la valeur |

## Relations cles
- **Appele par :** `AOR_Report->save()` (via `save_lines`), `AOR_Report->build_report_query_select()`, `build_report_html()`
- **Table DB :** `aor_fields`
- **Relation parent :** `aor_report_id` vers `aor_reports` (one-to-many)

---

## Points d'attention
- Les valeurs de `field_function` sont validees contre `getAorAllowedFieldFunctions()` — une valeur non autorisee est mise a `null` avec un warning log.
- Le `group_display` est gere separement des autres champs : il est calcule depuis `$post_data['aor_fields_group_display']` (tableau d'index de lignes) et non depuis le champ direct.
- Si le champ `field` (nom technique) est vide apres trim, la ligne est ignoree (pas de sauvegarde).
