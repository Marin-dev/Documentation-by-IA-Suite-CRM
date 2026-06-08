# 📄 jsLanguage.php

**Chemin :** `include/language/jsLanguage.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Génère et met en cache des versions JavaScript des fichiers de langue pour le frontend. Encode les chaînes `$app_strings` et `$app_list_strings` en JSON et les injecte dans l'objet `SUGAR.language` côté client, permettant aux scripts JS d'accéder aux traductions.

## ⚙️ Rôle technique
Classe `jsLanguage` avec méthodes statiques. `createAppStringsCache($lang)` génère le cache pour les chaînes applicatives globales. Le cache est écrit dans `cache/include/language/` via `write_array_to_file()`. Utilise `getJSONobj()` pour l'encodage JSON des chaînes.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun (`require_once` dans `getJSLanguage.php`)
- **Fonctions appelées :** `return_application_language()`, `return_app_list_strings_language()`, `getJSONobj()`, `write_array_to_file()`

## 📤 Sorties / Exports
- `jsLanguage` — classe (helper/cache)
  - `createAppStringsCache($lang)` — génération cache JS global
  - Méthodes pour les modules (INCONNU — non lues en entier)
- **Fichiers produits :** `cache/include/language/{lang}.js`
- **Output JS :** `SUGAR.language.setLanguage('app_strings', {...});`

## 🔗 Relations clés
- **Appelé par :** `getJSLanguage.php`, processus de repair
- **Appelle :** fonctions de lecture de langue, système de cache
- **Position dans le flux global :** génération du bundle JS de traductions consommé par le frontend

---

## 💡 Points d'attention
- Le cache JS doit être regénéré après modification des fichiers de langue (Admin > Quick Repair & Rebuild).
- L'encodage JSON des chaînes peut poser des problèmes avec certains caractères spéciaux dans les langues non-latin.
