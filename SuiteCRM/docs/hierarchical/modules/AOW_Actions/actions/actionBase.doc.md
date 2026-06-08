# actionBase.php

**Chemin :** `modules/AOW_Actions/actions/actionBase.php`
**Type :** PHP - Classe de base abstraite
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base pour toutes les actions de workflow AOW. Definit l'interface commune que chaque type d'action concret doit implementer ou surcharger.

## Role technique
Classe PHP simple (pas d'heritage). Fournit des implementations vides (no-op) pour les methodes `loadJS`, `edit_display` et `run_action`. Les classes concretes surchargent les methodes necessaires.

---

## Methodes
| Methode | Role |
|---|---|
| `__construct($id)` | Stocke l'id de l'action |
| `loadJS()` | Retourne les fichiers JS a charger pour l'edition (tableau vide par defaut) |
| `edit_display($line, $bean, $params)` | Retourne le HTML du formulaire d'edition de l'action |
| `run_action(SugarBean $bean, $params, $in_save)` | Execute l'action sur un bean (retourne `true` par defaut) |

## Relations cles
- **Etendue par :** `actionSendEmail`, `actionModifyRecord`, `actionCreateRecord`, `actionComputeField`
- **Appelee par :** `AOW_WorkFlow->run_actions()` (instanciation dynamique)

---

## Points d'attention
- Le nom de la classe concrete suit la convention `action{NomAction}` — ex: `actionSendEmail`.
- Support d'override dans `custom/modules/AOW_Actions/actions/` via prefixe `custom` (`customactionSendEmail`).
