# Fichier : TemplateMultiEnum.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateMultiEnum.php`
**Type :** PHP — Template de champ (multi-selection)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ de selection multiple (plusieurs valeurs d'une liste). Les valeurs selectionnees sont stockees en tant que chaine serialisee (format `^val1^,^val2^`) dans un champ de type `text`.

## Role technique

Classe `TemplateMultiEnum` etendant `TemplateEnum`. Type stocke : `text` (malgre le type logique multienum). Herite la logique enum avec dependances et visibility_grid.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateMultiEnum` | classe | Champ multi-selection |
| `$type` | propriete | `'text'` (stockage DB) |

---

## Relations cles

- **Etend :** `TemplateEnum`
- **Instanciee par :** `get_widget('multienum')` dans `FieldCases.php`

---

## Points d'attention

- `$type = 'text'` alors que logiquement c'est un multienum — le type DB est text mais le type logique differe. Peut causer de la confusion dans les vardefs.
