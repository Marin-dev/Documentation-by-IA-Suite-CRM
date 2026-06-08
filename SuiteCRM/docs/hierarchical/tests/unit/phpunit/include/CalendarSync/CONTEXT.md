# CalendarSync

## Rôle
Tests unitaires PHPUnit pour le module CalendarSync. Vérifie les composants de synchronisation de calendrier (orchestrateur, discovery, providers) en isolation via mocks.

## Contenu
| Fichier | Rôle |
|---|---|
| `CalendarSyncTest.php` | Tests unitaires du module CalendarSync (comportement core) |

## Points d'entrée
- `CalendarSyncTest` — lancé via PHPUnit

## Dépendances clés
- Dépend de : `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase`, `include/CalendarSync/`
- Utilisé par : pipeline CI/CD (suite unit)

## Notes
Correspond à `include/CalendarSync/` — tests en isolation (sans BDD ni providers réels).
