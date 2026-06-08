# 📄 FilterValidator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Validators/FilterValidator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Validateur de valeurs de filtre JSON API. Accepte toujours les valeurs (implémentation partielle).

## ⚙️ Rôle technique
Implémente `ValidatorInterface`. `isValid(string $fieldKey)` retourne toujours `true` — la validation est commentée (un switch sur les cas valides était prévu selon les commentaires internes).

---

## 📤 Sorties / Exports
- `FilterValidator` — classe (validateur)
  - `isValid(string $fieldKey): bool` → toujours `true`
- **Consommateurs identifiés :**
  - `FilterParser`

---

## 💡 Points d'attention
- **Dette technique** : la méthode retourne toujours `true` — aucune validation n'est effectuée. La docstring liste les cas valides mais ils ne sont pas vérifiés dans le code.
