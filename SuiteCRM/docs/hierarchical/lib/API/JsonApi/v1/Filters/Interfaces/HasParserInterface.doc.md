# 📄 HasParserInterface.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/HasParserInterface.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface optionnelle pour les opérateurs pouvant déléguer la conversion de valeur à un `ParserInterface`. Permet l'extensibilité du système de filtres avec des parseurs personnalisés.

## ⚙️ Rôle technique
Interface avec deux méthodes : `hasParser(): bool` (indique si un parseur est associé) et `getParser(): string` (retourne le parseur à utiliser).

---

## 📤 Sorties / Exports
- `HasParserInterface` — interface
  - `hasParser(): bool`
  - `getParser(): string`
- **Consommateurs identifiés :** INCONNU (interface disponible mais usage non trouvé dans le périmètre analysé)

## 🔗 Relations clés
- **Implémenté par :** INCONNU
- **Utilisé par :** INCONNU

---

## 💡 Points d'attention
- Interface apparemment non utilisée dans le périmètre `lib/API/JsonApi/v1` analysé — vérifier si des classes dans `lib/API/v8/` l'implémentent.
