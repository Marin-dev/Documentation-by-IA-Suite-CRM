# calendar_accounts_meetingsMetaData.php

**Chemin :** `metadata/calendar_accounts_meetingsMetaData.php`
**Type :** config (métadonnées de table de jointure calendrier)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `calendar_account_meetings` qui lie des comptes de calendrier externe (`CalendarAccount`) à des réunions (`Meetings`). Utilisée pour la synchronisation des réunions entre SuiteCRM et des services de calendrier externes (Google Calendar, etc.).

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['calendar_account_meetings']` | variable globale PHP | Définition de la table de synchronisation calendrier-réunions |

### Structure de la table `calendar_account_meetings`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `calendar_account_id` | varchar(36) | FK vers `calendar_accounts.id` |
| `meeting_id` | varchar(36) | FK vers `meetings.id` |
| `calendar_account_source` | varchar(255) | Source du compte calendrier (nullable) |
| `external_event_id` | varchar(255) | ID de l'événement dans le calendrier externe (nullable) |
| `last_sync` | datetime | Date de dernière synchronisation (nullable) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `calendar_accounts_meetingspk` | primary | `id` |
| `idx_cal_acc_mtg_cal` | index | `calendar_account_id` |
| `idx_cal_acc_mtg_mtg` | index | `meeting_id` |
| `idx_calendar_account_meeting` | unique | `calendar_account_id`, `meeting_id` |

### Relation

- **Type déclaré :** `one-to-many` (un compte calendrier peut avoir plusieurs réunions)
- **LHS :** module `CalendarAccount`, table `calendar_accounts`, clé `id`
- **RHS :** module `Meetings`, table `meetings`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module de synchronisation calendrier
- **Appelle :** rien

## Notes

- Contrairement aux autres tables de jointure, celle-ci utilise un index `unique` (pas `alternate_key`) pour la paire `(calendar_account_id, meeting_id)`.
- Champs spécifiques à la synchronisation : `external_event_id` (lien avec le service externe) et `last_sync` (contrôle de la fraîcheur des données).
- `calendar_account_source` : INCONNU — probablement le type de service (Google, Office365, etc.).
