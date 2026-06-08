# CalendarLocation.php

**Chemin :** `include/CalendarSync/domain/enums/CalendarLocation.php`
**Type :** PHP (enum)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Enum representant les deux emplacements possibles d'un evenement dans le contexte de la synchronisation : interne (SuiteCRM) ou externe (Google Calendar, CalDAV, etc.).

## Exports / Symboles principaux

| Cas | Signification |
|---|---|
| `INTERNAL` | Calendrier SuiteCRM (table `meetings`) |
| `EXTERNAL` | Calendrier externe (fournisseur tiers) |

- Methode helper attendue : `getOpposite()` — appelee dans `CalendarSyncOperationDiscovery` (ligne 116) pour obtenir la localisation inverse.
- **Consommateurs identifies :** `CalendarSyncOperationDiscovery`, `CalendarSyncOrchestrator`, `CalendarSync`, `CalendarSyncOperation`
