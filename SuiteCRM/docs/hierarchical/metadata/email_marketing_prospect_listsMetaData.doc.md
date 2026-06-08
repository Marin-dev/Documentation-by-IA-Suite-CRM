# email_marketing_prospect_listsMetaData.php

**Chemin :** `metadata/email_marketing_prospect_listsMetaData.php`
**Type :** config (métadonnées de table de jointure campagne email)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `email_marketing_prospect_lists` qui matérialise la relation many-to-many entre les campagnes email marketing (`EmailMarketing`) et les listes de prospects (`ProspectLists`). Permet d'associer une ou plusieurs listes de destinataires à une campagne email.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['email_marketing_prospect_lists']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `email_marketing_prospect_lists`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `prospect_list_id` | varchar(36) | FK vers `prospect_lists.id` |
| `email_marketing_id` | varchar(36) | FK vers `email_marketing.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `email_mp_listspk` | primary | `id` |
| `email_mp_prospects` | alternate_key | `email_marketing_id`, `prospect_list_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `EmailMarketing`, table `email_marketing`, clé `id`
- **RHS :** module `ProspectLists`, table `prospect_lists`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Campaigns / EmailMarketing
- **Appelle :** rien

## Notes

- RAS.
