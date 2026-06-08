# vardefs.php

**Chemin :** `modules/Users/vardefs.php`
**Type :** PHP (configuration / vardefs)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Définit le schéma de données de l'entité User : colonnes de la table `users`, relations, et index. C'est le contrat structurel qui pilote l'ORM SugarBean et Studio.

## Type
config

## Dépendances clés
- `$dictionary` global SuiteCRM — registre des vardefs

## Paramètres clés

| Champ | Type DB | Remarque |
|---|---|---|
| `user_name` | varchar(60) | Login, requis, non visible en édition Studio |
| `user_hash` | varchar(255) | Hash bcrypt du mot de passe, `sensitive`, non reportable, non visible API |
| `system_generated_password` | bool | Indique si le mot de passe a été généré automatiquement |
| `pwd_last_changed` | datetime | Date du dernier changement de mot de passe |
| `authenticate_id` | varchar(100) | Clé externe pour plugins d'authentification (LDAP, SAML…) |
| `sugar_login` | bool | Force l'auth SuiteCRM même si auth externe configurée (défaut: 1) |
| `is_admin` | bool | Administrateur système (défaut: 0) |
| `external_auth_only` | bool | Authentification externe exclusive |
| `factor_auth` | bool | Authentification à deux facteurs activée |
| `factor_auth_interface` | enum | Interface 2FA choisie (dropdown `user_factor_auth_interface_dom`) |
| `portal_only` | bool | Utilisateur portail uniquement |
| `is_group` | bool | Utilisateur de groupe (boite mail partagée, etc.) |
| `status` | enum | Active / Inactive (dropdown `user_status_dom`) |
| `aclroles` | link | Relation vers `acl_roles_users` |
| `SecurityGroups` | link | Relation vers `securitygroups_users` |

## Relations définies
| Relation | Type | Table pivot / clé |
|---|---|---|
| `user_direct_reports` | one-to-many | `users.reports_to_id` |
| `users_users_signatures` | one-to-many | `users_signatures.user_id` |
| `users_email_addresses` | many-to-many | `email_addr_bean_rel` |
| `users_calendar_accounts` | one-to-many | `calendar_accounts.calendar_user_id` |

## Index
- Clé primaire : `id`
- Index composé : `user_name, is_group, status, last_name, first_name, id`

## Notes
- Nombreux champs avec `'api-visible' => false` — non exposés via l'API REST.
- `UserType` est un champ virtuel (`source: non-db`) utilisé dans les vues pour discriminer le type (Regular / Admin / Group / Portal).
- Les champs `accept_status_fields` (calls et meetings) sont des champs `relate` spéciaux portant les informations de statut des sous-panneaux.
