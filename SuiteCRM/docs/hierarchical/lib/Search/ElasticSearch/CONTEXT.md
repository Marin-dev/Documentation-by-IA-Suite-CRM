# ElasticSearch

## Rôle
Ce dossier contient le moteur de recherche ElasticSearch pour SuiteCRM. Il implémente la recherche plein texte haute performance via le client officiel ElasticSearch PHP. Il gère l'indexation (création et mise à jour des index), la recherche, les hooks SuiteCRM pour la mise à jour automatique des index lors des modifications de beans, et les commandes CLI de gestion.

## Contenu
| Fichier | Rôle |
|---|---|
| `ElasticSearchEngine.php` | Moteur de recherche principal — exécute les requêtes ElasticSearch et retourne `SearchResults` |
| `ElasticSearchIndexer.php` | Indexeur — gère la création, mise à jour et suppression des documents dans les index ES |
| `ElasticSearchClientBuilder.php` | Factory du client ElasticSearch — instancie et configure `\Elasticsearch\Client` |
| `ElasticSearchHooks.php` | Hooks SuiteCRM — maintient les index à jour lors des sauvegardes/suppressions de beans |
| `ElasticSearchModuleDataPuller.php` | Utilitaire d'extraction des données de modules pour l'indexation initiale |

## Points d'entrée
- `ElasticSearchEngine.php` — point d'entrée pour les recherches
- `ElasticSearchIndexer.php` — point d'entrée pour l'indexation

## Dépendances clés
- **Dépend de :** `lib/Search/SearchEngine.php`, `lib/Search/Index/AbstractIndexer.php`, client `elasticsearch/elasticsearch` (Composer), `SearchWrapper`, `SearchConfigurator`
- **Utilisé par :** `lib/Search/SearchWrapper.php`, hooks SuiteCRM, `lib/Robo/Plugin/Commands/ElasticSearchCommands.php`

## Notes
- C'est le moteur de recherche recommandé pour les déploiements en production.
- `ElasticSearchHooks` s'enregistre automatiquement via `SearchWrapper`.
- `ElasticSearchClientBuilder` lit la configuration depuis `$sugar_config['search']['ElasticSearch']`.
