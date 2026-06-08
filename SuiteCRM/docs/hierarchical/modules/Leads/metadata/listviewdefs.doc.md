# Fichier : listviewdefs.php

**Chemin :** `modules/Leads/metadata/listviewdefs.php`
**Type :** `PHP`
**Categorie :** configuration (vue liste)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les colonnes de la vue liste du module Leads via `$listViewDefs['Leads']`.

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$listViewDefs['Leads']` | Colonnes : name, status, lead_source, email1, phone_work, account_name |

## Points d'attention

- Fichier de configuration pur. Le champ `name` (prenom+nom) est un champ calcule par `Person`.
