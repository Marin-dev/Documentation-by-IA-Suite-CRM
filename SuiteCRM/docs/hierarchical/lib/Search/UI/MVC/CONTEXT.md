# MVC

## Rôle
Ce dossier contient les classes de base MVC du sous-système d'interface utilisateur de recherche SuiteCRM. Il définit les classes abstraites `Controller` et `View` dont héritent tous les contrôleurs et vues de l'UI Search. Elles intègrent le moteur de templates Smarty de SuiteCRM.

## Contenu
| Fichier | Rôle |
|---|---|
| `Controller.php` | Classe abstraite de base pour les contrôleurs Search — gère l'injection de `SearchQuery` et du moteur |
| `View.php` | Classe abstraite de base pour les vues Search — encapsule le rendu Smarty |

## Points d'entrée
- `Controller.php` — étendu par `SearchFormController` et `SearchResultsController`

## Dépendances clés
- **Dépend de :** `SuiteCRM\Search\SearchQuery`, moteur Smarty SuiteCRM
- **Utilisé par :** `lib/Search/UI/SearchFormController.php`, `lib/Search/UI/SearchResultsController.php`

## Notes
- Couche d'abstraction légère permettant la séparation logique MVC dans le sous-système Search.
- Les vues Smarty utilisent les templates définis dans les modules SuiteCRM.
