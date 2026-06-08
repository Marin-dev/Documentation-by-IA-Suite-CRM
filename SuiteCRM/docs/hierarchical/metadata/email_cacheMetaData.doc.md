# email_cacheMetaData.php

**Chemin :** `metadata/email_cacheMetaData.php`
**Type :** config (métadonnées de table de cache email IMAP)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `email_cache` qui stocke les métadonnées des emails récupérés depuis des serveurs IMAP (via les comptes email entrants). Sert de cache local pour éviter des appels répétés au serveur IMAP lors de la consultation des boîtes mail.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['email_cache']` | variable globale PHP | Définition de la table de cache IMAP |

### Structure de la table `email_cache`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `ie_id` | id | FK vers le compte email entrant (`inbound_email.id`) |
| `mbox` | varchar(60) | Nom de la boîte mail (mailbox IMAP) |
| `subject` | varchar(255) | Sujet de l'email |
| `fromaddr` | varchar(100) | Adresse expéditeur |
| `toaddr` | varchar(255) | Adresse(s) destinataire(s) |
| `senddate` | datetime | Date d'envoi |
| `message_id` | varchar(255) | ID unique du message |
| `mailsize` | uint(16) | Taille du mail en octets |
| `imap_uid` | uint(32) | UID IMAP du message |
| `msgno` | uint(32) | Numéro séquentiel du message |
| `recent` | tinyint(1) | Drapeau IMAP : message récent |
| `flagged` | tinyint(1) | Drapeau IMAP : message marqué |
| `answered` | tinyint(1) | Drapeau IMAP : message répondu |
| `deleted` | tinyint(1) | Drapeau IMAP : message supprimé côté serveur |
| `seen` | tinyint(1) | Drapeau IMAP : message lu |
| `draft` | tinyint(1) | Drapeau IMAP : brouillon |

### Index

| Nom | Type | Champs |
|---|---|---|
| `idx_ie_id` | index | `ie_id` |
| `idx_mail_date` | index | `ie_id`, `mbox`, `senddate` |
| `idx_mail_from` | index | `ie_id`, `mbox`, `fromaddr` |
| `idx_mail_subj` | index | `subject` |
| `idx_mail_to` | index | `toaddr` |

## Interactions

- **Appelé par :** module InboundEmail, fonctionnalité de consultation des boîtes IMAP
- **Appelle :** rien

## Notes

- Pas de clé primaire définie dans ce fichier : INCONNU si une PK existe.
- Le champ `deleted` ici est un drapeau IMAP (pas le soft delete SugarCRM habituel) : représente l'état `\Deleted` côté serveur.
- La table n'a pas de colonne `body` : seules les métadonnées sont cachées, pas le contenu des emails.
