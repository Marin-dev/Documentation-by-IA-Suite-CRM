# 📄 ListViewDisplay.php

**Chemin :** `include/ListView/ListViewDisplay.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Classe de rendu intermédiaire pour les listes d'enregistrements. Gère l'affichage du formulaire de mise à jour en masse, du menu d'action et des lignes de liste. Base de `ListViewSmarty` et `ListViewXTPL`.

## ⚙️ Rôle technique
Orchestre l'affichage en combinant les données de `ListViewData` et le moteur de templates. Contient un compteur statique `$listViewCounter` pour gérer plusieurs listes sur une même page. Intègre `MassUpdate` pour le formulaire de mise à jour en masse et gère l'action dropdown.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/ListView/ListViewData.php` — données de la liste
  - `include/MassUpdate.php` — formulaire de mise à jour en masse

## 📤 Sorties / Exports
- `ListViewDisplay` — classe (framework/vue) — rendu de liste intermédiaire
  - `$listViewCounter` — statique, compte les listes sur la page
  - `$show_mass_update_form`, `$show_action_dropdown` — contrôles d'affichage
- **Consommateurs identifiés dans le repo :**
  - `include/ListView/ListViewSmarty.php` (hérite)
  - `include/ListView/ListViewXTPL.php` (hérite)

## 🔗 Relations clés
- **Appelé par :** `ListViewSmarty`, `ListViewXTPL`
- **Appelle :** `ListViewData`, `MassUpdate`
- **Position dans le flux global :** couche rendu entre les données et le template final

---

## 💡 Points d'attention
- `$listViewCounter` statique permet d'identifier chaque liste par un ID unique sur la page — important pour le JavaScript multi-liste.
- `$mass = null` par défaut — instancié uniquement si `$show_mass_update_form = true`.
