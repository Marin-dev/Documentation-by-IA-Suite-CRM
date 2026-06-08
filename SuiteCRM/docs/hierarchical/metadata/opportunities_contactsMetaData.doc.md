# opportunities_contactsMetaData.php

**Chemin :** `metadata/opportunities_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `opportunities_contacts` qui matérialise la relation many-to-many entre les opportunités commerciales (`Opportunities`) et les contacts (`Contacts`). Inclut le rôle du contact dans l'opportunité.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['opportunities_contacts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `opportunities_contacts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `opportunity_id` | varchar(36) | FK vers `opportunities.id` |
| `contact_role` | varchar(50) | Rôle du contact dans l'opportunité |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Opportunities`, table `opportunities`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Notes

- `contact_role` : INCONNU — valeurs possibles à vérifier dans les vardefs du module Opportunities.
