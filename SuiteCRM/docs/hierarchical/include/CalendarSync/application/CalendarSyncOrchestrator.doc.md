# CalendarSyncOrchestrator.php

**Chemin :** `include/CalendarSync/application/CalendarSyncOrchestrator.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Orchestrateur central de la synchronisation calendrier. Coordonne le cycle complet : recuperation des comptes, interrogation des fournisseurs (interne et externe), decouverte des differences, execution ou soumission en file des operations de synchronisation, mise a jour des metadonnees de statut sur chaque compte.

## Role technique

Classe de service avec etat minimal (`$syncTime`). Implemente le pattern pipeline : `syncAllCalendarAccounts` -> `syncCalendarAccount` -> `prepareProvidersAndQuery` -> `fetchAndEnrichEvents` -> `discoverAndExecuteOperations` -> `syncEvent`. Chaque etape est une methode protegee testable independamment. Supporte un mode synchrone et un mode asynchrone (creation de jobs dans la file `SugarJobQueue`).

---

## Dependances cles

- **Imports principaux :**
  - `CalendarAccountRepository` — lecture des comptes valides
  - `CalendarAccountValidator` — validation d'un compte avant sync
  - `CalendarAccountEventFactory` — creation d'objets evenements
  - `CalendarEventQueryFactory` — creation des fenetres temporelles de requete
  - `CalendarProviderRegistry` — obtention des providers (interne/externe)
  - `CalendarSyncConfig` — configuration (fenetres, limites, mode async)
  - `CalendarSyncJobFactory` — soumission de jobs au scheduler
  - `CalendarSyncJobManager` — detection de jobs actifs (anti-doublon)
  - `CalendarSyncOperationDiscovery` — decouverte des operations de sync
  - `CalendarLocation`, `CalendarSyncAction` (enums) — typage des operations

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncOrchestrator` | classe service | Orchestrateur principal |
| `syncAllCalendarAccounts(bool): void` | methode | Sync tous les comptes (async ou sync) |
| `syncCalendarAccount(CalendarAccount, ?bool): bool` | methode | Sync un compte specifique |
| `syncEvent(CalendarSyncOperation, ?bool): bool` | methode | Execute ou planifie une operation unitaire |

- **Consommateurs identifies :** `CalendarSync` (facade)

## Relations cles

- **Appele par :** `CalendarSync::syncAllCalendarAccounts()`, `CalendarSync::syncAllMeetingsOfCalendarAccount()`, `CalendarSync::syncEvent()`
- **Appelle :** `CalendarProviderRegistry`, `CalendarSyncOperationDiscovery`, `CalendarSyncJobFactory`, `AbstractCalendarProvider` (create/update/deleteEvent)
- **Position dans le flux global :** couche applicative entre la facade publique et les providers/infrastructure

---

## Points d'attention

- `fetchAndEnrichEvents()` recupere les evenements dans la fenetre temporelle configuree, puis charge individuellement les evenements lies hors-fenetre (lignes 340-374). Peut generer des requetes supplementaires si de nombreux liens existent hors-fenetre.
- `discoverAndExecuteOperations()` applique `$maxOperationsPerAccount` (ligne 451) — les operations au-dela de cette limite sont silencieusement ignorees. Surveiller les comptes avec beaucoup de differences.
- `updateSyncAttemptResult()` ecrit `'sync_partial'` si le total decouvre depasse les executions reelles — signal important pour le monitoring.
- En mode async (`$async = true`), `syncCalendarAccount` cree un job de compte et retourne immediatement sans fetcher les evenements.
- `updateLastSyncAttemptDate()` est appele avant la sync, `updateLastSyncDate()` apres — les deux echouent silencieusement (warn log uniquement).
