# Fichier : detailviewdefs.php

**Chemin :** `modules/Leads/metadata/detailviewdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit la disposition des champs dans la vue de detail (`DetailView`) du module Leads via `$viewdefs['Leads']['DetailView']`.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$viewdefs['Leads']['DetailView']` | Layout de la vue detail |
| Panneaux | Informations personnelles, adresse, champs de qualification (lead_source, status, etc.) |

## Impacte par / impacte

- Consomme par le framework MetaData pour generer la vue DetailView
- Peut etre surcharge dans `custom/Extension/modules/Leads/Ext/Layoutdefs/`

## Points d'attention

- Fichier de configuration pur. Le bouton "Convert Lead" est gere dans `views/view.detail.php` (pas dans ce fichier).
