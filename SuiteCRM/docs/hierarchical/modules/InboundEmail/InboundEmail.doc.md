# InboundEmail.php

**Chemin :** `modules/InboundEmail/InboundEmail.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean principal des boites de reception IMAP/POP3. Gere la connexion aux serveurs de messagerie entrants, la recuperation des emails, leur importation dans le CRM (creation d'enregistrements `Emails`), et le traitement des reponses de campagne (tracking). Supporte les boites personnelles, partagees et de groupe.

**Type :** model

---

## Dependances cles
- `SugarBean` (classe parente)
- `ZBateson\MailMimeParser\MailMimeParser` (parsing MIME)
- `ImapHandlerFactory` (`include/Imap/ImapHandlerFactory.php`)
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `Overview.php` (EmailMan)
- `temp.php` (EmailMan)
- `BeanFactory` (Emails, Cases, Contacts, Leads...)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `InboundEmail` | classe | Bean boite de reception email |
| `get_stored_options()` | methode | Lit les options serialisees du compte (from_addr, reply_to_name...) |
| `connectMailserver()` | methode | Ouvre la connexion IMAP/POP3 |
| `importMessages()` | methode | Importe les messages du serveur dans la DB |
| `handleCreateCase()` / `handleCaseReply()` | methodes | Gestion des tickets (AOP) |

---

## Interactions
- **Appele par :** `EmailMan::sendEmail()`, `EmailImportService`, `AOPInboundEmail`, scheduler
- **Appelle :** `ImapHandlerFactory`, `MailMimeParser`, `Emails`, `Cases`

---

## Notes
- Classe tres large (INCONNU : nombre exact de lignes). Beaucoup de methodes legacy coexistent avec le nouveau code IMAP.
- Utilise `$GLOBALS['jjwg_config']` par certains flux INCONNU.
