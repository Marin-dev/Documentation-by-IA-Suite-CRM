# am_projecttemplates_users_1MetaData.php

**Chemin :** `metadata/am_projecttemplates_users_1MetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `am_projecttemplates_users_1_c` qui matérialise la relation many-to-many entre les modèles de projet (`AM_ProjectTemplates`) et les utilisateurs (`Users`). Permet d'associer des utilisateurs à un modèle de projet.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Généré par Studio (`'from_studio' => true`, date : 2014-06-20).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['am_projecttemplates_users_1']` | variable globale PHP | Définition de la table de jointure custom |

### Structure de la table `am_projecttemplates_users_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `am_projecttemplates_ida` | varchar(36) | FK vers `am_projecttemplates.id` |
| `users_idb` | varchar(36) | FK vers `users.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `am_projecttemplates_users_1spk` | primary | `id` |
| `am_projecttemplates_users_1_alt` | alternate_key | `am_projecttemplates_ida`, `users_idb` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AM_ProjectTemplates`, table `am_projecttemplates`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Fichier généré par Studio le 2014-06-20.
- Table custom (suffixe `_c`).
