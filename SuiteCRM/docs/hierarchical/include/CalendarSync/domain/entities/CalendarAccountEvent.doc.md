# CalendarAccountEvent.php

**Chemin :** `include/CalendarSync/domain/entities/CalendarAccountEvent.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Entite de domaine representant un evenement calendrier dans le contexte de la synchronisation. Modelise un evenement qu'il soit interne (SuiteCRM Meeting) ou externe (Google Calendar, CalDAV). Sert de representation unifiee pour le moteur de diff et d'operations.

## Role technique

Classe PHP avec proprietes initializees dans le constructeur. Maintient un checksum MD5 du contenu (`$content_checksum`) calcule a la creation pour des comparaisons rapides. Les dates sont normalises via `DateTimeHelper`. Accepte des dates au format `DateTime` ou `string` (ISO 8601). Expose les donnees via getters, avec possibilite de modifier `linked_event_id` et `last_sync` (mutable sur ces deux champs uniquement).

---

## Dependances cles

- **Imports principaux :**
  - `CalendarEventType` (enum) — MEETING ou autre type
  - `DateTimeHelper` — normalisation et parsing des dates

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarAccountEvent` | classe entite | Evenement calendrier unifie |
| `DATE_FORMAT` | constante | Format ISO 8601 (ATOM) |
| `getId(): string` | methode | ID de l'evenement |
| `getName() / getTitle(): string` | methode | Titre de l'evenement |
| `getLinkedEventId(): ?string` | methode | ID de l'evenement lie dans l'autre calendrier |
| `setLinkedEventId(?string): self` | methode | Mise a jour du lien |
| `getContentChecksum(): string` | methode | Checksum MD5 du contenu |
| `isExternal(): bool` | methode | True si evenement externe |
| `getDateStart/End/Modified/LastSync(): DateTime` | methodes | Dates typees |

- **Consommateurs identifies :** `CalendarSyncOperationDiscovery`, `CalendarEventConflictResolver`, `CalendarSyncOrchestrator`, `AbstractCalendarProvider`, `CalendarAccountEventFactory`

## Relations cles

- **Appele par :** toutes les couches de traitement CalendarSync
- **Appelle :** `DateTimeHelper`, `CalendarEventType`
- **Position dans le flux global :** DTO central entre providers, discovery et orchestrateur

---

## Points d'attention

- Le checksum est calcule a la construction et ne se met pas a jour si `name`, `description`, `location`, ou les dates sont modifies apres coup. Seuls `linked_event_id` et `last_sync` sont mutables — le checksum reste coherent pour la comparaison de contenu.
- `date_end` peut etre `null` (evenement sans fin), ce qui est gere dans `getChecksumArray()` via `?->format(...) ?? '0'`.
- `last_sync` initialisee a `new DateTime('-1 year')` si null — assure que tout evenement sans historique est considere comme non-synchronise.
