# Step

## Rôle
Dossier parent des Steps Codeception pour les tests SuiteCRM. Contient les étapes réutilisables organisées par type de suite (Acceptance). Ces steps encapsulent les interactions UI/API de haut niveau pour les scénarios de test.

## Contenu
| Dossier | Rôle |
|---|---|
| `Acceptance/` | Steps pour les tests d'acceptation (navigation, CRUD modules, UI) |

## Points d'entrée
- `Step/Acceptance/` — steps injectés dans les acteurs d'acceptation

## Dépendances clés
- Dépend de : `_support/Page/`, acteurs Codeception
- Utilisé par : suites `tests/acceptance/`

## Notes
Structure standard Codeception — peut être étendu avec `Step/Api/` ou `Step/Unit/` si besoin.
