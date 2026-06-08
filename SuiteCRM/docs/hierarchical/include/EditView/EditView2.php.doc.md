# 📄 EditView2.php (nouveau framework)

**Chemin :** `include/EditView/EditView2.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe centrale du framework de vues d'édition/détail/création rapide. Utilisée par tous les modules SuiteCRM pour afficher un formulaire de création ou de modification d'enregistrement. C'est la base du nouveau framework MVC basé sur les metadata.

## ⚙️ Rôle technique
Charge les définitions de vue depuis un fichier `editviewdefs.php` (ou son équivalent) via `TemplateHandler`. Gère la navigation VCR via `SugarVCR`. Expose de nombreuses propriétés de configuration : `$tpl`, `$metadataFile`, `$view`, `$formatFields`, `$showDetailData`, `$showVCRControl`, `$isDuplicate`, `$sectionPanels`, etc. Les sous-classes `DetailView2`, `QuickCreate`, `SubpanelQuickCreate` étendent cette classe.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/TemplateHandler/TemplateHandler.php` — lecture et rendu des métadonnées de vue
  - `include/EditView/SugarVCR.php` — gestion de la navigation entre enregistrements
- **Arguments :** `$module`, `$focus` (SugarBean), `$metadataFile`, `$tpl`

## 📤 Sorties / Exports
- `EditView` — classe (framework/vue) — vue d'édition principale du nouveau framework
  - Propriétés clés : `$th` (TemplateHandler), `$focus` (SugarBean), `$fieldDefs`, `$sectionPanels`, `$view`
- **Consommateurs identifiés dans le repo :**
  - `include/DetailView/DetailView2.php`
  - `include/EditView/QuickCreate.php`
  - `include/EditView/SubpanelQuickCreate.php`
  - `include/SearchForm/SearchForm2.php`
  - `modules/*/views/view.edit.php`

## 🔗 Relations clés
- **Appelé par :** contrôleurs MVC de tous les modules standard, `DetailView2`
- **Appelle :** `TemplateHandler`, `SugarVCR`, `SugarBean`
- **Position dans le flux global :** coeur de la couche vue ; appelé par les contrôleurs après hydratation du SugarBean

---

## 💡 Points d'attention
- Définit une classe nommée `EditView` comme le fichier legacy `EditView.php` — ne jamais inclure les deux simultanément.
- `$returnAction`, `$returnModule`, `$returnId` gèrent le retour après sauvegarde — logique de navigation post-save.
- `$showVCRControl = true` par défaut (ligne 156) — peut être désactivé pour les popups ou quick creates.
