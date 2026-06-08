# Fichier : NonGmailSentFolderHandler.php

**Chemin :** `modules/Emails/NonGmailSentFolderHandler.php`
**Type :** PHP — Service / Handler
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la copie d'un email envoye dans le dossier "Envoyes" du serveur IMAP, pour les comptes qui ne sont pas Gmail (Gmail gere cela automatiquement). Evite la duplication du mail dans la boite sortante pour les serveurs IMAP standards.

## Role technique

Classe avec gestion d'etat d'erreur via `$lastError`. La methode `storeInSentFolder()` verifie les pre-conditions (IE present, non-POP3, non-Gmail), puis connecte le serveur IMAP et utilise `imap_append` via `InboundEmail::getImap()->append()` pour copier le message.

---

## Dependances

- **Utilise :** `InboundEmail`, `SugarPHPMailer`, `LoggerManager`
- **Leve :** `EmailException`, `InvalidArgumentException`

## Exports / Symboles principaux

- `NonGmailSentFolderHandler` — classe handler
  - `storeInSentFolder(InboundEmail $ie, SugarPHPMailer $mail, $options = "\\Seen")` — copie dans le dossier Envoyes, retourne bool
  - `setLastError(int $err)`, `getLastError()`, `clearLastError()` — gestion de l'etat d'erreur
  - Constantes : `NO_ERROR` (0), `ERR_EMPTY_MAILBOX` (1), `ERR_NO_STORED_SENT_FOLDER` (2), `ERR_IS_POP3` (8), `ERR_IS_GMAIL` (9), `ERR_COULDNT_COPY_TO_SENT` (10), `UNHANDLER_ERROR` (100)

- **Consommateurs :**
  - `modules/Emails/Email.php` (attribut `$nonGmailSentFolderHandler`)

## Relations cles

- **Appelle :** `InboundEmail::connectMailserver()`, `InboundEmail::getImap()->append()`, `SugarPHPMailer::CreateBody()`, `SugarPHPMailer::CreateHeader()`
- **Appele par :** `Email` lors de l'envoi
- **Position :** post-envoi SMTP, avant la fin de la transaction d'envoi

---

## Points d'attention

- Le destructeur `__destruct()` logue une erreur fatale si `$lastError` n'est jamais lu — mecanisme de detection de fuites d'erreur.
- `clearLastError()` logue aussi une erreur fatale si appele alors qu'une erreur non lue existe.
- `copyToNonGmailSentFolder()` appelle `CreateBody()` avant `CreateHeader()` — ordre requis pour generer les IDs de boundary (commentaire ligne 243).
