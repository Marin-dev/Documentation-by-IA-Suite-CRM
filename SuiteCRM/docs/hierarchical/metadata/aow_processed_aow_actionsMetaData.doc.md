# aow_processed_aow_actionsMetaData.php

**Chemin :** `metadata/aow_processed_aow_actionsMetaData.php`
**Type :** config (métadonnées de table de jointure workflow)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `aow_processed_aow_actions` qui enregistre quelles actions d'un workflow (`AOW_Actions`) ont été exécutées pour chaque enregistrement traité (`AOW_Processed`). Permet de tracer l'exécution des workflows (AOW = Advanced OpenWorkflow).

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['aow_processed_aow_actions']` | variable globale PHP | Définition de la table de jointure workflow |

### Structure de la table `aow_processed_aow_actions`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `aow_processed_id` | varchar(36) | FK vers `aow_processed.id` |
| `aow_action_id` | varchar(36) | FK vers `aow_actions.id` |
| `status` | varchar(36) | Statut d'exécution (défaut : `Pending`) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `aow_processed_aow_actionsspk` | primary | `id` |
| `idx_aow_processed_aow_actions` | alternate_key | `aow_processed_id`, `aow_action_id` |
| `idx_actid_del_freid` | index | `aow_action_id`, `deleted`, `aow_processed_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AOW_Processed`, table `aow_processed`, clé `id`
- **RHS :** module `AOW_Actions`, table `aow_actions`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma), moteur AOW workflow
- **Appelle :** rien

## Notes

- Champ `status` spécifique à cette table de jointure (valeur par défaut : `Pending`) : permet de suivre l'état d'exécution de chaque action d'un workflow traité. Valeurs possibles au-delà de `Pending` : INCONNU (à vérifier dans le module AOW).
- Table de traçabilité workflow : critique pour l'audit des automatisations.
