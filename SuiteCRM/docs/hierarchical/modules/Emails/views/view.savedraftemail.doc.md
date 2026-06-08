# Fichier : view.savedraftemail.php

**Chemin :** `modules/Emails/views/view.savedraftemail.php`
**Type :** PHP — Vue AJAX (reponse sauvegarde brouillon)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Retourne la reponse JSON apres sauvegarde d'un brouillon. Confirme au client la sauvegarde ou signale une erreur.

## Role technique

Herite de `ViewAjax`. Meme structure que `view.sendemail.php` mais pour le statut `draft`.

---

## Dependances

- **Herite de :** `ViewAjax`
- **Globales :** `$app_strings`

## Exports / Symboles principaux

- `EmailsViewSaveDraftEmail` — classe vue AJAX
  - `display()` — retourne JSON `{data}` si statut `draft`, `{errors}` si `save_error` ou autre

## Relations cles

- **Appele par :** `EmailsController::action_SaveDraft()`

---

## Points d'attention

- RAS
