# Fichier : view.detail.php

**Chemin :** `modules/Leads/views/view.detail.php`
**Type :** `PHP`
**Categorie :** view (detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue de detail d'un lead. Injecte la popup Form Letter et desactive le lien "Convert Lead" si le lead est deja converti et que la configuration `disable_convert_lead` est activee.

## Role technique

Classe `LeadsViewDetail` heritant de `ViewDetail`. Surcharge `display()` pour assigner la variable Smarty `DISABLE_CONVERT_ACTION` et integrer la popup PDF via `formLetter::DVPopupHtml()`.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ViewDetail` | Classe parente (framework) |
| `formLetter::DVPopupHtml()` | Popup Form Letter |
| `$sugar_config['disable_convert_lead']` | Config pour desactiver la conversion |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsViewDetail` | classe | Vue detail Lead |
| `display()` | methode | Surcharge : desactive Convert Lead si necessaire |

## Points d'attention

- La variable Smarty `DISABLE_CONVERT_ACTION` doit etre consommee dans le template pour masquer/desactiver le bouton Convert Lead.
- RAS autrement.
