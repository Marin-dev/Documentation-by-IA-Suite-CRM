# LegacyGoogleSyncMigrationService.php

**Chemin :** `include/CalendarSync/migrations/Services/LegacyGoogleSyncMigrationService.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de migration de l'ancien systeme Google Sync (preferences utilisateurs) vers le nouveau systeme CalendarSync (table `CalendarAccount` + `ExternalOAuthConnection`). Migre les tokens OAuth, les configurations et les donnees de synchronisation des reunions (champs `gsync_id`/`gsync_lastsync`) vers la table `calendar_account_meetings`.

## Role technique

Orchestrateur de migration : coordonne `UserMigrationService`, `ProviderMigrationService`, `MeetingMigrationService` et `SchedulerMigrationService`. La detection de doublon d'execution est geree via `MigrationRegistry`.

---

## Dependances cles

- **Imports principaux :**
  - `ValidationResult` — resultat de validation
  - `UserMigrationStatus` — statut par utilisateur
  - `LegacyUserData` — donnees legacy Google
  - `UserMigrationStatsDetail`, `MigrationStatsDetailType` — statistiques
  - `ProviderMigrationService`, `SchedulerMigrationService`, `UserMigrationService`, `MeetingMigrationService` — services specialises

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `LegacyGoogleSyncMigrationService` | classe service | Migration legacy Google Sync |

- **Consommateurs identifies :** INCONNU — probablement execute via un endpoint d'administration ou un script de migration

## Relations cles

- **Appele par :** INCONNU (script ou administration)
- **Appelle :** `UserMigrationService`, `ProviderMigrationService`, `MeetingMigrationService`, `SchedulerMigrationService`, `MigrationRegistry`
- **Position dans le flux global :** migration one-shot depuis l'ancienne synchro Google vers le nouveau systeme

---

## Points d'attention

- Migration potentiellement irreversible — doit etre jouee une seule fois grace au `MigrationRegistry`.
- Le corps complet de la classe n'a pas ete entierement lu — les methodes exactes sont INCONNU au-dela de la signature de classe et des imports.
