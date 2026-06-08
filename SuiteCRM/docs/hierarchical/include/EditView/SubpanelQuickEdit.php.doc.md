# 📄 SubpanelQuickEdit.php

**Chemin :** `include/EditView/SubpanelQuickEdit.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Formulaire d'édition rapide intégré dans un sous-panneau. Permet de modifier un enregistrement lié directement dans la vue détail du parent sans navigation. Fonctionnellement équivalent à `SubpanelQuickCreate` mais pour l'édition d'un existant.

## ⚙️ Rôle technique
Hérite de `SubpanelQuickCreate`. Le constructeur reçoit `$view = 'QuickEdit'` mais le normalise immédiatement en `'QuickCreate'` (ligne 58-60), car les deux vues partagent la même définition de métadonnées `quickcreatedefs.php`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/EditView2.php` — héritée via `SubpanelQuickCreate`

## 📤 Sorties / Exports
- `SubpanelQuickEdit` — classe (framework/vue) — édition rapide dans sous-panneau
- **Consommateurs identifiés dans le repo :** sous-panneaux des modules (InlineEditing)

## 🔗 Relations clés
- **Appelé par :** sous-panneaux avec édition inline activée
- **Appelle :** `SubpanelQuickCreate::__construct()`
- **Position dans le flux global :** édition inline depuis vue détail parent

---

## 💡 Points d'attention
- La vue `'QuickEdit'` est convertie en `'QuickCreate'` (ligne 58) — les deux partagent les mêmes métadonnées. C'est intentionnel selon le commentaire du code.
