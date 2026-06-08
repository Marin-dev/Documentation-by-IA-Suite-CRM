# Fichier : TemplateInt.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateInt.php`
**Type :** PHP — Template de champ (entier)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ entier personnalise. Supporte la recherche par plage (minimum/maximum) via `TemplateRange`.

## Role technique

Classe `TemplateInt` etendant `TemplateRange`. Type `int`. Herite les fonctionnalites de recherche par intervalle.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateInt` | classe | Champ entier |
| `$type` | propriete | `'int'` |

---

## Relations cles

- **Etend :** `TemplateRange`
- **Instanciee par :** `get_widget('int')` dans `FieldCases.php`
