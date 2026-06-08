# 📄 ByPreMadeFilterInterpreter.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/ByPreMadeFilterInterpreter.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface pour les interpréteurs de filtres "pré-définis" (ex: `Today`). Ces filtres sont des raccourcis nommés qui génèrent des clauses SQL sans nécessiter de saisie de valeur par l'utilisateur.

## ⚙️ Rôle technique
Interface avec deux méthodes : `hasByPreMadeFilter(string $name): bool` (vérifie si cet interpréteur reconnaît le filtre nommé) et `getByPreMadeFilter(): string` (retourne la clause SQL correspondante).

---

## 📤 Sorties / Exports
- `ByPreMadeFilterInterpreter` — interface
  - `hasByPreMadeFilter(string $name): bool`
  - `getByPreMadeFilter(): string`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Filters/Interpreters/ByPreMadeFilters/Today.php` (implémentation)
  - `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php` (utilisation)

## 🔗 Relations clés
- **Implémenté par :** `Today`
- **Utilisé par :** `FilterInterpreter`

---

## 💡 Points d'attention
- RAS.
