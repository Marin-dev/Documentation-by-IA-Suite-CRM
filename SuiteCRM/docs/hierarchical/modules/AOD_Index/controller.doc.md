# controller.php

**Chemin :** `modules/AOD_Index/controller.php`
**Type :** PHP — Controller (SugarController)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur HTTP du module AOD_Index. Expose deux actions : affichage des statistiques de l'index (`indexdata`) et declenchement manuel de l'optimisation de l'index Lucene (`optimise`). L'action `index` est remappee vers `indexdata`. Deprecie depuis v7.12.0.

## Role technique
Herite de `SugarController`. L'action `optimise` appelle directement `AOD_Index::optimise()` avec un timeout eleve (6000s) puis redirige vers le module. L'action `indexdata` se contente de setter `$this->view = 'indexdata'` pour deleguer l'affichage a `view.indexdata.php`.

---

## Entrees / Dependances
- **Imports principaux :**
  - `SugarController` (framework SugarCRM) — classe parente
  - `BeanFactory` (framework) — acces au bean AOD_Index
  - `SugarApplication` (framework) — redirection HTTP
- **Guard :** `sugarEntry` verifie en debut de fichier

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `AOD_IndexController` | classe | Controleur du module AOD_Index |
| `action_indexdata()` | methode | Route vers la vue `indexdata` |
| `action_optimise()` | methode | Declenche l'optimisation Lucene et redirige |

- **Consommateurs identifies :**
  - Framework SugarCRM (routage automatique par nom de module)

## Relations cles
- **Appele par :** Framework MVC SugarCRM via URL `index.php?module=AOD_Index&action=optimise`
- **Appelle :** `AOD_Index::getIndex()`, `AOD_Index::optimise()`, `SugarApplication::redirect()`
- **Position dans le flux global :** Point d'entree HTTP pour la gestion manuelle de l'index ; utilise depuis l'interface d'administration

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- `set_time_limit(6000)` dans `action_optimise` — l'optimisation peut durer tres longtemps sur un index volumineux.
- Le remapping `'index'=>'indexdata'` fait que l'URL `?module=AOD_Index&action=index` affiche en realite la vue `indexdata`.
