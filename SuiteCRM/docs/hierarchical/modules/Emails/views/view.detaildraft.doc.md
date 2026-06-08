# Fichier : view.detaildraft.php

**Chemin :** `modules/Emails/views/view.detaildraft.php`
**Type :** PHP — Vue (detail brouillon)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue detail d'un email en brouillon. Affiche les informations du brouillon avec les sous-panels actives.

## Role technique

Herite de `ViewDetail`. Utilise `EmailsDraftDetailView` specialisee. `type` est 'DetailDraft', sous-panels actives.

---

## Dependances

- **Herite de :** `ViewDetail`
- **Imports :** `modules/Emails/include/DetailView/EmailsDraftDetailView.php`

## Exports / Symboles principaux

- `EmailsViewDetailDraft` — classe vue
  - `preDisplay()` — prepare `EmailsDraftDetailView`

## Relations cles

- **Appele par :** `EmailsController::action_DetailDraftView()`

---

## Points d'attention

- `show_subpanels = true` contrairement a certaines autres vues email.
