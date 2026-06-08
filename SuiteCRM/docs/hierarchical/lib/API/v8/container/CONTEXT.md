# container

## Rôle
Ce dossier contient les fichiers de configuration du conteneur DI (injection de dépendances) de l'API v8 de SuiteCRM. Chaque fichier déclare la factory d'un service ou contrôleur spécifique : instanciation, injection des dépendances, et enregistrement sous une clé dans le container Slim. Il est l'équivalent dans la couche `lib/` de ce que `Api/V8/Config/services/` fait dans la couche applicative.

## Contenu
| Fichier | Rôle |
|---|---|
| `ApiController.php` | Factory de `ApiController` — injecte le logger |
| `ModuleController.php` | Factory de `ModuleController` — injecte services et libraries |
| `OAuth2Controller.php` | Factory de `OAuth2Controller` — injecte les serveurs OAuth2 |
| `SchemaController.php` | Factory de `SchemaController` |
| `AuthorizationServer.php` | Factory du serveur d'autorisation OAuth2 |
| `ResourceServer.php` | Factory du serveur de ressources OAuth2 (validation tokens) |
| `AuthenticationController.php` | Factory du contrôleur d'authentification |
| `ConfigurationManager.php` | Factory du gestionnaire de configuration SuiteCRM |
| `DatabaseManager.php` | Factory du gestionnaire de base de données |
| `DateTimeConverter.php` | Factory du convertisseur datetime |
| `CurrentLanguage.php` | Factory de la langue courante de l'utilisateur |
| `ApplicationLanguage.php` | Factory des labels de l'application |
| `ModuleLanguage.php` | Factory des labels de module |

## Points d'entrée
- `ApiController.php` — base de tous les contrôleurs
- `AuthorizationServer.php` / `ResourceServer.php` — configuration sécurité OAuth2

## Dépendances clés
- **Dépend de :** `lib/API/v8/Controller/`, `lib/API/OAuth2/Middleware/`, `lib/Utility/`, `Psr\Log\LoggerInterface`
- **Utilisé par :** bootstrapper de l'API v8 (`lib/API/core/containers.php`)

## Notes
- Chaque fichier retourne un tableau `[nom_service => closure]`.
- Ces factories constituent le graphe complet de dépendances de l'API v8.
