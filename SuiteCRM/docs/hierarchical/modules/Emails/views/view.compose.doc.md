# Fichier : view.compose.php

**Chemin :** `modules/Emails/views/view.compose.php`
**Type :** PHP — Vue (compose email)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue de composition d'email. Affiche le formulaire de redaction avec TinyMCE, la gestion des pieces jointes, les champs destinataires et le selecteur de compte expediteur.

## Role technique

Herite de `ViewEdit`. `preDisplay()` configure `ComposeView` (editview specialisee), assigne les variables Smarty (INBOUND_ID, TEMP_ID, RECORD, ACTION, IS_MODAL, ATTACHMENT_NAME, EMAIL_TINYMCE_CONFIG), charge le template `ComposeView.tpl`.

---

## Dependances

- **Herite de :** `ViewEdit`
- **Imports :** `modules/Emails/include/ComposeView/ComposeView.php`
- **Utilise :** `SugarTinyMCE`, `BeanFactory`, `jsLanguage`

## Exports / Symboles principaux

- `EmailsViewCompose` — classe vue
  - `preDisplay()` — preparation de la vue
  - `getEditView()` — fabrique l'instance `ComposeView`
  - `getSignatures(User $user)` — DEPRECATED — recupere les signatures
  - `setupTinyMCEConfig()` — configure TinyMCE (prive)

## Relations cles

- **Appele par :** `EmailsController::action_ComposeView()`, `action_ReplyTo()`, `action_ReplyToAll()`, `action_Forward()`
- **Utilise :** `ComposeView`, `SugarTinyMCE`

---

## Points d'attention

- `getSignatures()` est marquee deprecated (ligne 148).
- Si `return_module` est absent de la requete, tous les elements de UI (titre, header, footer, JS) sont masques — mode modal.
- L'erreur TinyMCE est geree silencieusement (try/catch avec log).
