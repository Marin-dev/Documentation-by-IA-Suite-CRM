# 📄 ListView.php

**Chemin :** `include/ListView/ListView.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe de base pour l'affichage des listes d'enregistrements dans SuiteCRM (vue liste des modules). Gère la pagination, le tri, les boutons d'action (export, suppression, sélection), la mise à jour en masse et l'affichage de l'en-tête/pied de page de liste.

## ⚙️ Rôle technique
Classe centrale legacy du framework de liste. Encapsule la logique de rendu d'une liste via XTemplate (`$xTemplate`). Expose de nombreuses propriétés de contrôle : `$records_per_page`, `$show_export_button`, `$show_delete_button`, `$show_mass_update`, `$show_paging`, `$inline`, etc. Utilisée comme classe parente par `DetailView` et `ListViewSubPanel`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/SugarVCR.php` — navigation entre enregistrements
- **Variables globales :** `$app_strings`, `$current_module`, `$mod_strings`, `$theme`

## 📤 Sorties / Exports
- `ListView` — classe (framework/vue) — liste d'enregistrements
- **Consommateurs identifiés dans le repo :**
  - `include/DetailView/DetailView.php` (hérite)
  - `include/ListView/ListViewSubPanel.php` (hérite)
  - modules legacy `view.list.php`

## 🔗 Relations clés
- **Appelé par :** contrôleurs de modules (legacy), `DetailView`
- **Appelle :** `SugarVCR`, XTemplate
- **Position dans le flux global :** couche vue liste legacy ; le nouveau framework utilise `ListViewSmarty`

---

## 💡 Points d'attention
- Classe legacy — le nouveau framework utilise `ListViewSmarty` (via `ListViewDisplay`).
- `$is_dynamic` et `$inline` permettent des modes d'affichage spéciaux (sous-panneau, modal) — logique conditionnelle importante dans les méthodes de rendu.
- `$list_field_defs` doit être peuplé par le contrôleur avant l'appel au rendu.
