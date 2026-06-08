# custom_fieldsMetaData.php

**Chemin :** `metadata/custom_fieldsMetaData.php`
**Type :** config (métadonnées de table de champs personnalisés)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `custom_fields` qui stocke des valeurs de champs personnalisés génériques pour n'importe quel bean. Table de stockage clé-valeur flexible avec 10 colonnes génériques (`field0` à `field9`) permettant d'étendre les données d'un bean sans modifier son schéma.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['custom_fields']` | variable globale PHP | Définition de la table de champs personnalisés |

### Structure de la table `custom_fields`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `bean_id` | varchar(36) | UUID du bean parent |
| `set_num` | int(11) | Numéro du jeu (défaut : 0) — permet plusieurs jeux par bean |
| `field0` à `field9` | varchar(255) | 10 champs génériques pour valeurs personnalisées |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `idx_beanid_set_num` | index | `bean_id`, `set_num` |

## Interactions

- **Appelé par :** framework SugarCRM (extension des beans)
- **Appelle :** rien

## Notes

- Pas de clé primaire `id` définie dans ce fichier : INCONNU si une PK existe en dehors.
- Pattern EAV (Entity-Attribute-Value) simplifié : 10 colonnes génériques nommées `field0` à `field9`, sans type ni sémantique connue à ce niveau. Nécessite une couche applicative pour interpréter les valeurs.
- `set_num` permet d'avoir plusieurs "jeux" de champs pour un même bean, ce qui multiplie les possibilités de stockage (10 × N jeux).
- Mécanisme ancien : le système moderne de Studio/custom fields utilise d'autres approches (colonnes custom dans les tables de modules via `_cstm`).
