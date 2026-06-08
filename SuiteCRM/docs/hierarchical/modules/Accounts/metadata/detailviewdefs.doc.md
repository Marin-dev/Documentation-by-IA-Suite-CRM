# Fichier : detailviewdefs.php

**Chemin :** `modules/Accounts/metadata/detailviewdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit la disposition des champs dans la vue de detail (`DetailView`) du module Accounts via le tableau `$viewdefs['Accounts']['DetailView']`. Specifie quels champs sont affiches, leur ordre, leur disposition en panneaux, et les options de chaque champ (lecture seule, liens, etc.).

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$viewdefs['Accounts']['DetailView']` | Layout de la vue detail |
| Panneaux de champs | Organisation en groupes : informations generales, adresse de facturation, adresse de livraison, autres |
| Champs relates | `parent_name`, `assigned_user_name`, `campaign_name` avec liens vers modules |

## Impacte par / impacte

- Consomme par le framework MetaData pour generer la vue DetailView
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`
- Dependance : `ViewDetail` du framework

## Points d'attention

- Fichier de configuration pur (pas de logique). Les modifications doivent passer par Studio ou les surcharges custom.
- La structure en panneaux permet d'organiser visuellement les champs par groupe thematique.
