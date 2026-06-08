# SqlSearch

## Rôle
Ce dossier contient le moteur de recherche SQL simple de SuiteCRM. Il effectue des recherches directement en base de données via des requêtes SQL `LIKE`, sans indexation préalable. C'est une alternative légère à ElasticSearch pour les déploiements sans moteur de recherche dédié.

## Contenu
| Fichier | Rôle |
|---|---|
| `SimpleSqlSearchEngine.php` | Moteur de recherche SQL — requêtes LIKE directes en BD, retourne `SearchResults` |

## Points d'entrée
- `SimpleSqlSearchEngine.php` — instancié par `SearchWrapper` quand le moteur SQL est sélectionné

## Dépendances clés
- **Dépend de :** `lib/Search/SearchEngine.php` (classe abstraite parente), `DBManager` (global SuiteCRM)
- **Utilisé par :** `lib/Search/SearchWrapper.php`

## Notes
- Performances dégradées sur de gros volumes (requêtes `LIKE` sans index full-text).
- Ne nécessite aucun service externe — fonctionne avec la base de données SuiteCRM existante.
- Alternative recommandée quand ElasticSearch n'est pas disponible et que les volumes restent modérés.
