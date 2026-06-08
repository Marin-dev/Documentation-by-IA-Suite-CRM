# 📄 ListViewXTPL.php

**Chemin :** `include/ListView/ListViewXTPL.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Implémentation de la vue liste utilisant le moteur XTemplate (héritage de SugarCRM). Alternative à `ListViewSmarty` pour les modules utilisant encore le moteur de templates XTemplate.

## ⚙️ Rôle technique
Hérite de `ListViewDisplay`. Utilise les blocs XTemplate nommés (`$row_block`, `$main_block`, `$nav_block`, etc.) pour le rendu des lignes, de la navigation et des sections pro/os. Encapsule un objet XTemplate (`$xtpl`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/ListView/ListViewDisplay.php` — classe parente

## 📤 Sorties / Exports
- `ListViewXTPL` — classe (framework/vue, legacy) — liste via XTemplate
  - Blocs : `$row_block`, `$main_block`, `$pro_block`, `$os_block`, `$nav_block`, `$pro_nav_block`

## 🔗 Relations clés
- **Appelé par :** modules legacy n'ayant pas migré vers Smarty
- **Appelle :** `ListViewDisplay`, XTemplate
- **Position dans le flux global :** pendant XTemplate de `ListViewSmarty` (Smarty)

---

## 💡 Points d'attention
- XTemplate est une technologie legacy — les nouveaux modules doivent utiliser `ListViewSmarty`.
- Les blocs `pro_block` et `os_block` suggèrent une distinction entre éditions SugarCRM Pro et Community Edition (héritage historique).
