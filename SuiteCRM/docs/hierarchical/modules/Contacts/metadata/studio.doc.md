# studio.php

**Chemin :** `modules/Contacts/metadata/studio.php`
**Type :** PHP — configuration / metadata Studio
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Déclare les définitions de vues éditables via l'outil Studio de SuiteCRM pour le module Contacts. Référence les fichiers templates pour chaque type de vue (detail, edit, list, search) permettant leur personnalisation sans-code.

**Type :** configuration

**Configure :** Outil Studio — vues personnalisables du module Contacts (`$GLOBALS['studioDefs']['Contacts']`)

## Notes

- Similaire à `modules/Campaigns/metadata/studio.php` mais pour Contacts
- Les vues modifiables via Studio écrivent leurs changements dans `custom/modules/Contacts/metadata/`
