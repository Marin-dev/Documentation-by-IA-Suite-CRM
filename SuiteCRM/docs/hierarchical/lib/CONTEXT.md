# lib

## Rôle
Ce dossier est la bibliothèque technique centrale de SuiteCRM. Il regroupe tous les composants réutilisables et sous-systèmes techniques : API REST (JSON:API + OAuth2), recherche (ElasticSearch/AOD/SQL/Basic), génération PDF (TCPDF/mPDF), utilitaires transversaux, anti-malware, logging, gestion des erreurs et automatisation CLI (Robo). Ces composants sont conçus pour être indépendants du cœur SuiteCRM tout en s'intégrant avec lui.

## Contenu
| Dossier | Rôle |
|---|---|
| `API/` | API REST SuiteCRM v8 — JSON:API, OAuth2, contrôleurs, routes, containers DI |
| `Search/` | Sous-système de recherche — moteurs multiples (ES, AOD, SQL, Basic), indexation, UI MVC |
| `PDF/` | Génération PDF — factory + moteurs TCPDF (modern) et mPDF legacy |
| `Robo/` | Automatisation CLI — commandes Robo pour API, tests, build, cache, ES, upgrade |
| `Utility/` | Utilitaires transversaux — configuration, logging PSR-3, sérialisation beans, anti-malware |
| `Log/` | Handlers Monolog — sortie SugarLog et CLI colorée (ANSI) |
| `Exception/` | Hiérarchie d'exceptions métier communes |
| `Interfaces/` | Interfaces transversales (anti-malware scanner) |
| `Enumerator/` | Constantes globales (codes d'exception) |

## Points d'entrée
- `API/public/index.php` — entrypoint HTTP de l'ancienne API REST (déprécié, migrer vers `Api/V8/`)
- `API/OAuth2/Middleware/AuthorizationServer.php` — émission des tokens OAuth2
- `Search/SearchWrapper.php` — façade centrale de recherche
- `PDF/PDFWrapper.php` — factory de génération PDF
- `Robo/Plugin/Commands/ApiCommands.php` — configuration CLI de l'API V8

## Dépendances clés
- **Dépend de :** `league/oauth2-server`, `slim/slim`, `elasticsearch/elasticsearch`, `tcpdf`, `robo/robo`, `Monolog`, `Psr\Log`, `JsonSchema\Validator`
- **Utilisé par :** `Api/V8/` (couche applicative), serveur web (requêtes `/api/`), CLI Robo, modules SuiteCRM (PDF, Search)

## Notes
- `lib/API/` est en cours de migration vers `Api/V8/` — `lib/API/core/app.php` est déprécié.
- ElasticSearch est le moteur de recherche recommandé pour la production.
- Les clés RSA OAuth2 dans `lib/API/OAuth2/` doivent être protégées contre l'accès web public.
- `ApiController::VERSION_STABILITY = 'ALPHA'` — l'API v8 est toujours en alpha.
- Dette technique documentée : `FilterValidator.isValid()` retourne toujours `true`; bug ligne 409 de `SuiteBeanResource`; bug ligne 352 de `ModulesLib`.
