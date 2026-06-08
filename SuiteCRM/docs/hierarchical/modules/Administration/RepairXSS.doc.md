# RepairXSS.php

**Chemin :** `modules/Administration/RepairXSS.php`
**Type :** PHP (view + action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Interface de reparation XSS : permet de re-sauvegarder tous les enregistrements d'un bean (ou de tous les modules) pour que la sanitisation XSS (`cleanBean()`) soit appliquee sur les donnees existantes. Utile apres une mise a jour des regles de nettoyage.

## Role technique
En mode normal : affiche un dropdown de selection de module et un template (`templates/RepairXSS.tpl`) avec estimation du nombre d'enregistrements. L'execution reelle est asynchrone via `Async.php` (`adminAction=refreshEstimate` et `adminAction=repairXssExecute`). En mode silencieux (`$runSilent`), appelle `cleanAllBeans()` (vide actuellement).

---

## Dependances cles
| Element | Role |
|---|---|
| `include/modules.php` | $moduleList, $beanList, $beanFiles |
| `Sugar_Smarty` | Template |
| `Async.php` | Execution asynchrone des reparations |

## Symboles principaux

| Fonction | Role |
|---|---|
| `cleanAllBeans()` | Corps vide — placeholder non implemente |

## Interactions
- **Appele par :** `index.php?module=Administration&action=RepairXSS`
- **Appelle (async) :** `Async.php` via AJAX JS
- **Template :** `modules/Administration/templates/RepairXSS.tpl`

---

## Notes
- `cleanAllBeans()` est vide (ligne 55-56) — la fonctionnalite synchrone pour scheduler n'est pas implementee.
- La logique reelle est dans `Async.php` (actions `refreshEstimate` et `repairXssExecute`).
