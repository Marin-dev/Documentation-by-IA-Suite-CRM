# meetings_contactsMetaData.php

**Chemin :** `metadata/meetings_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `meetings_contacts` qui matérialise la relation many-to-many entre les réunions (`Meetings`) et les contacts (`Contacts`). Inclut le statut de participation et d'acceptation.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['meetings_contacts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `meetings_contacts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `meeting_id` | varchar(36) | FK vers `meetings.id` |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `required` | varchar(1) | Participation requise (défaut : `1`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `none`) |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Meetings`, table `meetings`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Notes

- Pattern identique à `calls_contacts` (invités à une réunion).
