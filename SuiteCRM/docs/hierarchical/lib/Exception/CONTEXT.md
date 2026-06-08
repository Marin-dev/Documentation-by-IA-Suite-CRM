# Exception

## Rôle
Ce dossier contient la hiérarchie d'exceptions métier de la bibliothèque `lib/` de SuiteCRM. Ces exceptions couvrent les cas d'erreur communs à plusieurs sous-systèmes : accès refusé, argument invalide, malware détecté, ressource introuvable, opération non autorisée. Elles sont conçues pour être rattrapées à différents niveaux de l'application.

## Contenu
| Fichier | Rôle |
|---|---|
| `Exception.php` | Exception de base — classe parente de toutes les exceptions `lib/` |
| `AccessDeniedException.php` | Accès refusé (autorisation) |
| `InvalidArgumentException.php` | Argument invalide passé à une méthode |
| `MalwareFoundException.php` | Malware détecté lors d'un scan de fichier |
| `NotAllowedException.php` | Opération non autorisée dans le contexte courant |
| `NotFoundException.php` | Ressource introuvable |

## Points d'entrée
- `Exception.php` — classe de base de toute la hiérarchie

## Dépendances clés
- **Dépend de :** `\RuntimeException` ou `\Exception` PHP natif
- **Utilisé par :** `lib/Utility/AntiMalware/`, `lib/API/JsonApi/v1/`, `lib/API/OAuth2/`, `lib/Search/`

## Notes
- `MalwareFoundException` doit être interceptée dans les gestionnaires d'upload pour afficher un message approprié à l'utilisateur.
- Les codes d'exception standardisés sont dans `lib/Enumerator/ExceptionCode.php`.
