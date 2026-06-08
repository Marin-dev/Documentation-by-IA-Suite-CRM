# calls_contactsMetaData.php

**Chemin :** `metadata/calls_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `calls_contacts` qui matérialise la relation many-to-many entre les appels téléphoniques (`Calls`) et les contacts (`Contacts`). Permet d'enregistrer quels contacts ont participé à un appel, ainsi que leur statut d'acceptation.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['calls_contacts']` | variable globale PHP | Définition de la table de jointure appels-contacts |

### Structure de la table `calls_contacts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `call_id` | varchar(36) | FK vers `calls.id` |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `required` | varchar(1) | Participation requise (défaut : `1`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `none`) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `calls_contactspk` | primary | `id` |
| `idx_con_call_call` | index | `call_id` |
| `idx_con_call_con` | index | `contact_id` |
| `idx_call_contact` | alternate_key | `call_id`, `contact_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Calls`, table `calls`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Calls
- **Appelle :** rien

## Notes

- Champs `required` et `accept_status` spécifiques à cette jointure : indiquent si la participation est obligatoire et si l'invité a accepté/refusé.
- Même pattern que `calls_leads` et `calls_users` (invités à un appel).
