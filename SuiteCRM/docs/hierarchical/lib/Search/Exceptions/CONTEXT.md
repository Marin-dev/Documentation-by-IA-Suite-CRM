# Exceptions

## Rôle
Ce dossier regroupe les exceptions métier du sous-système de recherche SuiteCRM. Chaque exception représente un cas d'erreur spécifique au domaine de la recherche, permettant une gestion fine des erreurs dans les moteurs, l'indexation et l'interface utilisateur.

## Contenu
| Fichier | Rôle |
|---|---|
| `SearchException.php` | Exception de base du sous-système de recherche |
| `SearchEngineNotFoundException.php` | Levée quand le moteur de recherche demandé n'est pas disponible |
| `SearchInvalidRequestException.php` | Levée pour les requêtes de recherche invalides (query vide, etc.) |
| `SearchUserFriendlyException.php` | Exception dont le message peut être affiché à l'utilisateur final |

## Points d'entrée
- `SearchException.php` — classe de base de la hiérarchie d'exceptions Search

## Dépendances clés
- **Dépend de :** `SuiteCRM\Exception\Exception` (classe parente)
- **Utilisé par :** `lib/Search/SearchEngine.php`, `lib/Search/SearchWrapper.php`, moteurs de recherche (AOD, ES, Basic, SQL)

## Notes
- `SearchUserFriendlyException` est utilisée pour les messages d'erreur affichés dans l'UI Search.
- `SearchInvalidRequestException` est levée par `SearchEngine::validateQuery()`.
