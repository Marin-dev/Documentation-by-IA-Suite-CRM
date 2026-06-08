# 📄 Basic.php

**Chemin :** `include/SugarObjects/templates/basic/Basic.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Template de base pour tous les modules SuiteCRM. Classe parente de toute entité métier standard. Hérite de `SugarBean` et fournit le comportement commun (opt-in GDPR, enregistrement/chargement). Tous les modules héritent de ce template directement ou via Person, Company, Issue, Sale, File.

## ⚙️ Rôle technique
Hérite de `SugarBean`. Ajoute la logique d'opt-in (`$doNotDisplayOptInTickForModule`) pour exclure certains modules (Users, Employees) de l'affichage de la case GDPR. Le constructeur appelle simplement `parent::__construct()`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** `SugarBean` (héritée, via autoloader)

## 📤 Sorties / Exports
- `Basic` — classe (template/modèle) — base de tous les enregistrements SuiteCRM
  - `$doNotDisplayOptInTickForModule` — liste des modules sans case opt-in (statique)
- **Consommateurs identifiés dans le repo :**
  - `include/SugarObjects/templates/person/Person.php`
  - `include/SugarObjects/templates/company/Company.php`
  - `include/SugarObjects/templates/issue/Issue.php`
  - `include/SugarObjects/templates/sale/Sale.php`
  - `include/SugarObjects/templates/file/File.php`

## 🔗 Relations clés
- **Appelé par :** tous les modules via leur classe principale
- **Appelle :** `SugarBean::__construct()`
- **Position dans le flux global :** sommet de la hiérarchie des beans métier

---

## 💡 Points d'attention
- Toute modification de cette classe impacte potentiellement tous les modules du CRM.
- `$doNotDisplayOptInTickForModule` est statique — partagé entre toutes les instances.
