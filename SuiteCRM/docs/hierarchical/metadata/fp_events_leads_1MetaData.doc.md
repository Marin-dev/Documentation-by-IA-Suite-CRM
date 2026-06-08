# fp_events_leads_1MetaData.php

**Chemin :** `metadata/fp_events_leads_1MetaData.php`
**Type :** config (métadonnées de table de jointure événements-prospects)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `fp_events_leads_1_c` qui matérialise la relation many-to-many entre les événements (`FP_events`) et les prospects (`Leads`). Inclut le statut d'invitation et d'acceptation pour chaque prospect.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['fp_events_leads_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `fp_events_leads_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `fp_events_leads_1fp_events_ida` | varchar(36) | FK vers `fp_events.id` |
| `fp_events_leads_1leads_idb` | varchar(36) | FK vers `leads.id` |
| `invite_status` | varchar(25) | Statut d'invitation (défaut : `Not Invited`) |
| `accept_status` | varchar(25) | Statut d'acceptation (défaut : `No Response`) |
| `email_responded` | int(2) | A répondu par email (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `FP_events`, table `fp_events`, clé `id`
- **RHS :** module `Leads`, table `leads`, clé `id`

## Notes

- Généré par Studio le 2013-04-30. Structure identique à `fp_events_contacts` et `fp_events_prospects_1`.
