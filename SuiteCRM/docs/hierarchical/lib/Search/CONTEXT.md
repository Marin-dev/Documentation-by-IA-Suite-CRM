# Search

## Rôle
Ce dossier implémente le sous-système de recherche complet de SuiteCRM. Il offre une architecture extensible avec plusieurs moteurs interchangeables (ElasticSearch, AOD/Lucene, SQL, Basic), une infrastructure d'indexation, une couche UI MVC et une gestion unifiée des erreurs. `SearchWrapper` est le point d'accès central qui dispatche vers le moteur configuré.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `SearchWrapper.php` | Façade principale — dispatche vers le moteur configuré, gère les modules et utilisateurs |
| `SearchEngine.php` | Classe abstraite — contrat de tous les moteurs + méthodes d'affichage |
| `SearchQuery.php` | DTO de requête de recherche (termes, modules, pagination) |
| `SearchResults.php` | DTO des résultats de recherche |
| `SearchModules.php` | Gestion de la liste des modules indexables |
| `SearchConfigurator.php` | Configuration du sous-système de recherche |
| `AOD/` | Moteur AOD/Lucene — index fichiers locaux (legacy) |
| `BasicSearch/` | Moteur basique — SQL sans index |
| `ElasticSearch/` | Moteur ElasticSearch — haute performance, recommandé en production |
| `Exceptions/` | Exceptions métier de la recherche |
| `Index/` | Infrastructure d'indexation (AbstractIndexer, documentifiers, traits) |
| `SqlSearch/` | Moteur SQL simple — requêtes LIKE directes |
| `UI/` | Couche MVC de l'interface de recherche (formulaire + résultats) |

## Points d'entrée
- `SearchWrapper.php` — point d'entrée unique pour toute recherche dans SuiteCRM
- `ElasticSearch/ElasticSearchIndexer.php` — point d'entrée pour l'indexation ES

## Dépendances clés
- **Dépend de :** `lib/Log/` (logging Monolog), `elasticsearch/elasticsearch`, `Monolog`, `SugarBean`, moteur Smarty SuiteCRM
- **Utilisé par :** modules de recherche SuiteCRM, `lib/Robo/Plugin/Commands/ElasticSearchCommands`

## Notes
- ElasticSearch est le moteur recommandé pour la production.
- `SearchEngine::validateQuery()` lève `SearchInvalidRequestException` si la query est vide.
- Les moteurs sont configurés via `SearchConfigurator` (lit `$sugar_config`).
