# Controller.php (PDF)

**Chemin :** `modules/Administration/PDF/Controller.php`
**Namespace :** `SuiteCRM\Modules\Administration\PDF`
**Type :** PHP (Controller MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur pour la page de configuration du moteur PDF. Gere la sauvegarde du moteur PDF selectionne (via `PDFConfigurator`). Supporte les appels AJAX.

## Role technique
Etend `SuiteCRM\Modules\Administration\PDF\MVC\Controller`. `doSave()` lit `$_POST['pdf-engine']` via `filter_input`, configure et sauvegarde via `PDFConfigurator::make()->setEngine()->save()`. Redirige ou renvoie JSON selon `isAjax()`.

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\PDF\PDFConfigurator` | Sauvegarde du moteur PDF |
| `MVC\Controller` (abstrait) | Classe de base |

## Interactions
- **Instancie par :** `PDFSettings.php`
- **Appelle :** `PDFConfigurator::make()->setEngine()->save()`
