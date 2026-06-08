# CalendarEventQuery.php

**Chemin :** `include/CalendarSync/domain/services/CalendarEventQuery.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Value object representant les criteres d'une requete d'evenements calendrier : plage de dates, ID de calendrier et limite de resultats. Sert d'objet de parametre pour les methodes `getEvents()` des providers.

## Role technique

Classe immuable avec validation dans le constructeur (dates coherentes, limite positive). Expose `toArray()` pour compatibilite avec des APIs externes qui attendent un tableau d'options. Implemente `__toString()` pour les logs.

---

## Dependances cles

Aucune.

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarEventQuery` | classe value object | Criteres de requete d'evenements |
| `getStartDate(): ?DateTime` | methode | Date de debut |
| `getEndDate(): ?DateTime` | methode | Date de fin |
| `getLimit(): ?int` | methode | Limite de resultats |
| `toArray(): array` | methode | Conversion en tableau d'options |

- **Consommateurs identifies :** `AbstractCalendarProvider::getEvents()`, `CalendarEventQueryFactory`

## Relations cles

- **Appele par :** `CalendarSyncOrchestrator::prepareProvidersAndQuery()` (via `CalendarEventQueryFactory`)
- **Appelle :** rien
- **Position dans le flux global :** parametre de la requete d'evenements aux providers

---

## Points d'attention

- `calendarId` est un parametre present mais non documente comme essentiel — son usage varie selon les providers.
- Validation a la construction : si dates invalides ou limite <= 0, lance `InvalidArgumentException`.
