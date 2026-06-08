# Fichier : action_view_map.php

**Chemin :** `modules/Leads/action_view_map.php`
**Type :** `PHP`
**Categorie :** configuration (mapping action-vue)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le mapping entre les noms d'actions et les noms de vues pour le module Leads via `$action_view_map`. Permet au framework MVC de router certaines actions vers des vues personnalisees.

---

## Parametres cles

| Action | Vue |
| --- | --- |
| `editconvert` | `editConvert` |
| `editconvertlayout` | `editConvertLayout` |
| `saveandpublishlayout` | `editConvert` |
| `savelayout` | `editConvert` |
| `showduplicates` | `showDuplicates` |

## Impacte par / impacte

- Consomme par le framework de routing MVC lors de la resolution de la vue a afficher

## Points d'attention

- Fichier de configuration pur. Specifique au module Leads pour le flux de conversion de lead.
