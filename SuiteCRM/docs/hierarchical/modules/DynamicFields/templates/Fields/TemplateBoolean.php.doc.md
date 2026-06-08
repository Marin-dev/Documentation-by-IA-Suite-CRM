# Fichier : TemplateBoolean.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateBoolean.php`
**Type :** PHP — Template de champ (booleen/case a cocher)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ case a cocher (booleen) personnalise. Gere la logique de rendu de l'etat coche/decoche en tenant compte de multiples representations de la valeur vraie (`'1'`, `'on'`, `'yes'`, `'true'`).

## Role technique

Classe `TemplateBoolean` etendant `TemplateField`. Type `bool`, valeur par defaut `'0'`. La methode `get_xtpl_edit()` retourne un tableau avec la cle `{name}_checked = 'checked'` si la valeur est vraie. La comparaison accepte les formes `'1'`, `'on'`, `'yes'`, `'true'`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateBoolean` | classe | Champ booleen |
| `$type` | propriete | `'bool'` |
| `$default_value` | propriete | `'0'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Instanciee par :** `get_widget('bool')` dans `FieldCases.php`
