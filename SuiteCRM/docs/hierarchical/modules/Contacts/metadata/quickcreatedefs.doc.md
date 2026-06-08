# quickcreatedefs.php

**Chemin :** `modules/Contacts/metadata/quickcreatedefs.php`
**Type :** PHP — configuration / metadata
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les champs du formulaire de création rapide (QuickCreate) du module Contacts. Ce formulaire allégé est affiché dans les dashlets et sous-panneaux pour créer un contact sans naviguer vers la vue d'édition complète.

**Type :** configuration

**Configure :** Vue QuickCreate Contacts (`$viewdefs['Contacts']['QuickCreate']`)

## Notes

- Utilisé par `ContactsViewQuickcreate` (`views/view.quickcreate.php`)
- Contient un sous-ensemble des champs de `editviewdefs.php` (formulaire simplifié)
