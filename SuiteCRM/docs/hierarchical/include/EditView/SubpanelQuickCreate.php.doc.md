# 📄 SubpanelQuickCreate.php

**Chemin :** `include/EditView/SubpanelQuickCreate.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Formulaire de création rapide intégré dans un sous-panneau (subpanel). Permet de créer un enregistrement lié directement depuis la vue détail d'un enregistrement parent, sans navigation vers un autre écran.

## ⚙️ Rôle technique
Ne hérite pas directement d'`EditView` — encapsule une instance d'`EditView2` (`$this->ev`). Utilise `$viewType = 'QuickCreate'` pour charger les métadonnées `quickcreatedefs.php`. Propriété `$defaultProcess` contrôle si le traitement standard est appliqué automatiquement.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/EditView/EditView2.php` — vue d'édition encapsulée (composition, pas héritage)

## 📤 Sorties / Exports
- `SubpanelQuickCreate` — classe (framework/vue) — création rapide dans sous-panneau
  - `$defaultProcess` — contrôle du traitement automatique
  - `$viewType` — type de vue (`'QuickCreate'`)
- **Consommateurs identifiés dans le repo :**
  - `include/EditView/PopupQuickCreate.php`
  - sous-panneaux des modules

## 🔗 Relations clés
- **Appelé par :** rendus de sous-panneaux (`SubpanelLayouts`)
- **Appelle :** `EditView2`
- **Position dans le flux global :** création inline depuis vue détail parent

---

## 💡 Points d'attention
- Utilise la composition (`$this->ev = new EditView()`) plutôt que l'héritage — différent de `QuickCreate`.
- `$defs['templateMeta']['form']['buttons']` est accessible sur `$this->ev` pour personnaliser les boutons.
