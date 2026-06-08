# 📄 ListViewSmarty.php

**Chemin :** `include/ListView/ListViewSmarty.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Implémentation principale de la vue liste utilisant le moteur Smarty. C'est la classe utilisée par le framework MVC actuel pour toutes les vues liste des modules. Gère les colonnes affichées, les menus contextuels, les opérations en masse et la fusion de doublons.

## ⚙️ Rôle technique
Hérite de `ListViewDisplay`. Utilise `Sugar_Smarty` pour le rendu final. Expose des flags de fonctionnalités : `$export`, `$delete`, `$select`, `$mailMerge`, `$email`, `$targetList`, `$multiSelect`, `$quickViewLinks`, `$mergeduplicates`, `$contextMenus`. Intègre les menus contextuels via `contextMenu.php`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/ListView/ListViewDisplay.php` — classe parente
  - `include/contextMenus/contextMenu.php` — menus contextuels sur les lignes

## 📤 Sorties / Exports
- `ListViewSmarty` — classe (framework/vue) — liste Smarty du nouveau framework
  - `$displayColumns`, `$searchColumns`, `$tpl` — configuration d'affichage
  - `$lvd` — instance de `ListViewData`
- **Consommateurs identifiés dans le repo :**
  - `include/Dashlets/DashletGeneric.php`
  - `include/ListView/ListViewFacade.php`
  - `modules/*/views/view.list.php`

## 🔗 Relations clés
- **Appelé par :** contrôleurs de modules (nouveau framework), `DashletGeneric`
- **Appelle :** `ListViewDisplay`, `Sugar_Smarty`, `contextMenu`
- **Position dans le flux global :** rendu final de toutes les vues liste dans le CRM

---

## 💡 Points d'attention
- `$menu_location = 'top'` par défaut — peut être changé en `'bottom'` pour déplacer les boutons d'action.
- `$quickViewLinks = true` — active les liens de prévisualisation rapide (hover panel) sur les enregistrements.
- Nombreux flags booléens à configurer selon le contexte (sous-panneau vs liste principale).
