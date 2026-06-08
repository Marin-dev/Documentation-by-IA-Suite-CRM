# callable

## Rôle
Ce dossier contient les callables (closures/fonctions invocables) de configuration de l'API v8. Ces callables sont enregistrées dans le container Slim et utilisées pour initialiser des services spécifiques, notamment le flux OAuth2. Ils font le lien entre la configuration et les instances de services.

## Contenu
| Fichier | Rôle |
|---|---|
| `oauth2.php` | Callable de configuration du flux OAuth2 — instancie et configure les grant types du serveur d'autorisation |

## Points d'entrée
- `oauth2.php` — exécuté lors de l'initialisation du container DI pour configurer OAuth2

## Dépendances clés
- **Dépend de :** `lib/API/OAuth2/Middleware/AuthorizationServer`, repositories OAuth2, clés RSA
- **Utilisé par :** `lib/API/v8/container/` (chargement du container DI)

## Notes
- Ce dossier est analogue au pattern "factory callable" pour les services complexes qui nécessitent plusieurs étapes de configuration.
