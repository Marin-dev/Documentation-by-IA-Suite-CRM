# InboundEmail.php

**Chemin :** `modules/InboundEmail/InboundEmail.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle principal des boîtes mail entrantes. Gère la configuration des comptes IMAP/POP3, la récupération et l'importation des emails entrants dans SuiteCRM, la création de leads/contacts/cases depuis les emails, et la gestion des dossiers de groupe. Classe centrale du système de réception d'emails.

## Type

model

---

## Dépendances clés

- `SugarBean` (classe parente)
- `ZBateson\MailMimeParser\MailMimeParser` — parsing des emails MIME
- `ImapHandlerFactory` (`include/Imap/ImapHandlerFactory.php`) — connexion IMAP
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `Overview` (`modules/InboundEmail/Overview.php`)
- `AOPInboundEmail` (via Services/EmailImportService)
- `BeanFactory` — instanciation Contacts, Leads, Cases, Emails, etc.

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `InboundEmail` | classe | Entité compte email entrant (IMAP/POP3) |
| `get_stored_options()` | méthode | Récupère une option de configuration stockée (from_addr, reply_to, etc.) |
| `retrieve()` | méthode | Charge le bean et initialise la connexion IMAP |
| Connexion IMAP | propriété `$conn` | Instance de connexion IMAP active |

## Interactions

- **Appelé par :** `EmailMan::sendEmail()` (chargement mailbox), `EmailImportService`, scheduler `pollMonitoredInboxes`
- **Appelle :** ImapHandlerFactory, MailMimeParser, BeanFactory (Contacts, Leads, Cases, Emails)

## Notes

- Table de stockage : INCONNU (non lu en totalité — à investiguer dans les vardefs).
- `service` peut être `imap`, `imap:ssl`, `imap:tls`, `pop3`, etc.
- `mailbox_type` distingue les boîtes de groupe (`group`) des boîtes personnelles.
- Classe volumineuse (fichier > 80 lignes lues, corps non épuisé).
