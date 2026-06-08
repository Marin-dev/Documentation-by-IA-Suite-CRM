# ConflictResolution.php

**Chemin :** `include/CalendarSync/domain/enums/ConflictResolution.php`
**Type :** PHP (enum)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Enum representant les strategies de resolution de conflits lors d'une synchronisation calendrier bidirectionnelle quand les deux versions (interne et externe) ont ete modifiees simultanement.

## Exports / Symboles principaux

| Cas | Valeur string | Signification |
|---|---|---|
| `TIMESTAMP` | `'timestamp'` | L'evenement le plus recemment modifie gagne |
| `EXTERNAL_BASED` | `'external_based'` | L'evenement externe prend priorite |
| `INTERNAL_BASED` | `'internal_based'` | L'evenement interne SuiteCRM prend priorite |

- **Consommateurs identifies :** `CalendarEventConflictResolver`, `CalendarSyncConfig`, `CalendarSyncOperationDiscovery`
