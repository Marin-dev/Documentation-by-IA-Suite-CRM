# searchdefs.php

**Chemin :** `modules/Contacts/metadata/searchdefs.php`
**Type :** PHP — configuration / metadata
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les champs disponibles dans le formulaire de recherche (basique et avancée) du module Contacts. Complète `SearchFields.php` en déclarant la disposition visuelle des champs de recherche.

**Type :** configuration

**Configure :** Formulaire de recherche Contacts (`$searchdefs['Contacts']`)

## Notes

- Chargé via `metafiles.php` → `searchdefs`
- Travaille conjointement avec `SearchFields.php` (opérateurs) et `listviewdefs.php` (affichage résultats)
