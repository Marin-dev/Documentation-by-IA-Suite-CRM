# Enumerator

## Rôle
Ce dossier regroupe les classes d'énumération globales de la bibliothèque SuiteCRM `lib/`. Il centralise les constantes transversales utilisées dans plusieurs sous-systèmes. Actuellement, il contient les codes d'exception standardisés utilisés dans la hiérarchie d'exceptions `lib/Exception/`.

## Contenu
| Fichier | Rôle |
|---|---|
| `ExceptionCode.php` | Constantes de codes d'exception — codes numériques ou string pour les exceptions SuiteCRM |

## Points d'entrée
- `ExceptionCode.php` — unique fichier, référencé par `lib/Exception/` et `lib/API/JsonApi/v1/Resource/`

## Dépendances clés
- **Dépend de :** rien (classe statique de constantes)
- **Utilisé par :** `lib/Exception/`, `lib/API/JsonApi/v1/Resource/SuiteBeanResource`

## Notes
- Classe de constantes pure — aucune logique métier.
- Permet d'uniformiser les codes d'exception dans tout le repo `lib/`.
