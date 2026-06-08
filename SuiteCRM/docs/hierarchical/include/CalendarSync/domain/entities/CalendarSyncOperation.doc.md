# CalendarSyncOperation.php

**Chemin :** `include/CalendarSync/domain/entities/CalendarSyncOperation.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Value object representant une operation de synchronisation calendrier a executer : quelle action (CREATE/UPDATE/DELETE), sur quel evenement (`subject_id`), dans quel calendrier (`location`), pour quel compte et quel utilisateur, avec optionnellement l'evenement source comme payload.

## Role technique

Classe immuable (pas de setters). Consommee par `CalendarSyncOrchestrator` pour executer l'operation et par `CalendarSyncOperationSerializer` pour la serialisation en vue d'un job asynchrone. Creee par `CalendarSyncOperationDiscovery::createSyncOperation()`.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarLocation` (enum) — INTERNAL / EXTERNAL
  - `CalendarSyncAction` (enum) — CREATE / UPDATE / DELETE

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncOperation` | classe value object | Commande de synchronisation |
| `getUserId(): string` | methode | ID utilisateur |
| `getCalendarAccountId(): string` | methode | ID du compte calendrier |
| `getSubjectId(): string` | methode | ID de l'evenement cible |
| `getLocation(): CalendarLocation` | methode | Calendrier cible (INTERNAL/EXTERNAL) |
| `getAction(): CalendarSyncAction` | methode | Action a effectuer |
| `getPayload(): ?CalendarAccountEvent` | methode | Evenement source (null pour DELETE) |

- **Consommateurs identifies :** `CalendarSyncOrchestrator`, `CalendarSyncOperationSerializer`, `CalendarSyncJobManager`, `CalendarSyncJobCleaner`

## Relations cles

- **Appele par :** `CalendarSyncOperationDiscovery` (creation), `CalendarSyncOrchestrator` (execution)
- **Appelle :** rien
- **Position dans le flux global :** commande intermediaire entre le diff et l'execution

---

## Points d'attention

- Pour une operation CREATE, `subject_id` est vide (`''`) — l'ID sera genere par le provider lors de la creation reelle.
- Pour DELETE, `payload` est `null` — l'orchestrateur ne passe que l'ID de l'evenement a supprimer.
