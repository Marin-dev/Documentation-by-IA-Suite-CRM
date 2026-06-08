# 📄 VardefManager.php

**Chemin :** `include/SugarObjects/VardefManager.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Gestionnaire central des définitions de variables (vardefs) des modules SuiteCRM. Charge les vardefs d'un module depuis ses templates de base (Basic, Person, Company, etc.) et les vardefs personnalisés, les fusionne dans le dictionnaire global `$dictionary`.

## ⚙️ Rôle technique
Classe statique. La méthode principale `createVardef($module, $object, $templates, $object_name)` itère sur les templates dans l'ordre inverse de priorité (du plus bas au plus élevé). Appelle `LanguageManager::createLanguageFile()` pour synchroniser les fichiers de langue. Gère les modules désactivés (`$custom_disabled_modules`) et les champs de type `link` (`$linkFields`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `modules/TableDictionary.php` — dictionnaire global des tables
  - `include/SugarObjects/LanguageManager.php` — gestion des fichiers de langue (appelé en fin de `createVardef`)
- **Variables globales :** `$dictionary` (dictionnaire des vardefs)

## 📤 Sorties / Exports
- `VardefManager` — classe statique (framework/vardefs)
  - `createVardef($module, $object, $templates, $object_name)` — chargement et fusion des vardefs
  - `$custom_disabled_modules` — modules sans vardefs custom
  - `$linkFields` — cache des champs de type link
- **Consommateurs identifiés dans le repo :** `modules/*/vardefs.php` (tous les modules)

## 🔗 Relations clés
- **Appelé par :** `vardefs.php` de chaque module au chargement
- **Appelle :** `LanguageManager::createLanguageFile()`, templates vardefs (`include/SugarObjects/templates/*/vardefs.php`)
- **Position dans le flux global :** phase de bootstrap/repair ; alimente `$dictionary` utilisé par `SugarBean`

---

## 💡 Points d'attention
- Les templates sont traités en ordre inverse (`array_reverse` ligne 61) — le template de plus haute priorité (dernier dans le tableau) surcharge les précédents.
- Les vardefs custom sont chargés depuis `custom/modules/{module}/Ext/Vardefs/` — respecter cette convention pour les personnalisations.
- `$custom_disabled_modules` permet de désactiver le chargement des custom vardefs pour des modules spécifiques (ex: modules dont la personnalisation est interdite).
