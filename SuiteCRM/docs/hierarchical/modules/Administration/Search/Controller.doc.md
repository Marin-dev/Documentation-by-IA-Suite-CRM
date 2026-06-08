# Controller.php (Search)

**Chemin :** `modules/Administration/Search/Controller.php`
**Namespace :** `SuiteCRM\Modules\Administration\Search`
**Type :** PHP (Controller MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur pour la page de configuration du moteur de recherche. Gere la sauvegarde du moteur selectionne et des modules actives pour la recherche globale.

## Role technique
Etend `MVC\Controller`. `doSave()` : lit `$_POST['search-engine']`, configure via `SearchConfigurator::make()->setEngine()->save()`, puis appelle `SearchModules::saveGlobalSearchSettings()`. Supporte AJAX.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\Search\SearchConfigurator` | Sauvegarde du moteur de recherche |
| `SuiteCRM\Search\SearchModules` | Sauvegarde des modules de recherche |

## Interactions
- **Instancie par :** `SearchSettings.php`
