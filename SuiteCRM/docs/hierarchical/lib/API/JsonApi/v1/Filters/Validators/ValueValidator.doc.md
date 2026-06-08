# 📄 ValueValidator.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Validators/ValueValidator.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Validateur de valeurs d'opérandes de filtre. Interdit les caractères réservés qui pourraient créer des ambiguïtés dans la syntaxe filtre JSON API ou des injections SQL.

## ⚙️ Rôle technique
Implémente `ValidatorInterface`. Maintient une liste statique `$BANNED_RESERVED_CHARACTERS` (ex: `+`, `!`, `"`, `#`, `$`, etc.). `isValid(string $value)` retourne `false` si la valeur contient l'un de ces caractères.

Caractères **autorisés** (commentés dans la liste) : `,`, `[`, `]`, `:`, `;`, `` ` ``, espace.

---

## 📤 Sorties / Exports
- `ValueValidator` — classe (validateur)
  - `isValid(string $value): bool`
- **Consommateurs identifiés :** INCONNU (à vérifier dans `FilterParser` ou `FilterInterpreter`)

---

## 💡 Points d'attention
- La liste des caractères interdits est statique et codée en dur — non configurable.
- Les caractères autorisés (en commentaire) incluent `,` et `[` qui sont utilisés dans la syntaxe de filtre — cohérent avec le design.
