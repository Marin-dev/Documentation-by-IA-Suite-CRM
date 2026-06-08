# 📄 ExternalOAuthConnection.php

**Chemin :** `modules/ExternalOAuthConnection/ExternalOAuthConnection.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant une connexion OAuth externe (vers Google, Microsoft, ou un fournisseur générique). Stocke les tokens d'accès et de rafraîchissement obtenus après autorisation d'un fournisseur tiers. Supporte les comptes personnels (visibles uniquement par leur créateur) et les comptes partagés (visibles par le groupe).

## Rôle technique

Classe `ExternalOAuthConnection` héritant de `Basic` (table `external_oauth_connections`). Implémente une logique ACL personnalisée : les comptes personnels (`type='personal'`) ne sont accessibles qu'à leur créateur ou aux admins. Filtre la liste SQL en conséquence. Préserve les champs `writeonly` (tokens) lors des mises à jour partielles.

---

## Dépendances clés

- `Basic` (framework SuiteCRM) — classe parente ORM
- `has_group_action_acls_defined()` — vérification des ACL de groupe
- `ACLAccess()` (parent) — délégation ACL standard
- `$current_user` — vérification d'accès personnel
- `$log` — journalisation des accès refusés

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ExternalOAuthConnection` | classe | Modèle de connexion OAuth externe |
| `hasAccessToPersonalAccount()` | méthode | Vérifie si l'utilisateur courant peut accéder à ce compte personnel |
| `ACLAccess($view, $is_owner, $in_group)` | méthode | Logique ACL personnalisée (admin-only pour edit/delete, groupe pour detail) |
| `create_new_list_query()` | méthode | Filtre : comptes non-personnels + comptes personnels du créateur courant |
| `keepWriteOnlyFieldValues()` | méthode protégée | Préserve les tokens lors des sauvegardes partielles |

## Champs principaux

| Champ | Rôle |
|---|---|
| `client_id` / `client_secret` | Identifiants du client OAuth |
| `access_token` | Token d'accès courant |
| `refresh_token` | Token de rafraîchissement |
| `token_type` | Type de token (Bearer…) |
| `expires_in` | Timestamp d'expiration |
| `type` | `personal` ou partagé |

---

## Relations clés

- **Appelé par :** `OAuthAuthorizationService`, entrypoints `redirectToExternalOAuth`, `setExternalOAuthToken`
- **Appelle :** `Basic`, `has_group_action_acls_defined()`
- **Position dans le flux global :** stockage persistant des tokens après autorisation externe (ex : connexion Gmail pour l'envoi d'e-mails)

---

## Notes

- Actions bloquées (`isNotAllowedAction`) : `export`, `import`, `massupdate`, `duplicate`.
- Actions admin-only (`isAdminOnlyAction`) : `edit`, `delete`, `editview`, `save`.
- Actions basées sur SecurityGroups (`isSecurityGroupBasedAction`) : `detail`, `detailview`, `view`.
- `keepWriteOnlyFieldValues()` évite d'écraser les tokens chiffrés si l'utilisateur laisse le champ vide lors de l'édition.
