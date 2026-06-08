# Fichier : TemplateDecimal.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateDecimal.php`
**Type :** PHP — Template de champ (decimal)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ decimal personnalise avec precision configurable. Surcharge la methode de type DB pour utiliser le type `decimal(len, precision)`.

## Role technique

Classe `TemplateDecimal` etendant `TemplateFloat`. Type `decimal`. Surcharge `get_db_type()` pour retourner `decimal(len, precision)` via le template DB du gestionnaire (`decimal_tpl`). La precision par defaut est 6 si non specificiee.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateDecimal` | classe | Champ decimal |
| `$type` | propriete | `'decimal'` |
| `get_db_type()` | methode | Retourne le type SQL decimal(len, precision) |

---

## Relations cles

- **Etend :** `TemplateFloat`
- **Instanciee par :** `get_widget('decimal')` dans `FieldCases.php`
