# 📄 QuickCreate.php

**Chemin :** `include/EditView/QuickCreate.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Formulaire de création rapide d'enregistrement (version allégée du formulaire d'édition complet). Utilisé pour créer un enregistrement depuis un widget rapide sans quitter la page courante, potentiellement via AJAX.

## ⚙️ Rôle technique
Hérite d'`EditView` (legacy). Ajoute la propriété `$viaAJAX` pour indiquer si la requête provient d'un appel AJAX. Surcharge `process()` avec un paramètre `$checkFormName` pour la validation du nom de formulaire.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/EditView.php` — classe parente (legacy EditView)

## 📤 Sorties / Exports
- `QuickCreate` — classe (framework/vue) — formulaire de création rapide
  - `$viaAJAX` — booléen AJAX
  - `process($checkFormName, $formName)` — rendu du formulaire

## 🔗 Relations clés
- **Appelé par :** widgets de création rapide dans les modules, boutons "+" dans les sous-panneaux
- **Appelle :** `EditView::process()`
- **Position dans le flux global :** entrée de création allégée ; alternative à la vue EditView complète

---

## 💡 Points d'attention
- Hérite de l'`EditView` legacy (pas d'`EditView2`) — à distinguer de `SubpanelQuickCreate` qui hérite d'`EditView2`.
