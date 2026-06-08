# Fichier : ContactsQuickCreate.php

**Chemin :** `modules/Contacts/ContactsQuickCreate.php`
**Type :** PHP - Composant UI (creation rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit le formulaire de creation rapide de contacts accessible depuis les sous-panels d'autres modules. Permet de creer un contact sans quitter la vue courante.

## Role technique

Etend `QuickCreate` (`include/EditView/QuickCreate.php`). Override `process()` pour forcer le chargement des `$mod_strings` en langue courante avant le rendu.

---

## Dependances cles

- `include/EditView/QuickCreate.php` — classe parente
- `return_module_language()` — chargement des traductions

## Exports / Symboles principaux

- `ContactsQuickCreate` — classe
  - `process($checkFormName, $formName)` — prepare le formulaire de creation rapide (l.54)

## Consommateurs identifies

- Framework SuiteCRM (sous-panels avec creation rapide activee)
- Vue de creation rapide Contacts

## Relations cles

- **Position dans le flux :** Formulaire inline de creation de contact

---

## Points d'attention

- Force le rechargement de `$mod_strings` pour le module Contacts — evite les problemes de langue dans les contextes cross-module.
