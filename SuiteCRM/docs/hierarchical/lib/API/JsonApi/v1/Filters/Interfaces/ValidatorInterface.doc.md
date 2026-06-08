# 📄 ValidatorInterface.php

**Chemin :** `lib/API/JsonApi/v1/Filters/Interfaces/ValidatorInterface.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrat pour tous les validateurs du système de filtres JSON API. Définit une interface uniforme pour valider des blocs de filtre, des champs, des opérateurs ou des valeurs.

## ⚙️ Rôle technique
Interface avec une seule méthode : `isValid(mixed $block): bool`.

---

## 📤 Sorties / Exports
- `ValidatorInterface` — interface
  - `isValid(mixed $block): bool`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Filters/Validators/FieldValidator.php`
  - `lib/API/JsonApi/v1/Filters/Validators/FilterValidator.php`
  - `lib/API/JsonApi/v1/Filters/Validators/OperatorValidator.php`
  - `lib/API/JsonApi/v1/Filters/Validators/SpecialOperatorValidator.php`
  - `lib/API/JsonApi/v1/Filters/Validators/ValueValidator.php`

## 🔗 Relations clés
- **Implémenté par :** toutes les classes `*Validator` du dossier `Filters/Validators/`

---

## 💡 Points d'attention
- RAS.
