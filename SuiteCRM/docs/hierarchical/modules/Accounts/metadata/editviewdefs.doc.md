# Fichier : editviewdefs.php

**Chemin :** `modules/Accounts/metadata/editviewdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit la disposition des champs dans la vue d'edition (`EditView`) du module Accounts via `$viewdefs['Accounts']['EditView']`. Specifie les champs editables, leur ordre, les validations cote client et la disposition en panneaux.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$viewdefs['Accounts']['EditView']` | Layout de la vue edition |
| Champs requis | Indiques par `required => true` dans chaque entree de champ |
| Champs relates | Selectors popup pour `parent_name`, `assigned_user_name`, `campaign_name` |

## Impacte par / impacte

- Consomme par le framework MetaData pour generer le formulaire EditView
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`

## Points d'attention

- Fichier de configuration pur. Les modifications doivent passer par Studio.
- Partage la structure de panneau avec `detailviewdefs.php`.
