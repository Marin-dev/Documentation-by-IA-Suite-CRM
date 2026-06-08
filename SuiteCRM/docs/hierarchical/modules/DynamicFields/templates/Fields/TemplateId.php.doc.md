# Fichier : TemplateId.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateId.php`
**Type :** PHP — Template de champ (ID)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ ID personnalise (UUID/GUID). Sert de classe parente pour `TemplateCurrencyId`. Stocke un identifiant de reference vers un autre enregistrement.

## Role technique

Classe `TemplateId` etendant `TemplateField`. Type `id`. Champ de reference technique.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateId` | classe | Champ ID |
| `$type` | propriete | `'id'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Etendue par :** `TemplateCurrencyId`
- **Instanciee par :** `get_widget('id')` dans `FieldCases.php`
