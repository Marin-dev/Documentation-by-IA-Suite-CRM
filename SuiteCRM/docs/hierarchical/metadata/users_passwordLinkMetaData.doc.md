# users_passwordLinkMetaData.php

**Chemin :** `metadata/users_passwordLinkMetaData.php`
**Type :** config (metadonnees de table de securite)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table `users_password_link` qui stocke les liens de reinitialisation de mot de passe pour les utilisateurs. Chaque lien est associe a un utilisateur et expire (gestion via `date_generated`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['users_password_link']` | variable globale PHP | Definition de la table des liens de reinitialisation |

### Structure de la table `users_password_link`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | id (requis) | Cle primaire UUID |
| `keyhash` | varchar(255) | Hash du lien de reinitialisation (requis) |
| `user_id` | varchar(36) | FK vers `users.id` |
| `username` | varchar(36) | Nom d'utilisateur associe au lien |
| `date_generated` | datetime | Date de generation du lien |
| `deleted` | bool | Soft delete (nullable) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `users_password_link_pk` | primary | `id` |
| `idx_username` | index | `username` |

### Relation

- Pas de bloc `relationships` dans ce fichier.

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema), module Users, systeme de reinitialisation de mot de passe
- **Appelle :** rien

## Notes

- Protege par la constante `sugarEntry`.
- Le `keyhash` est probablement un token unique genere cote serveur pour valider la demande de reinitialisation.
- La colonne `date_generated` permet d'implementer une expiration du lien (logique de verification externe a cette table).
- SuiteCRM 2011-2021 (date de copyright etendue par rapport aux autres fichiers).
