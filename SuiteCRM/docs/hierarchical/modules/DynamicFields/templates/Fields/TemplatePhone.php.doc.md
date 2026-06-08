# Fichier : TemplatePhone.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplatePhone.php`
**Type :** PHP — Template de champ (telephone)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ telephone personnalise. Etend le champ texte avec les specificites d'affichage et de validation d'un numero de telephone.

## Role technique

Classe `TemplatePhone` etendant `TemplateText`. Type `phone`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplatePhone` | classe | Champ telephone |
| `$type` | propriete | `'phone'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Instanciee par :** `get_widget('phone')` dans `FieldCases.php`
