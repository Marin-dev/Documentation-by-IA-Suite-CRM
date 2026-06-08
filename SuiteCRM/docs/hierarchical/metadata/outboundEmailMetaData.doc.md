# outboundEmailMetaData.php

**Chemin :** `metadata/outboundEmailMetaData.php`
**Type :** config (métadonnées de table de configuration email sortant)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `outbound_email` qui stocke les configurations de comptes email sortants (serveurs SMTP) de SuiteCRM. Chaque enregistrement représente un compte SMTP (système ou utilisateur) utilisé pour l'envoi d'emails.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['OutboundEmail']` | variable globale PHP | Définition de la table `outbound_email` |

### Structure de la table `outbound_email`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `name` | varchar(50) | Nom du compte email sortant (requis) |
| `type` | varchar(15) | Type de compte : `user` (défaut), `system`, etc. |
| `user_id` | id | FK vers l'utilisateur propriétaire (requis) |
| `smtp_from_name` | varchar | Nom d'affichage de l'expéditeur |
| `smtp_from_addr` | varchar | Adresse email de l'expéditeur |
| `mail_sendtype` | varchar(8) | Type d'envoi (défaut : `smtp`) |
| `mail_smtptype` | varchar(20) | Type SMTP (défaut : `other` ; ex. gmail, etc.) |
| `mail_smtpserver` | varchar(100) | Adresse du serveur SMTP |
| `mail_smtpport` | int(5) | Port SMTP (défaut : 0) |
| `mail_smtpuser` | varchar(100) | Utilisateur SMTP |
| `mail_smtppass` | varchar(100) | Mot de passe SMTP (stocké en clair) |
| `mail_smtpauth_req` | bool | Authentification SMTP requise (défaut : 0) |
| `mail_smtpssl` | int(1) | Chiffrement SSL/TLS : 0=aucun, 1=SSL, 2=TLS |

## Interactions

- **Appelé par :** module OutboundEmail, module Campaigns, envoi d'emails
- **Appelle :** rien

## Notes

- Section `indices` entièrement commentée dans le fichier source : aucun index défini → pas de clé primaire explicite en base. Point d'attention : INCONNU si une PK est créée par un mécanisme externe.
- `mail_smtppass` stocké en clair (varchar) : risque de sécurité — vérifier si un chiffrement est appliqué en amont.
- `type` = `user` (défaut) ou `system` : les comptes système sont partagés, les comptes utilisateur sont personnels.
- `reportable: false` sur tous les champs : les données SMTP n'apparaissent pas dans les rapports.
