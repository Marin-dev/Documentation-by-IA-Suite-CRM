# View.php (Search)

**Chemin :** `modules/Administration/Search/View.php`
**Namespace :** `SuiteCRM\Modules\Administration\Search`
**Type :** PHP (View MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de la page de configuration de la recherche. Affiche le moteur actuel, les moteurs disponibles (legacy + nouveaux), et les modules actives/desactives pour la recherche globale.

## Role technique
Etend `MVC\View`. `preDisplay()` : charge les moteurs legacy (`BasicSearchEngine`, `BasicAndAodEngine` si AOD actif), fusionne avec les moteurs FTS, retire `LuceneSearchEngine`. `display()` : charge les modules via `SearchModules::getAllModules()`, encode en JSON pour Smarty.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Search\SearchModules` | Modules de recherche actifs/desactifs |
| `SuiteCRM\Search\SearchWrapper` | Moteur et controleur actuel |

## Interactions
- **Instanciee par :** `Search\Controller`
- **Template :** `modules/Administration/Search/view.tpl`
