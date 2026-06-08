# Fichier : view.sendemail.php

**Chemin :** `modules/Emails/views/view.sendemail.php`
**Type :** PHP — Vue AJAX (reponse d'envoi)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Retourne la reponse JSON d'un envoi d'email. Informe le client JavaScript du succes ou de l'echec de l'envoi.

## Role technique

Herite de `ViewAjax`. `display()` inspecte le statut du bean et retourne un JSON structure (`data` si succes, `errors` si echec).

---

## Dependances

- **Herite de :** `ViewAjax`
- **Globales :** `$app_strings`

## Exports / Symboles principaux

- `EmailsViewSendEmail` — classe vue AJAX
  - `display()` — retourne JSON `{data: {type, id, title}}` ou `{errors: {type, id, title}}`

## Relations cles

- **Appele par :** `EmailsController::action_send()` (via `$this->view = 'sendemail'`)

---

## Points d'attention

- Statuts geres : `sent` (succes), `send_error` (echec), autre (erreur generique).
