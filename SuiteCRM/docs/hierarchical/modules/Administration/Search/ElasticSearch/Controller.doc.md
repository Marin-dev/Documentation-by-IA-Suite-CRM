# Controller.php (Search/ElasticSearch)

**Chemin :** `modules/Administration/Search/ElasticSearch/Controller.php`
**Namespace :** `SuiteCRM\Modules\Administration\Search\ElasticSearch`
**Type :** PHP (Controller MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur pour la page de configuration ElasticSearch. Gere la sauvegarde de la config ES (host, user, pass, enabled), le test de connexion, et la planification d'indexation complete ou partielle.

## Role technique
Etend `MVC\Controller`. Actions :
- `doSaveConfig()` : sauvegarde via `Configurator` dans `config_override.php`
- `doTestConnection()` : teste la connexion HTTPS avec `ClientBuilder`, retourne JSON
- `doFullIndex()` / `doPartialIndex()` : cree un `SchedulersJob` en file via `SugarJobQueue`
- `getSchedulers()` : liste les planificateurs `runElasticSearchIndexerScheduler`

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Search\ElasticSearch\ElasticSearchClientBuilder` | Construction client ES |
| `SuiteCRM\Search\ElasticSearch\ElasticSearchIndexer` | Test de ping ES |
| `Elasticsearch\ClientBuilder` | Client ES officiel |
| `SugarJobQueue` | File de planification |
| `SchedulersJob` | Bean job planificateur |
| `Configurator` | Persistance config |

## Symboles principaux

| Methode | Role |
|---|---|
| `doSaveConfig()` | Sauvegarde config ES (host/user/pass/enabled) |
| `doTestConnection()` | Test connexion ES, retourne JSON |
| `doFullIndex()` | Planifie indexation complete |
| `doPartialIndex()` | Planifie indexation partielle |
| `getSchedulers()` | Liste planificateurs ES |

## Interactions
- **Instancie par :** `ElasticSearchSettings.php`
- **Appelle :** `SugarJobQueue::submitJob()`, `ElasticSearchIndexer::ping()`
