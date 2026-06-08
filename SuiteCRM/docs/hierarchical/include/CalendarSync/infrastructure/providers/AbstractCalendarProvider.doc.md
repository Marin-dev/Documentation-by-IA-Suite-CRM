# AbstractCalendarProvider.php

**Chemin :** `include/CalendarSync/infrastructure/providers/AbstractCalendarProvider.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe abstraite de base pour tous les fournisseurs de calendrier (Google, CalDAV, JSON, interne SuiteCRM). Definit le contrat et les methodes template pour les operations CRUD sur les evenements calendrier, garantissant une gestion coherente du timestamp de synchronisation.

## Role technique

Pattern Template Method : les methodes publiques `createEventFromSource()`, `updateEventFromSource()`, `updateSourceEvent()`, `deleteEvent()` sont `final` et appellent les methodes abstraites `doCreateEvent()`, `doUpdateEvent()`, `doDeleteEvent()` implementees par les sous-classes. Assure que `setLastSync()` est toujours appele avant chaque operation. `generateEventId()` produit un ID unique pour les creations.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarAccountEvent` — entite evenement
  - `CalendarEventQuery` — criteres de requete d'evenements
  - `CalendarAccountEventFactory` — creation d'evenements cibles depuis une source
  - `CalendarConnectionTestResult` — resultat du test de connexion
  - `CalendarSyncConfig` — acces au nom du calendrier externe
  - `CalendarAccountRelationshipManager` — gestion des relations (injected)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AbstractCalendarProvider` | classe abstraite | Base des providers |
| `setConnection(CalendarAccount): void` | methode | Configure le compte calendrier |
| `testCalendarConnection(): CalendarConnectionTestResult` | methode abstraite | Test de connexion |
| `getEvents(CalendarEventQuery): array` | methode abstraite | Liste des evenements |
| `getEvent(string): ?CalendarAccountEvent` | methode abstraite | Evenement par ID |
| `createEventFromSource(CalendarAccountEvent, DateTime): string` | methode finale | Cree un evenement depuis la source |
| `updateEventFromSource(string, CalendarAccountEvent, DateTime): void` | methode finale | Met a jour depuis la source |
| `updateSourceEvent(string, CalendarAccountEvent, DateTime): void` | methode finale | Met a jour la source apres creation |
| `deleteEvent(string): void` | methode finale | Supprime un evenement |
| `doCreateEvent/doUpdateEvent/doDeleteEvent()` | abstraites | Implementation provider-specifique |

- **Consommateurs identifies :** `CalendarSyncOrchestrator`, `CalendarProviderInstanceFactory`

## Relations cles

- **Appele par :** `CalendarSyncOrchestrator::syncEvent()`
- **Appelle :** sous-classes (CalDAVProvider, GoogleCalendarProvider, JsonFileCalendarProvider, SuiteCRMInternalCalendarProvider)
- **Position dans le flux global :** couche infrastructure entre l'orchestrateur et les APIs externes

---

## Points d'attention

- `generateEventId()` utilise `uniqid()` + `date()` — potentiellement non-unique sous haute concurrence. A verifier selon l'usage.
- `$connection` est `null` jusqu'a `setConnection()` — toute sous-classe qui accede a `$this->connection` sans appel prealable a `setConnection()` risque un NPE.
- Les methodes `doCreate/doUpdate/doDelete` sont `abstract protected` — les sous-classes ne peuvent pas les exposer directement, seul le template public est expose.
