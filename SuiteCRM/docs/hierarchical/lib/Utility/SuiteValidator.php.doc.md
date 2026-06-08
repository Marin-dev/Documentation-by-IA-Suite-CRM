# SuiteValidator.php

**Chemin :** `lib/Utility/SuiteValidator.php`
**Type :** PHP — Service utilitaire (validation)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Validateur de donnees SuiteCRM. Valide les IDs (UUIDs ou numeriques), les cles, et detecte les champs de pourcentage. Tient compte de la configuration `strict_id_validation` pour appliquer un pattern UUID strict ou non.

## Role technique
Methodes d'instance. `isValidId()` accepte une valeur numerique ou un UUID selon le pattern configure. Pattern strict UUID : `^{?[A-Z0-9]{8}-[A-Z0-9]{4}-...\}?$`. Sinon utilise `get_id_validation_pattern()`. `isPercentageField()` verifie le nom du champ par pattern.

---

## Dependances cles
- `$sugar_config` global — cles `strict_id_validation`, `key_validation_pattern`
- `get_id_validation_pattern()` — fonction globale SuiteCRM

## Exports / Symboles principaux
- `SuiteValidator` — classe
  - `isValidId(?string $id): bool`
  - `isValidKey(?string $key): bool`
  - `isPercentageField(string $fieldname): bool`
  - `getIdValidationPattern(): string`

- **Consommateurs identifies :** INCONNU (vraisemblablement dans l'API V8)

---

## Points d'attention
- `strict_id_validation = true` : pattern UUID strict (case-insensitive).
- `isPercentageField()` detecte les champs contenant `pct`, `percent`, `percentage`, ou exactement `aos_products_quotes_vat`.
