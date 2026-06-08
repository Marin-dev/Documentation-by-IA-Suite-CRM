# UI

## Rôle
Ce dossier contient la couche d'interface utilisateur du sous-système de recherche SuiteCRM. Il implémente le pattern MVC pour l'affichage du formulaire de recherche et des résultats. `SearchFormController`/`View` gèrent le formulaire ; `SearchResultsController`/`View` gèrent l'affichage des résultats ; `SearchThrowableHandler` gère l'affichage des erreurs côté utilisateur.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `MVC/` | Classes abstraites de base `Controller` et `View` pour le sous-système Search |
| `SearchFormController.php` | Contrôleur du formulaire de recherche — assigne les variables Smarty |
| `SearchFormView.php` | Vue du formulaire de recherche — rendu Smarty |
| `SearchResultsController.php` | Contrôleur des résultats de recherche |
| `SearchResultsView.php` | Vue des résultats de recherche — rendu Smarty |
| `SearchThrowableHandler.php` | Gestionnaire d'erreurs UI — affiche les exceptions à l'utilisateur |

## Points d'entrée
- `SearchFormController.php` — appelé par `SearchEngine::displayForm()`
- `SearchResultsController.php` — appelé par `SearchEngine::displayResults()`

## Dépendances clés
- **Dépend de :** `lib/Search/MVC/` (classes abstraites), `lib/Search/SearchQuery`, `lib/Search/SearchWrapper`, moteur Smarty SuiteCRM
- **Utilisé par :** `lib/Search/SearchEngine.php` (méthodes `displayForm()` et `displayResults()`)

## Notes
- La chaîne de recherche est encodée HTML via `htmlspecialchars()` avant assignation Smarty.
- `SearchThrowableHandler` est conçu pour afficher des messages d'erreur compréhensibles aux utilisateurs (pas les traces techniques).
