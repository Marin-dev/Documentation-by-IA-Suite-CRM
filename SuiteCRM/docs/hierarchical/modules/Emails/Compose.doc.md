# Fichier : Compose.php

**Chemin :** `modules/Emails/Compose.php`
**Type :** PHP — Script d'action (compose)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Prépare les donnees pour le formulaire de composition d'email (compose package). Gere plusieurs cas : appel depuis client externe, compose rapide (quickCreate), compose complet depuis un enregistrement parent (Case, KBDocument, Quote), reponse/transfert, ou compose vierge.

## Role technique

Script procedural. La fonction `generateComposeDataPackage()` construit un tableau `$ret` avec les destinataires, le sujet, le corps et les pieces jointes pre-remplies selon le contexte. `initFullCompose()` encode ce tableau en JSON et l'injecte dans la page ou le repond via AJAX.

---

## Dependances

- **Globales :** `$beanList`, `$beanFiles`, `$mod_strings`, `$current_user`
- **Utilise :** `BeanFactory`, `EmailUI`, `KBDocument`, `getJSONobj()`
- **Inclut :** `modules/Emails/EmailUI.php` (pour reponse/transfert et KBDocument)

## Exports / Symboles principaux

- `generateComposeDataPackage(array $data, bool $forFullCompose = true)` — construit le package compose
- `initFullCompose(array $ret)` — encode et sort le JSON ou injecte dans la page
- `getQuotesRelatedData(array $data)` — recupere les donnees liees aux devis

## Relations cles

- **Appelle :** `EmailUI::getDraftAttachments()`, `EmailUI::handleReplyType()`, `EmailUI::displayComposeEmail()`, `KBDocument::get_kbdoc_body_without_incrementing_count()`
- **Appele par :** URL `index.php?module=Emails&action=Compose` et appels AJAX depuis les sous-panels

---

## Points d'attention

- Ce fichier est un script legacy (non MVC) qui co-existe avec la vue `view.compose.php`.
- La condition `isset($data['listViewExternalClient'])` permet un usage par des clients externes.
- Le mode `replyAll` (ligne 251) filtre les adresses de l'utilisateur courant des CC pour eviter l'auto-envoi.
- Le cas `KBDocument` charge `EmailUI` manuellement (ligne 139).
