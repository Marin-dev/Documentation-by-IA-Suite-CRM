# TreeData.php

**Chemin :** `TreeData.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée AJAX pour la récupération de données arborescentes (tree data) utilisées par les composants d'interface de type arbre (catégories produits, tags KB, prévisions, documents). Dispatche les appels vers les fonctions de données spécifiques à chaque module.

**Type :** entrypoint (AJAX)

## Rôle technique

Parse les paramètres de la requête (`$_REQUEST`) en les classant par préfixe (`PARAMT_` = paramètres arbre, `PARAMN_` = paramètres nœud), valide le module et la fonction demandée contre une whitelist, puis appelle la fonction via `call_user_func()`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/modules.php` — mapping `$beanList` pour valider le module
  - `modules/{module}/TreeData.php` — fonctions de données spécifiques au module
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 2), whitelist de modules et fonctions (lignes 99-141)
- **Paramètres d'entrée ($_REQUEST) :**
  - `module` — nom du module cible (requis)
  - `function` / `call_back_function` — nom de la fonction à appeler
  - `PARAMT_*` — paramètres au niveau de l'arbre
  - `PARAMN_*_{depth}` — paramètres au niveau des nœuds par profondeur

## Whitelist des modules et fonctions autorisés

| Module | Fonctions autorisées |
|---|---|
| `ProductTemplates` | `get_node_data`, `get_categories_and_products` |
| `ProductCategories` | `get_node_data`, `get_product_categories` |
| `KBTags` | `get_node_data`, `get_tags_nodes`, `childNodes`, `getRootNode`, `get_browse_documents`, etc. |
| `KBDocuments` | `get_node_data`, `get_category_nodes`, `get_documents` |
| `Forecasts` | `get_node_data`, `get_worksheet`, `commit_forecast`, `save_worksheet`, etc. |
| `Documents` | `get_node_data`, `get_category_nodes`, `get_documents` |

## Relations clés

- **Appelé par :** composants JavaScript d'arborescence dans l'interface SuiteCRM (widgets ytree/AJAX)
- **Appelle :** `modules/{module}/TreeData.php` → `call_user_func($func_name, $params1)`

---

## Points d'attention

- La whitelist `$TreeDataFunctions` (lignes 99-141) est la protection principale contre l'exécution de fonctions arbitraires — toute extension doit y être ajoutée.
- `call_user_func($func_name, ...)` appelle la fonction globalement (pas une méthode de classe) — les fonctions doivent être définies dans le scope global du fichier `TreeData.php` du module.
- `$GLOBALS['log']->debug("TreeData:session started")` en ligne 53 — logging de debug actif.
- Aucune vérification ACL explicite dans ce dispatcher — délégué aux fonctions de modules.
