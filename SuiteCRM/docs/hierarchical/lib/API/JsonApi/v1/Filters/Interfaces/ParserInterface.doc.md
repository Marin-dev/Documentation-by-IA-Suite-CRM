# 📄 ParserInterface.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/ParserInterface.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Interface pour les parseurs de valeurs de filtres. Définit comment convertir une valeur de filtre brute en SQL.

## ⚙️ Rôle technique
Interface avec une seule méthode : `parseToSQL(mixed $value): string`.

---

## 📤 Sorties / Exports
- `ParserInterface` — interface
  - `parseToSQL(mixed $value): string`
- **Consommateurs identifiés :** INCONNU (à vérifier dans `lib/API/v8/`)

## 🔗 Relations clés
- **Implémenté par :** INCONNU
- **Lié à :** `HasParserInterface` (qui peut référencer un parseur)

---

## 💡 Points d'attention
- Aucune implémentation concrète trouvée dans le périmètre analysé.
