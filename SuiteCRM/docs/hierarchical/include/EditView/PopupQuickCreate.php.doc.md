# 📄 PopupQuickCreate.php

**Chemin :** `include/EditView/PopupQuickCreate.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Formulaire de création rapide affiché dans une fenêtre popup. Permet de créer un enregistrement lié depuis un popup et de retourner l'ID créé à la fenêtre parente (ex: sélection d'un contact depuis un formulaire de réunion).

## ⚙️ Rôle technique
Hérite de `SubpanelQuickCreate`. Force `$defaultProcess = false` pour contrôler manuellement le traitement. Remplace les boutons du formulaire par `['POPUPSAVE', 'POPUPCANCEL']` (ligne 56) — boutons spécifiques au contexte popup avec callbacks JavaScript vers la fenêtre parente.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/SubpanelQuickCreate.php` — classe parente

## 📤 Sorties / Exports
- `PopupQuickCreate` — classe (framework/vue) — création rapide en popup
  - `process($module)` — rendu du formulaire popup

## 🔗 Relations clés
- **Appelé par :** mécanismes de sélection relate (champs de type relate/parent)
- **Appelle :** `SubpanelQuickCreate::__construct()`, `SubpanelQuickCreate::process()`
- **Position dans le flux global :** création inline depuis un popup de sélection

---

## 💡 Points d'attention
- Les boutons `POPUPSAVE` et `POPUPCANCEL` impliquent du JavaScript côté client pour la communication inter-fenêtres — couplage fort au thème/JS frontend.
