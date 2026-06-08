# Fichier : TemplateParentType.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateParentType.php`
**Type :** PHP — Template de champ (type parent)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente le champ stockant le type du module parent dans une relation parent polymorphique (complement de `TemplateParent`). Stocke le nom du module parent (ex: `'Accounts'`, `'Contacts'`).

## Role technique

Classe `TemplateParentType` etendant `TemplateText`. Type `parent_type`. Champ technique complementaire de `TemplateParent`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateParentType` | classe | Type du module parent |
| `$type` | propriete | `'parent_type'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Complementaire de :** `TemplateParent`
