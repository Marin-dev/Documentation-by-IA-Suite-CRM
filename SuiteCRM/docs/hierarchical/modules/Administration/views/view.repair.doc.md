# view.repair.php

**Chemin :** `modules/Administration/views/view.repair.php`
**Type :** PHP (view MVC SugarCRM)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de reparation rapide complète. Declenche immediatement un `clearAll` sur tous les modules et affiche un lien de retour. Accessible via `action=Repair`.

## Role technique
Etend `SugarView`. La methode `display()` instancie `RepairAndClear` et appelle `repairAndClearAll(['clearAll'], [translate('LBL_ALL_MODULES')], false, true)` — execution synchrone complete.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Administration/QuickRepairAndRebuild.php` | Classe RepairAndClear |

## Symboles principaux
- `ViewRepair extends SugarView` — classe view

## Interactions
- **Appele par :** `index.php?module=Administration&action=Repair`
- **Appelle :** `RepairAndClear::repairAndClearAll()`
