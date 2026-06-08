# 📄 EditView.php

**Chemin :** `include/EditView/EditView.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Ancienne implémentation de la vue d'édition (création/modification d'enregistrement). Cette classe legacy utilise directement les templates XTemplate et Smarty avec un module et un template passés en paramètre.

## ⚙️ Rôle technique
Classe simple sans héritage complexe. Le constructeur accepte un module et un template, et instancie `Sugar_Smarty`. La méthode `process()` applique les variables Smarty et rend le template. Marquée `@deprecated` dans le PHPDoc (ligne 47).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Sugar_Smarty` (instanciée dans le constructeur) — moteur de templates

## 📤 Sorties / Exports
- `EditView` — classe (framework/vue, deprecated) — vue d'édition legacy
  - `__construct($module, $template)` — initialisation
  - `process()` — rendu du template
- **Consommateurs identifiés dans le repo :** modules legacy n'ayant pas migré vers `EditView2`

## 🔗 Relations clés
- **Appelé par :** anciens contrôleurs de modules
- **Appelle :** `Sugar_Smarty`
- **Position dans le flux global :** couche vue legacy ; remplacée par `EditView2`

---

## 💡 Points d'attention
- Marquée `@deprecated` (ligne 47) — ne pas utiliser pour les nouveaux développements.
- **Attention :** ce fichier définit une classe `EditView` qui entre en conflit de nom avec `EditView2.php` qui définit également une classe `EditView` (le nouveau framework). Les deux fichiers ne doivent pas être inclus en même temps.
