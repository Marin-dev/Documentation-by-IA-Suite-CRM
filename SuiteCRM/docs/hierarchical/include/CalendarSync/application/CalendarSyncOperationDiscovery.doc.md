# CalendarSyncOperationDiscovery.php

**Chemin :** `include/CalendarSync/application/CalendarSyncOperationDiscovery.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service applicatif qui compare les evenements d'un calendrier source avec ceux d'un calendrier cible et determine la liste des operations de synchronisation necessaires (CREATE, UPDATE, DELETE). Constitue le coeur de la logique de "diff" entre deux ensembles d'evenements.

## Role technique

Algorithme de reconciliation bidirectionnel : construit des index de recherche (`targetEventsLookup`, `reverseLinkedLookup`) pour un matching O(n). Pour chaque evenement source, determine si une creation, mise a jour ou suppression est necessaire en tenant compte de la strategie de resolution de conflits configuree. Delegue la resolution de conflits a `CalendarEventConflictResolver`. Methode publique `createSyncOperation()` utilitaire pour creer un objet operation typee.

---

## Dependances cles

- **Imports principaux :**
  - `CalendarSyncOperation` — objet operation resultant
  - `CalendarEventConflictResolver` — strategie de resolution de conflit
  - `CalendarSyncConfig` — lecture de la strategie configuree
  - `ConflictResolution` (enum) — cas de resolution
  - `CalendarSyncAction` (enum) — CREATE / UPDATE / DELETE
  - `CalendarLocation` (enum) — INTERNAL / EXTERNAL

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncOperationDiscovery` | classe | Service de decouverte |
| `discoverSyncOperations(array, array, CalendarLocation, bool, string, string, AbstractCalendarProvider): array` | methode | Produit la liste des operations |
| `createSyncOperation(string, string, CalendarSyncAction, CalendarLocation, ?string, ?CalendarAccountEvent): CalendarSyncOperation` | methode | Cree une operation unitaire |

- **Consommateurs identifies :** `CalendarSyncOrchestrator`

## Relations cles

- **Appele par :** `CalendarSyncOrchestrator::discoverAndExecuteOperations()`
- **Appelle :** `CalendarEventConflictResolver::determineWinningEvent()`, `CalendarSyncConfig::getConflictResolution()`
- **Position dans le flux global :** etape de "diffing" entre calendrier interne et externe, avant execution des operations

---

## Points d'attention

- Le parametre `$allowDeletion` controle si les suppressions sont autorisees cote source. A `false`, les evenements orphelins ne sont pas supprimes (comportement conservateur).
- L'index `$reverseLinkedLookup` permet de retrouver un evenement cible dont le `linked_event_id` pointe vers la source, gerant les cas de liaison inverse.
- La strategie de conflit (`ConflictResolution::tryFrom()`) se replie sur `TIMESTAMP` si la valeur configuree est invalide (ligne 102).
- Le parametre `$targetProvider` est accepte mais non utilise dans la methode — potentielle extension future ou dette technique.
