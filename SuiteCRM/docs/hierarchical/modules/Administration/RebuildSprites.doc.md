# RebuildSprites.php

**Chemin :** `modules/Administration/RebuildSprites.php`
**Type :** PHP (view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'interface pour la reconstruction des sprites CSS (images combinées). Affiche un message de traitement et le template qui declenche la reconstruction via AJAX.

## Role technique
Si `$_REQUEST['process']` n'est pas defini, affiche le template `RebuildSprites.tpl`. La reconstruction reelle est effectuee via `AdministrationController::action_callRebuildSprites()` (appel AJAX).

---

## Interactions
- **Appele par :** `index.php?module=Administration&action=RebuildSprites`
- **Template :** `modules/Administration/templates/RebuildSprites.tpl`
- **Execution reelle :** `AdministrationController::action_callRebuildSprites()` via AJAX
