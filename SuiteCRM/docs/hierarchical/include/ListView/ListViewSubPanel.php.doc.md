# 📄 ListViewSubPanel.php

**Chemin :** `include/ListView/ListViewSubPanel.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Spécialisation de `ListView` pour l'affichage dans un sous-panneau (subpanel). Affiche une liste d'enregistrements liés à un enregistrement parent directement dans sa vue détail.

## ⚙️ Rôle technique
Hérite de `ListView`. Remplace le moteur XTemplate par `Sugar_Smarty` pour le rendu (`$smartyTemplate`). Le constructeur instancie directement `Sugar_Smarty` en plus d'appeler `parent::__construct()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `ListView` (héritée) — `include/ListView/ListView.php`
  - `Sugar_Smarty` — moteur de templates

## 📤 Sorties / Exports
- `ListViewSubPanel` — classe (framework/vue) — liste dans sous-panneau
  - `$smartyTemplate` — instance Smarty protégée

## 🔗 Relations clés
- **Appelé par :** framework de sous-panneaux (`SubpanelLayouts`)
- **Appelle :** `ListView`, `Sugar_Smarty`
- **Position dans le flux global :** rendu de la section sous-panneau dans les vues détail

---

## 💡 Points d'attention
- Utilise Smarty contrairement à `ListView` qui utilise XTemplate — transition architecturale visible.
