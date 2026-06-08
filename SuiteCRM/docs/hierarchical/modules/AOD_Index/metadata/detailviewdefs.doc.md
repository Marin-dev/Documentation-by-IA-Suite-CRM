# detailviewdefs.php

**Chemin :** `modules/AOD_Index/metadata/detailviewdefs.php`
**Configure :** Mise en page de la vue detail du module AOD_Index
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definit `$viewdefs['AOD_Index']['DetailView']` — la structure en panneaux de la page de detail d'un enregistrement AOD_Index. Dispose 3 panneaux : identite (name + assigned_user), dates (date_entered + date_modified avec auteur), description.

## Parametres cles
| Panneau | Champs |
|---|---|
| 1 | `name`, `assigned_user_name` |
| 2 | `date_entered` (avec `created_by_name`), `date_modified` (avec `modified_by_name`) |
| 3 | `description` |

Boutons : EDIT, DUPLICATE, DELETE, FIND_DUPLICATES. Largeur 2 colonnes.

## Impacte par / impacte
- Charge par le framework MVC SugarCRM pour le rendu de `DetailView`
- Reference dans `metafiles.php`

## Points d'attention
- RAS — fichier de configuration standard genere.
