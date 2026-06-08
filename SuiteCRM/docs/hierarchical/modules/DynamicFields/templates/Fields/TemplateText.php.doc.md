# Fichier : TemplateText.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateText.php`
**Type :** PHP — Template de champ (champ texte court)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ texte court (varchar) personnalise. Gere le rendu de la valeur en vue edition, recherche et detail, avec support de la valeur par defaut et des textes d'aide.

## Role technique

Classe `TemplateText` etendant `TemplateField`. Type `varchar`. Supporte la recherche unifiee (`supports_unified_search = true`). Surcharge `get_xtpl_edit()` (retourne valeur du bean ou valeur par defaut), `get_xtpl_search()` (valeur de `$_REQUEST`) et `get_xtpl_detail()` (valeur du bean).

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateText` | classe | Champ varchar personnalise |
| `$type` | propriete | `'varchar'` |
| `$supports_unified_search` | propriete | `true` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Etendue par :** `TemplateEnum`, `TemplateTextArea`, et plusieurs autres classes Template*
- **Instanciee par :** `get_widget('varchar')` dans `FieldCases.php`
