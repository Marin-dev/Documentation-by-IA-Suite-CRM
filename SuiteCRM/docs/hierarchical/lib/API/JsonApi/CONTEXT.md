# JsonApi

## Rôle
Ce dossier est le conteneur de la couche JSON:API de SuiteCRM. Il héberge la version 1 de l'implémentation JSON:API (sous-dossier `v1/`) qui fournit tous les composants nécessaires à la conformité JSON:API 1.0 : ressources, filtres, relations, sérialisation et validation. Cette couche est la bibliothèque de base utilisée par tous les contrôleurs de l'API v8.

## Contenu
| Dossier | Rôle |
|---|---|
| `v1/` | Implémentation complète JSON:API v1 : ressources, filtres, repositories, énumérations |

## Points d'entrée
- `v1/` — dossier unique contenant toute l'implémentation

## Dépendances clés
- **Dépend de :** container DI, `\BeanFactory`, `DBManager`
- **Utilisé par :** `lib/API/v8/Controller/`, `lib/API/v8/Library/`

## Notes
- Ce dossier n'est qu'un conteneur de versioning — toute la logique est dans `v1/`.
- Si une v2 de l'API JSON:API devait être créée, elle serait ajoutée en parallèle de `v1/`.
