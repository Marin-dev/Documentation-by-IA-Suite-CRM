# 📄 ByIdFilterInterpreter.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/ByIdFilterInterpreter.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface définissant le contrat pour les interpréteurs de filtres par identifiant (filtre `[id]`). Permet de générer une clause SQL `WHERE id IN (...)` depuis une structure de filtre JSON API.

## ⚙️ Rôle technique
Interface avec une seule méthode : `getByIdFilter(array $filterStructure): string`. Le tableau `$filterStructure` doit contenir la clé `[id]` avec un tableau d'identifiants.

---

## 📤 Sorties / Exports
- `ByIdFilterInterpreter` — interface
  - `getByIdFilter(array $filterStructure): string`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Filters/Interpreters/ByIdFilters/ByIdFilter.php` (implémentation)
  - `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php` (utilisation)

## 🔗 Relations clés
- **Implémenté par :** `ByIdFilter`
- **Utilisé par :** `FilterInterpreter`

---

## 💡 Points d'attention
- RAS.
