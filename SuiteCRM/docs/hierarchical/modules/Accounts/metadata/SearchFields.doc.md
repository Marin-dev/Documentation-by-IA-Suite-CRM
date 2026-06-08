# Fichier : SearchFields.php

**Chemin :** `modules/Accounts/metadata/SearchFields.php`
**Type :** `PHP`
**Categorie :** configuration (champs de recherche)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les operateurs et options de recherche pour chaque champ searchable du module Accounts via `$searchFields['Accounts']`. Specifie comment chaque champ doit etre traite lors d'une recherche (operateur SQL, valeur par defaut, etc.).

---

## Parametres cles

| Parametre | Effet |
| --- | --- |
| `$searchFields['Accounts']` | Map des champs recherchables avec leurs operateurs |
| Operateurs typiques | `LIKE '%s%'`, `=`, sous-requete pour les emails |

## Impacte par / impacte

- Consomme par le framework SearchView lors de la construction des requetes de recherche
- Complementaire a `searchdefs.php` qui definit la presentation

## Points d'attention

- Fichier de configuration pur.
- Le champ `email` utilise une sous-requete specifique (heritee de `vardefs.php`).
