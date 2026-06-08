# View.php (Search/MVC)

**Chemin :** `modules/Administration/Search/MVC/View.php`
**Namespace :** `SuiteCRM\Modules\Administration\Search\MVC`
**Type :** PHP (View abstraite MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe abstraite de base pour les vues Search. Fournit `preDisplay()` avec assignation Smarty commune (MOD, APP, config search) et methodes utilitaires (`getButtons()`, `getEngines()`).

## Symboles principaux

| Methode | Role |
|---|---|
| `preDisplay()` | Assigne variables globales Smarty + config search |
| `getButtons()` | Genere les boutons Save/Cancel HTML inline |
| `getEngines()` | Retourne liste moteurs de recherche via SearchWrapper |

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Search\SearchWrapper` | Liste des moteurs de recherche |
| `SuiteCRM\Search\UI\MVC\View` | Classe de base |

## Interactions
- **Etendu par :** `SuiteCRM\Modules\Administration\Search\View`, `SuiteCRM\Modules\Administration\Search\ElasticSearch\View`
