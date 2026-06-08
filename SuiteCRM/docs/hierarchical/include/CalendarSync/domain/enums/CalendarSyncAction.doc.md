# CalendarSyncAction.php

**Chemin :** `include/CalendarSync/domain/enums/CalendarSyncAction.php`
**Type :** PHP (enum)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Enum representant les actions possibles lors d'une synchronisation calendrier : creation, mise a jour ou suppression d'un evenement.

## Exports / Symboles principaux

| Cas | Valeur string | Signification |
|---|---|---|
| `CREATE` | `'create'` | Creer un nouvel evenement |
| `UPDATE` | `'update'` | Mettre a jour un evenement existant |
| `DELETE` | `'delete'` | Supprimer un evenement |

- **Consommateurs identifies :** `CalendarSync`, `CalendarSyncOperationDiscovery`, `CalendarSyncOrchestrator`, `CalendarSyncOperation`
