# CalendarSyncInterface.php

**Chemin :** `include/CalendarSync/CalendarSyncInterface.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Contrat (interface PHP) definissant toutes les operations publiques du module de synchronisation de calendriers. Garantit la separation entre l'API publique et l'implementation concrete (`CalendarSync`). Permet de substituer l'implementation pour les tests ou des evolutions futures.

## Role technique

Interface PHP pure, sans logique. Documente les signatures de methodes et leurs comportements attendus (exceptions possibles, types de retour). Regroupee en sections fonctionnelles : execution de jobs, gestion des fournisseurs, utilitaires UI, gestion de configuration, planification, gestion des comptes, singleton.

---

## Dependances cles

- **Imports principaux :** aucun (interface pure)
- **Types references :** `Meeting`, `CalendarAccount`, `CalendarConnectionTestResult`, `Scheduler`

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncInterface` | interface | Contrat de la facade |
| `syncAllCalendarAccounts(bool): bool` | signature | Sync tous les comptes |
| `syncAllMeetingsOfCalendarAccount(string): void` | signature | Sync meetings d'un compte |
| `syncMeeting(Meeting): void` | signature | Sync unitaire d'une reunion |
| `syncEvent(string): bool` | signature | Execute un job serialise |
| `getProviderAuthMethodWithValidation(string): string` | signature | Auth method du fournisseur |
| `testProviderConnectionWithValidation(CalendarAccount): CalendarConnectionTestResult` | signature | Test de connexion |
| `getFieldsToHide(string): array` | signature | Champs a masquer UI |
| `saveConfig(array): bool` | signature | Sauvegarde config |
| `getConfig(): array` | signature | Lecture config |
| `getConflictResolutionCases(): array` | signature | Cas de resolution de conflits |
| `getScheduler(): ?Scheduler` | signature | Instance du scheduler |
| `getActiveCalendarAccountsForUser(string): array` | signature | Comptes actifs d'un user |
| `getInstance(): CalendarSync` | signature statique | Retourne le singleton |

- **Consommateurs identifies :** `CalendarSync` (implementeur direct)

## Relations cles

- **Appele par :** tout code qui type-hinte `CalendarSyncInterface`
- **Appelle :** rien (interface)
- **Position dans le flux global :** definition du contrat public du module CalendarSync

---

## Points d'attention

- `getInstance()` retourne `CalendarSync` concret (pas `CalendarSyncInterface`) — couplage fort sur le type de retour, empechant une substitution totale sans casser la signature.
