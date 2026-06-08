# PDFView.php

**Chemin :** `modules/Administration/PDF/PDFView.php`
**Namespace :** `SuiteCRM\Modules\Administration\PDF`
**Type :** PHP (View MVC)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de la page de configuration PDF. Assigne les moteurs disponibles, le moteur par defaut et le controleur actuel au template Smarty.

## Role technique
Etend `MVC\View`. `preDisplay()` appelle `PDFWrapper::getController()` et `PDFWrapper::getDefaultEngine()`, construit la liste des moteurs via `getEngines()`. `display()` affiche `modules/Administration/PDF/view.tpl` (ou override dans `custom/`).

---

## Dependances cles
| Element | Role |
|---|---|
| `SuiteCRM\PDF\PDFWrapper` | Acces moteur PDF actuel |
| `MVC\View` (abstrait) | Classe de base |

## Interactions
- **Instanciee par :** `PDF\Controller`
- **Template :** `modules/Administration/PDF/view.tpl`
