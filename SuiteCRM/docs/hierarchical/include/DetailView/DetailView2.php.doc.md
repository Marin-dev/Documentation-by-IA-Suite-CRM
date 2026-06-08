# 📄 DetailView2.php

**Chemin :** `include/DetailView/DetailView2.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Nouvelle implémentation de la vue de détail basée sur le framework metadata. Affiche un enregistrement SuiteCRM en lecture seule à partir des définitions de vue (`detailviewdefs.php`). C'est la classe utilisée par les modules dans le framework MVC actuel.

## ⚙️ Rôle technique
Hérite d'`EditView` (le détail réutilise la même infrastructure de rendu que l'édition). La propriété `$view = 'DetailView'` oriente le rendu. La méthode `setup()` charge le template Smarty (`include/DetailView/DetailView.tpl` par défaut) et le fichier de métadonnées (`detailviewdefs` par défaut). Utilise `TemplateHandler` pour le rendu des champs.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/TemplateHandler/TemplateHandler.php` — moteur de rendu des champs
  - `include/EditView/EditView2.php` — classe parente (`EditView`)
- **Arguments de `setup()` :** `$module`, `$focus` (SugarBean), `$metadataFile`, `$tpl`, `$createFocus`, `$metadataFileName`

## 📤 Sorties / Exports
- `DetailView2` — classe (framework/vue) — vue détail du nouveau framework
  - `setup(...)` — méthode principale d'initialisation
- **Consommateurs identifiés dans le repo :** `modules/*/views/view.detail.php`

## 🔗 Relations clés
- **Appelé par :** contrôleurs MVC de tous les modules standard
- **Appelle :** `EditView::setup()`, `TemplateHandler`
- **Position dans le flux global :** vue lecture seule dans le cycle Create/Edit/Detail/List

---

## 💡 Points d'attention
- Hérite d'`EditView` bien qu'il s'agisse d'une vue en lecture — le template Smarty diffère mais la logique de rendu de champs est partagée.
- Le paramètre `$metadataFileName` (défaut `'detailviewdefs'`) permet de charger une vue alternative (ex: popup detail).
- `$createFocus = true` par défaut : instancie un nouveau SugarBean si `$focus` est null.
