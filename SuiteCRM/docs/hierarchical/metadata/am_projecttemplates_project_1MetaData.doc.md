# am_projecttemplates_project_1MetaData.php

**Chemin :** `metadata/am_projecttemplates_project_1MetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `am_projecttemplates_project_1_c` qui matérialise la relation entre les modèles de projet (`AM_ProjectTemplates`) et les projets (`Project`). Permet de lier un modèle de projet à un projet concret.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Généré par Studio (`'from_studio' => true`, date : 2014-06-04).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['am_projecttemplates_project_1']` | variable globale PHP | Définition de la table de jointure custom |

### Structure de la table `am_projecttemplates_project_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `am_projecttemplates_project_1am_projecttemplates_ida` | varchar(36) | FK vers `am_projecttemplates.id` |
| `am_projecttemplates_project_1project_idb` | varchar(36) | FK vers `project.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `am_projecttemplates_project_1spk` | primary | `id` |
| `am_projecttemplates_project_1_ida1` | index | `am_projecttemplates_project_1am_projecttemplates_ida` |
| `am_projecttemplates_project_1_alt` | alternate_key | `am_projecttemplates_project_1project_idb` |

### Relation

- **Type déclaré :** `true_relationship_type = one-to-many` (mais implémenté en many-to-many via table de jointure)
- **LHS :** module `AM_ProjectTemplates`, table `am_projecttemplates`, clé `id`
- **RHS :** module `Project`, table `project`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Incohérence notable : `true_relationship_type = 'one-to-many'` mais `relationship_type = 'many-to-many'` dans la définition de la relation. La valeur `true_relationship_type` reflète l'intention métier (un modèle génère un projet), mais l'implémentation reste une table de jointure many-to-many.
- Noms de colonnes très longs (nom complet de la relation concaténé avec le module).
