# 📄 SearchForm2.php

**Chemin :** `include/SearchForm/SearchForm2.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Nouvelle implémentation du formulaire de recherche basée sur le framework metadata. Gère les onglets basic/advanced/custom, les recherches sauvegardées, et pilote l'affichage de la liste de résultats via `ListViewSmarty`. C'est la classe utilisée par tous les modules dans le framework MVC actuel.

## ⚙️ Rôle technique
Charge les définitions depuis `searchdefs.php` et `listviewdefs.php`. Utilise `TemplateHandler` (via `EditView2`) pour le rendu des champs. Gère `$displayView` ('basic_search' / 'advanced_search'), `$showAdvanced`, `$showBasic`, `$showCustom`, `$displaySavedSearch`. Intègre la pagination et le tri via `$lv` (instance de `ListViewSmarty`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/tabs.php` — onglets basic/advanced
  - `include/ListView/ListViewSmarty.php` — affichage des résultats
  - `include/TemplateHandler/TemplateHandler.php` — rendu des champs de recherche
  - `include/EditView/EditView2.php` — rendu de formulaire

## 📤 Sorties / Exports
- `SearchForm` — classe (framework/vue) — formulaire de recherche nouveau framework
  - `$lv` — `ListViewSmarty` (liste des résultats)
  - `$th` — `TemplateHandler`
  - `$displayView`, `$showAdvanced`, `$showBasic`, `$showCustom`
  - `$displaySavedSearch` — affichage des recherches sauvegardées
- **Consommateurs identifiés dans le repo :** `modules/*/views/view.list.php`

## 🔗 Relations clés
- **Appelé par :** contrôleurs de modules (nouveau framework), vues liste
- **Appelle :** `ListViewSmarty`, `TemplateHandler`, `EditView2`
- **Position dans le flux global :** formulaire de filtre en amont de la `ListViewSmarty`

---

## 💡 Points d'attention
- `$showSavedSearchesOptions = true` (ligne 80) — affiche le dropdown des recherches sauvegardées par défaut.
- `$nbTabs` est calculé dynamiquement selon les flags `$showBasic`, `$showAdvanced`, `$showCustom`.
- Même nom de classe (`SearchForm`) que le fichier legacy `SearchForm.php` — conflit si les deux sont inclus.
