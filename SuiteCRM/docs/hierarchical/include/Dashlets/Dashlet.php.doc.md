# 📄 Dashlet.php

**Chemin :** `include/Dashlets/Dashlet.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe de base abstraite pour tous les dashlets du tableau de bord SuiteCRM. Elle définit le contrat minimal qu'un dashlet doit respecter : titre, icônes de configuration/rafraîchissement/suppression, rendu HTML de l'en-tête et du pied de page. Tout dashlet métier hérite de cette classe.

## ⚙️ Rôle technique
Fournit les propriétés communes (`id`, `title`, `isConfigurable`, `isRefreshable`, `autoRefresh`) et les méthodes de rendu HTML (`getHeader()`, `getFooter()`, `setConfigureIcon()`, `setRefreshIcon()`, `setDeleteIcon()`). Le rendu utilise `SugarThemeRegistry` pour les images et `Sugar_Smarty` pour les templates. Un système d'auto-rafraîchissement configurable en minutes est intégré.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/Sugar_Smarty.php` — moteur de templates Smarty
  - `include/utils/layout_utils.php` — utilitaires de mise en page (ex: `get_form_header`)
  - `SugarThemeRegistry` (globale) — accès aux images du thème courant

## 📤 Sorties / Exports
- `Dashlet` — classe (base framework) — classe parente de tous les dashlets
- **Consommateurs identifiés dans le repo :**
  - `include/Dashlets/DashletGeneric.php`
  - `include/Dashlets/DashletGenericChart.php`
  - `include/SugarObjects/templates/basic/Dashlets/Dashlet/m-n-Dashlet.php`

## 🔗 Relations clés
- **Appelé par :** modules `*/Dashlets/*.php`, `DashletGeneric`, `DashletGenericChart`
- **Appelle :** `SugarThemeRegistry::current()->getImage()`, `get_form_header()`, `Sugar_Smarty`
- **Position dans le flux global :** base du framework de tableau de bord ; instanciée par le moteur `MySugar` côté contrôleur

---

## 💡 Points d'attention
- `getTitle()` est marquée `@deprecated` depuis l'introduction de `getHeader()` / `getFooter()` (ligne 167).
- La propriété `$autoRefresh` est de type string `"0"` au lieu de `int 0` (ligne 96) — risque de comparaison stricte dans les consommateurs.
- `lock_homepage` dans `$sugar_config` désactive le bouton de suppression et le drag-and-drop (lignes 154, 191).
