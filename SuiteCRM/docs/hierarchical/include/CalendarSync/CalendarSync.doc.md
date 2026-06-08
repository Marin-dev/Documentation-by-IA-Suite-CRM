# CalendarSync.php

**Chemin :** `include/CalendarSync/CalendarSync.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Facade principale du module de synchronisation de calendriers. Sert de point d'entree unique pour toutes les operations de synchronisation : synchronisation globale de tous les comptes, synchronisation d'un compte specifique, synchronisation unitaire d'une reunion, gestion de la configuration et des fournisseurs de calendriers. Exposes en tant que singleton au reste de l'application.

## Role technique

Classe singleton qui implemente `CalendarSyncInterface`. Delegue l'orchestration a `CalendarSyncOrchestrator`, la decouverte d'operations a `CalendarSyncOperationDiscovery`, la gestion des jobs scheduler a `CalendarSyncJobFactory` / `CalendarSyncJobCleaner`, et la persistance des comptes a `CalendarAccountRepository`. Pattern Facade — aucune logique metier directe, uniquement coordination des couches internes.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarAccountValidator` — validation des comptes calendrier
  - `CalendarAccountRepository` — requetes BDD sur les comptes
  - `CalendarSyncJobManager` — verification des jobs actifs
  - `CalendarSyncOperationDiscovery` — creation des operations de sync
  - `CalendarSyncOrchestrator` — orchestration de la synchronisation
  - `CalendarSyncConfig` — configuration (fenetres, mode async, etc.)
  - `CalendarSyncJobCleaner` — annulation des jobs obsoletes
  - `CalendarSyncJobFactory` — creation des jobs dans la file
  - `CalendarProviderRegistry` — registre des fournisseurs externes
  - `CalendarSyncOperationSerializer` — serialisation/deserialisation des operations

- **Variables d'environnement utilisees :** aucune directe (configuration via `SugarConfig`/table `config`)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSync` | classe singleton | Facade principale |
| `getInstance()` | methode statique | Retourne l'instance unique |
| `syncAllCalendarAccounts(bool)` | methode | Synchronise tous les comptes |
| `syncAllMeetingsOfCalendarAccount(string)` | methode | Sync un compte specifique |
| `syncMeeting(Meeting)` | methode | Sync une reunion (hook logique) |
| `syncEvent(string)` | methode | Execute un job de sync depuis le scheduler |
| `saveConfig(array)` | methode | Sauvegarde la configuration |
| `getConfig()` | methode | Lit la configuration |
| `getFieldsToHide(string)` | methode | Champs a masquer selon la methode d'auth |
| `findDuplicateCalendarAccount(string, string)` | methode | Verifie les doublons d'ID calendrier |

- **Consommateurs identifies dans le repo :** INCONNU (point d'entree externe, chercher via `CalendarSync::getInstance()`)

## Relations cles

- **Appele par :** modules/scheduler, logic hooks sur Meeting, vues d'administration du calendrier
- **Appelle :** `CalendarSyncOrchestrator`, `CalendarAccountRepository`, `CalendarProviderRegistry`, `CalendarSyncConfig`
- **Position dans le flux global :** point d'entree de toute la synchronisation calendrier — premier appel du scheduler ou des hooks

---

## Points d'attention

- Singleton avec `__clone()` prive et `__wakeup()` lancant une exception : non serialisable intentionnellement.
- `syncMeeting()` verifie `$this->config->enableCalendarSyncLogicHooks()` — les hooks sont desactives par defaut (ligne 147). Si la config ne l'active pas, aucune sync ne se declenche depuis les logic hooks.
- La detection de l'action CREATE/UPDATE/DELETE repose sur `$bean->fetched_row` et `$bean->deleted` (lignes 150-156) — coherence avec le cycle de vie des beans Sugar.
- `getFieldsToHide()` : la logique masque tous les champs d'auth sauf ceux de la methode active — attention si de nouvelles methodes sont ajoutees sans MAJ de `$fieldMappings`.
