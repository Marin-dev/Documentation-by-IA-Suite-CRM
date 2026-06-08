# Fichier : TemplateRelatedTextField.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateRelatedTextField.php`
**Type :** PHP — Template de champ (champ lie/relate)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ de relation (relate) personnalise permettant de lier un enregistrement a un autre module. Affiche un champ texte avec selecteur popup pour choisir l'enregistrement lie.

## Role technique

Classe `TemplateRelatedTextField` etendant `TemplateText`. Type `relate`. Les metadonnees de la relation (module cible, champ id, champ nom) sont stockees dans `ext1`/`ext2`/`ext3`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateRelatedTextField` | classe | Champ relation |
| `$type` | propriete | `'relate'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Instanciee par :** `get_widget('relate')` dans `FieldCases.php`

---

## Points d'attention

- `$ext1`/`$ext2`/`$ext3` stockent les metadonnees de la relation (module, champ id, champ affiche) — semantique specifique a ce type de champ.
