# 📄 LanguageManager.php

**Chemin :** `include/SugarObjects/LanguageManager.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Gestionnaire des fichiers de langue des modules. Crée et met en cache les fichiers de langue pour un module donné en fusionnant les chaînes issues de ses templates SugarObject (Basic, Person, Company, etc.). Utilisé lors du chargement initial ou du repair.

## ⚙️ Rôle technique
Classe statique. `createLanguageFile($module, $templates, $refresh)` fusionne les `$mod_strings` des templates dans le bon ordre de priorité et écrit le fichier résultant dans `cache/modules/{module}/language/{lang}.lang.php`. En mode développeur (`inDeveloperMode()`), le refresh est forcé. Utilise un cache statique `$createdModules` pour éviter les régénérations multiples dans une même requête.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/SugarObjects/translated_prefix.php` — préfixes de traduction (inclus via `require_once __DIR__.'/translated_prefix.php'`)
- **Variables globales lues :** `$mod_strings`, `$current_language`, `$sugar_config['default_language']`

## 📤 Sorties / Exports
- `LanguageManager` — classe statique (framework/langue)
  - `createLanguageFile($module, $templates, $refresh)` — génération/mise en cache du fichier de langue
- **Fichiers produits :** `cache/modules/{module}/language/{lang}.lang.php`

## 🔗 Relations clés
- **Appelé par :** `VardefManager::createVardef()`, processus de repair
- **Appelle :** fonctions de lecture de langue (`return_module_language()`), système de cache
- **Position dans le flux global :** phase de bootstrap des vardefs ; le fichier produit est lu par le système de traduction

---

## 💡 Points d'attention
- Le cache statique `$createdModules` est par requête — en mode developer, le refresh est forcé à chaque appel (ligne 61).
- Si `$current_language` est vide, la langue par défaut de la config est utilisée (ligne 68).
