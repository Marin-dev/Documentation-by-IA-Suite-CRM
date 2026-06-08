# am_tasktemplates_am_projecttemplatesMetaData.php

**Chemin :** `metadata/am_tasktemplates_am_projecttemplatesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `am_tasktemplates_am_projecttemplates_c` qui matérialise la relation entre les modèles de tâche (`AM_TaskTemplates`) et les modèles de projet (`AM_ProjectTemplates`). Permet de composer un modèle de projet à partir de plusieurs modèles de tâche.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Généré le 2014-05-30.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['am_tasktemplates_am_projecttemplates']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `am_tasktemplates_am_projecttemplates_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `am_tasktemplates_am_projecttemplatesam_projecttemplates_ida` | varchar(36) | FK vers `am_projecttemplates.id` |
| `am_tasktemplates_am_projecttemplatesam_tasktemplates_idb` | varchar(36) | FK vers `am_tasktemplates.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `am_tasktemplates_am_projecttemplatesspk` | primary | `id` |
| `am_tasktemplates_am_projecttemplates_ida1` | index | colonne `_ida` |
| `am_tasktemplates_am_projecttemplates_alt` | alternate_key | colonne `_idb` |

### Relation

- **Type déclaré :** `true_relationship_type = one-to-many` (implémenté en many-to-many)
- **LHS :** module `AM_ProjectTemplates`, table `am_projecttemplates`, clé `id`
- **RHS :** module `AM_TaskTemplates`, table `am_tasktemplates`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Noms de colonnes extrêmement longs (concaténation du nom complet de la relation + module) : risque de dépassement de longueur selon le SGBD.
- `true_relationship_type = 'one-to-many'` : sémantiquement un modèle de projet contient plusieurs modèles de tâche (one-to-many), mais l'implémentation physique reste many-to-many.
