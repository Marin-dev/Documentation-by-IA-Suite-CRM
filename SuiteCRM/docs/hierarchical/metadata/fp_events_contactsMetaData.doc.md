# fp_events_contactsMetaData.php

**Chemin :** `metadata/fp_events_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure événements-contacts)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `fp_events_contacts_c` qui matérialise la relation many-to-many entre les événements (`FP_events`) et les contacts (`Contacts`). Inclut le statut d'invitation et d'acceptation pour chaque contact.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['fp_events_contacts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `fp_events_contacts_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `fp_events_contactsfp_events_ida` | varchar(36) | FK vers `fp_events.id` |
| `fp_events_contactscontacts_idb` | varchar(36) | FK vers `contacts.id` |
| `invite_status` | varchar(25) | Statut d'invitation (défaut : `Not Invited`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `No Response`) |
| `email_responded` | int(2) | A répondu par email (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `FP_events`, table `fp_events`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Notes

- Généré le 2013-03-22 (sans `from_studio`).
- Champs `invite_status`, `accept_status`, `email_responded` spécifiques à la gestion des participants à un événement.
- Même pattern que `fp_events_leads_1` et `fp_events_prospects_1`.
