# Fichier : Email.php

**Chemin :** `modules/Emails/Email.php`
**Type :** PHP — Model (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe centrale du module Emails. Represente un email dans SuiteCRM (recu, envoye, brouillon, archive). Assure la persistance en base (table `emails`), l'envoi via SMTP, l'archivage IMAP et les liaisons CRM avec les autres modules (Contacts, Comptes, Leads, Opportunites, etc.).

## Role technique

Herite de `Basic` (SugarBean). Encapsule tous les champs d'un email (expediteur, destinataires, corps HTML/texte, pieces jointes, statut, type). Fournit les methodes d'envoi (`send()`, `sendFromOutbound()`), de manipulation des adresses (`parse_addrs()`), de gestion des pieces jointes (`handleAttachments()`, `handleMultipleFileAttachments()`), et de synchronisation IMAP.

---

## Dependances

- **Imports principaux :**
  - `EmailFromValidator` (`modules/Emails/EmailFromValidator.php`) — validation de l'adresse expediteur
  - `EmailException` (`modules/Emails/EmailException.php`) — exceptions metier email
  - `SugarPHPMailer` (`include/SugarPHPMailer.php`) — envoi SMTP
  - `UploadFile` / `UploadMultipleFiles` (`include/`) — gestion des pieces jointes
  - `NonGmailSentFolderHandler` (`modules/Emails/NonGmailSentFolderHandler.php`) — copie dans le dossier Envoyes non-Gmail
- **Variables d'environnement :** aucune directe (via `$sugar_config`)

## Exports / Symboles principaux

- `Email` — classe (model) — bean principal du module Emails
  - Proprietes publiques : `from_addr`, `to_addrs`, `cc_addrs`, `bcc_addrs`, `description_html`, `description`, `status`, `type`, `mailbox_id`, `uid`, `flagged`, `seen`, `draft`, `et` (EmailUI), etc.
  - Constantes d'erreur : `NO_ERROR`, `ERR_NOT_STORED_AS_SENT`, `ERR_NO_IE`, `ERR_CODE_SHOULD_BE_INT`, `UNHANDLED_LAST_ERROR`
  - Table : `emails`
  - `$relationshipMap` : correspondance modules CRM -> relations emails_beans

- **Consommateurs identifies :**
  - `modules/Emails/EmailsController.php`
  - `modules/Emails/Save.php`
  - `modules/Emails/Delete.php`
  - `modules/Emails/Compose.php`
  - `modules/Emails/views/view.*.php`
  - `modules/Emails/include/ListView/ListViewDataEmails.php`

## Relations cles

- **Appelle :** `SugarPHPMailer`, `EmailFromValidator`, `NonGmailSentFolderHandler`, `BeanFactory`, `OutboundEmail`
- **Appele par :** `EmailsController`, `Save.php`, `Delete.php`, vues, dashlets
- **Position dans le flux :** coeur du module ; cree, sauvegarde et envoie les emails ; relie les emails aux beans CRM via `emails_beans`

---

## Points d'attention

- Le champ `type` (archived/draft/out/forward) conditionne tout le comportement de sauvegarde.
- `$et` (instance de `EmailUI`) est attache dynamiquement ; absence possible si `email2init()` n'est pas appele.
- Dual representation des adresses : `from_addr` (string brut) + `from_addr_name` (nom + adresse) + `From`/`FromName` (convention PHPMailer) — source de confusion documentee dans `EmailFromValidator`.
- `$nonGmailSentFolderHandler` et `$tempEmailAtSend` sont des attributs proteges lies a la logique de copie dans le dossier Envoyes.
- La propriete `$new_schema = true` (ligne 251) indique la version 2.0 du schema email.
