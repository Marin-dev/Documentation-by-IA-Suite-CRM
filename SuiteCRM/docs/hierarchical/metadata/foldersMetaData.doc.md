# foldersMetaData.php

**Chemin :** `metadata/foldersMetaData.php`
**Type :** config (métadonnées de tables dossiers email — fichier multi-tables)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de **trois tables** du système de dossiers email de SuiteCRM :
1. `folders` — dossiers email (arborescents, avec support des dossiers dynamiques)
2. `folders_subscriptions` — abonnements utilisateurs à des dossiers
3. `folders_rel` — lien polymorphe entre dossiers et beans (emails, etc.)

## Type

config

## Exports / Symboles principaux

### Table `folders`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `name` | varchar(255) | Nom du dossier (requis) |
| `folder_type` | varchar(25) | Type du dossier (nullable) |
| `parent_folder` | id | FK auto-référentielle pour l'arborescence (nullable) |
| `has_child` | bool | Indique si le dossier a des sous-dossiers (défaut : 0) |
| `is_group` | bool | Dossier partagé/groupe (défaut : 0) |
| `is_dynamic` | bool | Dossier dynamique (défaut : 0) |
| `dynamic_query` | text | Requête SQL pour dossier dynamique |
| `assign_to_id` | id | Utilisateur assigné (nullable) |
| `created_by` | id | Créateur (requis) |
| `modified_by` | id | Modificateur (requis) |
| `deleted` | bool | Soft delete (défaut : 0) |

### Table `folders_subscriptions`

| Colonne | Type | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID |
| `folder_id` | id | FK vers `folders.id` |
| `assigned_user_id` | id | FK vers `users.id` |

### Table `folders_rel`

Table de jointure polymorphe dossier ↔ beans.

| Colonne | Type | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID |
| `folder_id` | id | FK vers `folders.id` |
| `polymorphic_module` | varchar(25) | Module du bean (discriminant) |
| `polymorphic_id` | id | UUID du bean |
| `deleted` | bool | Soft delete (défaut : 0) |

## Interactions

- **Appelé par :** module InboundEmail, interface de messagerie SuiteCRM
- **Appelle :** rien

## Notes

- `is_dynamic` + `dynamic_query` : les dossiers dynamiques exécutent une requête SQL pour peupler leur contenu — risque de sécurité si la requête est modifiable par l'utilisateur.
- `folders_rel.polymorphic_module` : longueur varchar(25) — peut tronquer certains noms de modules longs.
- Structure arborescente via `parent_folder` auto-référentielle sans niveau de profondeur limité.
