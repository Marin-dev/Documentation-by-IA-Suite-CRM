# CalendarAccountRepository.php

**Chemin :** `include/CalendarSync/domain/services/CalendarAccountRepository.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Repository d'acces aux donnees pour les comptes calendrier (`CalendarAccount`). Fournit des methodes filtrees pour recuperer les comptes valides (non supprimes, avec utilisateur assigne), les comptes personnels d'un utilisateur, et la recherche par ID de calendrier externe.

## Role technique

Classe de service utilisant directement `BeanFactory` et des requetes SQL natives (via `db->query()`) pour optimiser les lectures en batch (eviter le probleme N+1). La methode protegee `getCalendarAccountsForUser()` est la base de toutes les requetes, avec parametrage flexible (userId, type, validatedOnly, limit, includeDeleted). Les resultats sont triees par date de tentative de sync (les comptes les plus anciens en premier).

---

## Dependances cles

- **Imports principaux :**
  - `BeanFactory` (SuiteCRM core) — creation et chargement des beans `CalendarAccount`
  - `DBManagerFactory` (implicite) — acces BDD via `$calendarAccount->db`

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarAccountRepository` | classe repository | Acces aux donnees comptes calendrier |
| `getValidatedAccountsBatch(?int): array` | methode | Tous comptes valides (avec limite) |
| `hasPersonalCalendarAccount(string): bool` | methode | Test existence compte personnel |
| `getPersonalCalendarAccounts(string): array` | methode | Comptes personnels d'un user |
| `getValidatedPersonalCalendarAccountForUser(string): ?CalendarAccount` | methode | Compte personnel valide (1er) |
| `getAllValidatedCalendarAccountsForUser(string): array` | methode | Tous comptes valides d'un user |
| `findByExternalCalendarId(string, ?string): ?CalendarAccount` | methode | Recherche par ID calendrier externe |

- **Consommateurs identifies :** `CalendarSync` (facade), `CalendarSyncOrchestrator`

## Relations cles

- **Appele par :** `CalendarSync::getActiveCalendarAccountForUser()`, `CalendarSyncOrchestrator::getCalendarAccounts()`
- **Appelle :** `BeanFactory::newBean('CalendarAccount')`, `BeanFactory::getBean('CalendarAccount', id)`
- **Position dans le flux global :** couche de persistance en lecture pour les comptes calendrier

---

## Points d'attention

- La requete SQL de `getCalendarAccountsForUser()` selectionne uniquement les IDs, puis charge chaque bean via `BeanFactory::getBean()` (ligne 218) — reste N+1 mais limite par le parametre `$limit`.
- L'ordre SQL `last_sync_attempt_date IS NOT NULL, last_sync_attempt_date ASC` priorise les comptes jamais synchronises en dernier (IS NULL = 0 = faux = retourne 0 donc derniers). Verification necessaire du comportement exact selon le SGBD.
- Usage interne uniquement (`@internal`) — tout code externe doit passer par la facade `CalendarSync`.
