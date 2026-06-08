# 📄 SugarRegistry.php

**Chemin :** `include/SugarObjects/SugarRegistry.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-06-02

---

## 🎯 Rôle fonctionnel
Registre global nommé permettant de stocker et récupérer des objets ou valeurs arbitraires par clé, sans passer par des variables globales. Utilisé comme conteneur léger d'injection de dépendances ou de partage d'état entre composants.

## ⚙️ Rôle technique
Implémente le pattern Registry avec instances multiples nommées (`$_instances`). Chaque instance est un dictionnaire clé/valeur accessible via `__get()` et `__set()` (propriétés magiques). `getInstance($name)` retourne ou crée une instance nommée.

---

## 📥 Entrées / Dépendances
- **Imports principaux :** aucun

## 📤 Sorties / Exports
- `SugarRegistry` — classe (pattern Registry)
  - `getInstance($name = 'default')` — instance nommée du registre
  - `__get($key)` / `__set($key, $value)` — lecture/écriture dynamique

## 🔗 Relations clés
- **Appelé par :** INCONNU — usage dispersé dans le codebase
- **Appelle :** rien
- **Position dans le flux global :** service transversal de partage d'état

---

## 💡 Points d'attention
- `__get()` retourne `null` si la clé n'existe pas (ligne 68) — pas d'exception — les consommateurs doivent vérifier la valeur.
- Les instances multiples (`getInstance($name)`) permettent d'isoler des registres par contexte (ex: 'default', 'test').
