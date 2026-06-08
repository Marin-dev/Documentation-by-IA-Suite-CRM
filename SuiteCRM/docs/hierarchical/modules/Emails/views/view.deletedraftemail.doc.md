# Fichier : view.deletedraftemail.php

**Chemin :** `modules/Emails/views/view.deletedraftemail.php`
**Type :** PHP — Vue AJAX (reponse suppression brouillon)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Retourne la reponse JSON apres suppression d'un brouillon. Informe le client du succes ou de l'echec.

## Role technique

Herite de `ViewAjax`. Meme structure que les autres vues AJAX email.

---

## Dependances

- **Herite de :** `ViewAjax`
- **Globales :** `$app_strings`, `$mod_strings`

## Exports / Symboles principaux

- `EmailsViewDeleteDraftEmail` — classe vue AJAX
  - `display()` — retourne JSON selon statut `draft`/`save_error`/autre

## Relations cles

- **Appele par :** `EmailsController::action_DeleteDraft()`

---

## Points d'attention

- RAS
