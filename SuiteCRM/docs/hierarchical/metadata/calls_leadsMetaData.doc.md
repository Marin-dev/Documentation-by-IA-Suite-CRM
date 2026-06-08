# calls_leadsMetaData.php

**Chemin :** `metadata/calls_leadsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `calls_leads` qui matérialise la relation many-to-many entre les appels (`Calls`) et les prospects (`Leads`). Permet d'enregistrer quels prospects ont participé à un appel.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['calls_leads']` | variable globale PHP | Définition de la table de jointure appels-prospects |

### Structure de la table `calls_leads`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `call_id` | varchar(36) | FK vers `calls.id` |
| `lead_id` | varchar(36) | FK vers `leads.id` |
| `required` | varchar(1) | Participation requise (défaut : `1`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `none`) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `calls_leadspk` | primary | `id` |
| `idx_lead_call_call` | index | `call_id` |
| `idx_lead_call_lead` | index | `lead_id` |
| `idx_call_lead` | alternate_key | `call_id`, `lead_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Calls`, table `calls`, clé `id`
- **RHS :** module `Leads`, table `leads`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Calls
- **Appelle :** rien

## Notes

- Structure identique à `calls_contacts` et `calls_users` (invités à un appel).
