# Fichier : TemplateDatetimecombo.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateDatetimecombo.php`
**Type :** PHP — Template de champ (date+heure)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ date et heure combine (datetimecombo) personnalise. Identique a `TemplateDate` dans sa structure mais pour le type datetime avec selecteur d'heure.

## Role technique

Classe `TemplateDatetimecombo` etendant `TemplateRange`. Type `datetimecombo`. Meme logique de `$dateStrings` que `TemplateDate` avec les expressions de date relatives.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateDatetimecombo` | classe | Champ date+heure |
| `$type` | propriete | `'datetimecombo'` |

---

## Relations cles

- **Etend :** `TemplateRange`
- **Instanciee par :** `get_widget('datetime')` ou `get_widget('datetimecombo')` dans `FieldCases.php`
