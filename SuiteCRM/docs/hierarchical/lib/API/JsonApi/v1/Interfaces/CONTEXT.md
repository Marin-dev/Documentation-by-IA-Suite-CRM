# Interfaces

## Rôle
Ce dossier définit les contrats (interfaces PHP) de la couche ressource JSON:API v1 de SuiteCRM. Il expose les interfaces pour l'identification des ressources (`JsonApiResourceIdentifier`) et pour la mise en forme des réponses (`JsonApiResponseInterface`). Ces interfaces garantissent la conformité à la spec JSON:API dans toutes les implémentations.

## Contenu
| Fichier | Rôle |
|---|---|
| `JsonApiResourceIdentifier.php` | Interface pour les identificateurs de ressource JSON:API (`id` + `type`) avec pattern immutable |
| `JsonApiResponseInterface.php` | Interface pour les réponses JSON:API — définit le contrat de sérialisation |

## Points d'entrée
- `JsonApiResourceIdentifier.php` — implémenté par `Resource/ResourceIdentifier.php`

## Dépendances clés
- **Dépend de :** rien (interfaces pures PHP)
- **Utilisé par :** `lib/API/JsonApi/v1/Resource/ResourceIdentifier.php`, classes de réponse JSON:API

## Notes
- Le pattern `with*()` suggère un usage immutable (retourne `$this`).
- Interfaces légères — aucune logique métier.
