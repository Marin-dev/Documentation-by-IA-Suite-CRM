# 📄 Issue.php

**Chemin :** `include/SugarObjects/templates/issue/Issue.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template pour les modules représentant des tickets ou problèmes (Cases, Bugs). Fournit la structure de base pour les entités de type "problème à résoudre" avec statut, priorité et affectation.

## ⚙️ Rôle technique
Hérite de `Basic`. Corps minimal — le constructeur appelle uniquement `parent::__construct()`. Les champs spécifiques (statut, priorité, etc.) sont définis dans les vardefs du template (`include/SugarObjects/templates/issue/vardefs.php`), pas dans la classe PHP.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/templates/basic/Basic.php` — classe parente

## 📤 Sorties / Exports
- `Issue` — classe (template/modèle) — entité ticket/problème
- **Consommateurs identifiés dans le repo :**
  - `modules/Cases/Case.php`
  - `modules/Bugs/Bug.php`

## 🔗 Relations clés
- **Appelé par :** modules Cases, Bugs
- **Appelle :** `Basic::__construct()`
- **Position dans le flux global :** niveau 2 de la hiérarchie beans (Basic > Issue > module)

---

## 💡 Points d'attention
- Classe quasi-vide — toute la logique métier est dans les vardefs ou les classes fils.
