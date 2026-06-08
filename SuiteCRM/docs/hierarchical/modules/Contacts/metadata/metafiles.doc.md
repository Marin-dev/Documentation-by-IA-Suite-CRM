# metafiles.php

**Chemin :** `modules/Contacts/metadata/metafiles.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Registre des fichiers de métadonnées du module Contacts. Déclare les chemins vers les fichiers de définition de vues (detail, edit, list, search, popup) utilisés par le framework SuiteCRM pour charger les configurations de vues.

**Type :** configuration / metadata

---

## Configure

Variable globale `$metafiles['Contacts']` du framework SuiteCRM.

## Paramètres clés

| Clé | Fichier référencé |
|---|---|
| `detailviewdefs` | `modules/Contacts/metadata/detailviewdefs.php` |
| `editviewdefs` | `modules/Contacts/metadata/editviewdefs.php` |
| `listviewdefs` | `modules/Contacts/metadata/listviewdefs.php` |
| `searchdefs` | `modules/Contacts/metadata/searchdefs.php` |
| `popupdefs` | `modules/Contacts/metadata/popupdefs.php` |
| `searchfields` | `modules/Contacts/metadata/SearchFields.php` |

---

## Impacté par / impacte

- Framework SuiteCRM — lit ce fichier pour résoudre les chemins vers les métadonnées
- Tous les fichiers listés ci-dessus

---

## Notes

- Fichier de configuration pur sans logique — sert de registre central des métadonnées du module.
