# view.indexdata.php

**Chemin :** `modules/AOD_Index/views/view.indexdata.php`
**Type :** PHP — View (SugarView)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue d'administration de l'index AOD. Affiche les statistiques de l'index Lucene (nombre total d'enregistrements, indexes, echoues, fichiers d'index) et, si des echecs existent, un tableau liste des enregistrements en echec d'indexation. Deprecie depuis v7.12.0.

## Role technique
Herite de `SugarView`. La methode `display()` effectue des requetes SQL directes via `DBManagerFactory` pour compter les enregistrements par module et les evenements d'indexation. Alimente un template Smarty (`modules/AOD_Index/tpls/indexdata.tpl`). Si des echecs existent, instancie un `ListViewSmarty` pour afficher les `AOD_IndexEvent` en echec.

---

## Entrees / Dependances
- **Imports principaux :**
  - `SugarView` (`include/MVC/View/SugarView.php`) — classe parente
  - `DBManagerFactory` (framework) — requetes SQL de comptage
  - `BeanFactory` (framework) — acces a `AOD_Index` et `AOD_IndexEvent`
  - `ListViewSmarty` (framework) — rendu du tableau des echecs
  - `AOD_Index::getIndexableModules()` — liste des modules indexables
  - Template Smarty : `modules/AOD_Index/tpls/indexdata.tpl` (fichier TPL non PHP, hors perimetre)

## Sorties / Exports
| Symbole | Type | Role |
|---|---|---|
| `AOD_IndexViewIndexData` | classe | Vue des statistiques d'indexation |
| `display()` | methode publique | Rendu complet de la page de stats |

Variables Smarty assignees :
| Variable | Contenu |
|---|---|
| `revisionCount` | Somme des enregistrements non supprimes dans tous les modules indexables |
| `indexedCount` | Nombre d'evenements d'index avec `success=1` |
| `failedCount` | Nombre d'evenements d'index avec `success=0` |
| `index` | Bean AOD_Index (singleton) |
| `indexFiles` | Nombre de fichiers `.cfs` dans le repertoire de l'index |

- **Consommateurs identifies :**
  - `modules/AOD_Index/controller.php` — route `action_indexdata` vers cette vue

## Relations cles
- **Appele par :** `AOD_IndexController::action_indexdata()`
- **Appelle :** `AOD_Index::getIndex()`, `AOD_Index::getIndexableModules()`, `DBManagerFactory`, `ListViewSmarty`, template `indexdata.tpl`
- **Position dans le flux global :** Vue de monitoring de l'index, accessible depuis l'interface d'administration

---

## Points d'attention
- **Deprecie depuis v7.12.0.**
- Les requetes SQL de comptage sont generees pour chaque module indexable — peut etre lent si de nombreux modules sont actives.
- `glob($index->location."/*.cfs")` peut retourner `false` si le repertoire n'existe pas — gere par `is_countable()`.
- La vue charge dynamiquement les `listviewdefs` de `AOD_IndexEvent` avec un `require` — chemin dependant de `$seed->module_dir`.
