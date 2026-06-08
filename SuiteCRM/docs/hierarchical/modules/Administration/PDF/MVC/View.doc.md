# View.php (PDF/MVC)

**Chemin :** `modules/Administration/PDF/MVC/View.php`
**Namespace :** `SuiteCRM\Modules\Administration\PDF\MVC`
**Type :** PHP (View abstraite MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe abstraite de base pour les vues du sous-module PDF. Fournit `preDisplay()` avec assignation Smarty commune (MOD, APP, config PDF) et methodes utilitaires (`getButtons()`, `getEngines()`).

## Symboles principaux

| Methode | Role |
|---|---|
| `preDisplay()` | Assigne variables globales Smarty + config PDF |
| `getButtons()` | Genere les boutons Save/Cancel |
| `getEngines()` | Retourne liste moteurs PDF disponibles |

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\PDF\PDFWrapper` | Liste des moteurs disponibles |
| `SuiteCRM\Search\UI\MVC\View` | Classe de base |
| `SuiteCRM\Utility\StringUtils` | Conversion camelCase vers label traduit |

## Interactions
- **Etendu par :** `SuiteCRM\Modules\Administration\PDF\PDFView`
