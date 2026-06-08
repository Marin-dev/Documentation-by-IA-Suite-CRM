# Fichier : TemplateFloat.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateFloat.php`
**Type :** PHP — Template de champ (nombre flottant)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ nombre a virgule flottante personnalise. Sert de classe parente pour `TemplateDecimal` et `TemplateCurrency` via `TemplateRange`.

## Role technique

Classe `TemplateFloat` etendant `TemplateRange`. Type `float`. Probablement des methodes de formatage et de validation numerique.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateFloat` | classe | Champ flottant |
| `$type` | propriete | `'float'` |

---

## Relations cles

- **Etend :** `TemplateRange`
- **Etendue par :** `TemplateDecimal`
- **Instanciee par :** `get_widget('float')` dans `FieldCases.php`
