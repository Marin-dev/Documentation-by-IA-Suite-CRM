# Fichier : controller.php

**Chemin :** `modules/Emails/controller.php`
**Type :** PHP — Point d'entree controleur (alias)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fichier de point d'entree du controleur du module Emails. Delegue simplement vers `EmailsController.php` en respectant la convention de nommage PSR.

## Role technique

Contient uniquement un `require_once` vers `modules/Emails/EmailsController.php`. Aucune logique propre.

---

## Dependances

- `modules/Emails/EmailsController.php`

## Exports / Symboles principaux

- Aucun symbole propre — re-export de `EmailsController`

## Relations cles

- **Appele par :** routeur SuiteCRM (cherche `controller.php` dans le module)
- **Delegue vers :** `EmailsController`

---

## Points d'attention

- Ce fichier est un simple redirect de compatibilite. Toute la logique est dans `EmailsController.php`.
