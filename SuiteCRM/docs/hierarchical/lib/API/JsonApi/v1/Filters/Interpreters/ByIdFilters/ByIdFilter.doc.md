# 📄 ByIdFilter.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interpreters/ByIdFilters/ByIdFilter.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Implémente le filtre par liste d'identifiants pour l'API JSON. Convertit une liste d'IDs transmise dans le filtre `[id]` en une clause SQL `id IN (...)`.

## ⚙️ Rôle technique
Implémente `ByIdFilterInterpreter`. Le constructeur reçoit le `ContainerInterface`. La méthode `getByIdFilter(array $filterStructure)` extrait les IDs de `$filterStructure['[id]']`, les échappe via `DBManager::quote()`, et retourne `id IN ("id1","id2",...)`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Container\ContainerInterface`
  - `SuiteCRM\API\JsonApi\v1\Filters\Interfaces\ByIdFilterInterpreter`
  - `SuiteCRM\Exception\Exception`
  - `DatabaseManager` (depuis le container) — pour l'échappement SQL

## 📤 Sorties / Exports
- `ByIdFilter` — classe (service)
  - `getByIdFilter(array $filterStructure): string` — clause SQL `id IN (...)`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php`

## 🔗 Relations clés
- **Appelé par :** `FilterInterpreter::getFilterById()`
- **Appelle :** `DatabaseManager::quote()`, `ContainerInterface::get('DatabaseManager')`

---

## 💡 Points d'attention
- Lève `Exception` si `$filterStructure` est vide.
- Les IDs vides dans la liste sont silencieusement ignorés (`continue`).
- L'injection du `DBManager` via le container assure la testabilité mais crée une dépendance à la BD à l'exécution.
