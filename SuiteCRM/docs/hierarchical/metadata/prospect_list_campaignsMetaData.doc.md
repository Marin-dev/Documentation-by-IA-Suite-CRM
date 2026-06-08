# prospect_list_campaignsMetaData.php

**Chemin :** `metadata/prospect_list_campaignsMetaData.php`
**Type :** config (métadonnées de table de jointure campagnes)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `prospect_list_campaigns` qui matérialise la relation many-to-many entre les listes de prospects (`ProspectLists`) et les campagnes marketing (`Campaigns`). Permet d'associer des listes de destinataires à des campagnes.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['prospect_list_campaigns']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `prospect_list_campaigns`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `prospect_list_id` | varchar(36) | FK vers `prospect_lists.id` |
| `campaign_id` | varchar(36) | FK vers `campaigns.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `ProspectLists`, table `prospect_lists`, clé `id`
- **RHS :** module `Campaigns`, table `campaigns`, clé `id`

## Notes

- RAS.
