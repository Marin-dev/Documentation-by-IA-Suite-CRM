# Fichier : CallsQuickCreate.php

**Chemin :** `modules/Calls/CallsQuickCreate.php`
**Type :** vue (formulaire rapide)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Formulaire de creation rapide d'un appel depuis un subpanel ou la barre de raccourcis. Equivalent de `MeetingsQuickCreate` pour le module Calls.

## Role technique
Etend `QuickCreate`. Pre-remplit date/heure, direction, statut et construit les dropdowns de selection d'heure selon le format utilisateur.

---

## Dependances cles
- `QuickCreate` (`include/EditView/QuickCreate.php`)
- `BeanFactory::newBean('Calls')`

## Exports / Symboles principaux
- `CallsQuickCreate` — classe — formulaire rapide appels

---

## Points d'attention
Structure identique a `MeetingsQuickCreate`.
