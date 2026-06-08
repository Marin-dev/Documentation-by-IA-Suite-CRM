# modules_array.php

**Chemin :** `modules/MailMerge/modules_array.php`
**Type :** PHP - Configuration
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit la liste des modules supportés dans le wizard Mail Merge : Accounts, Cases, Contacts, Leads, Opportunities.

## Type
config

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `$modules_array` — tableau associatif des 5 modules supportés

## Interactions
- **Appelé par :** `Step3.php`, scripts du wizard MailMerge
- **Appelle :** rien

## Notes
- Liste hardcodée — à modifier pour ajouter de nouveaux modules compatibles.
