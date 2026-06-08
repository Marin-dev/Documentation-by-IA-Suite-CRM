# 📄 SugarConfig.php

**Chemin :** `include/SugarObjects/SugarConfig.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Gestionnaire de configuration applicative. Fournit un accès unifié et mis en cache à la configuration de SuiteCRM stockée dans `$GLOBALS['sugar_config']`. Utilisé dans tout le CRM pour lire les paramètres de configuration (base de données, langue, thème, limites, etc.).

## ⚙️ Rôle technique
Singleton (pattern via variable statique dans `getInstance()`). Utilise `SugarArray::staticGet()` pour naviguer dans la configuration imbriquée par clé pointée. Met en cache les valeurs lues dans `$_cached_values` pour éviter les accès répétés au tableau global. `clearCache()` permet de forcer le rechargement après modification de la configuration.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `include/utils/array_utils.php` — `SugarArray::staticGet()` (chargé à la demande)
- **Variables globales lues :** `$GLOBALS['sugar_config']`

## 📤 Sorties / Exports
- `SugarConfig` — classe (singleton/config) — accès à la configuration
  - `getInstance()` — retourne l'instance singleton
  - `get($key, $default)` — lecture d'une clé de config avec valeur par défaut
  - `clearCache($key)` — invalidation du cache (clé ou total)
- **Consommateurs identifiés dans le repo :** utilisé dans l'ensemble du codebase

## 🔗 Relations clés
- **Appelé par :** tout le codebase (contrôleurs, services, vues)
- **Appelle :** `SugarArray`, `$GLOBALS['sugar_config']`
- **Position dans le flux global :** service transversal, disponible dès le bootstrap

---

## 💡 Points d'attention
- Le cache n'est pas invalidé automatiquement si `$GLOBALS['sugar_config']` est modifié en dehors de `SugarConfig` — utiliser `clearCache()` après modification.
- Singleton à portée de requête HTTP — pas de persistance entre requêtes.
