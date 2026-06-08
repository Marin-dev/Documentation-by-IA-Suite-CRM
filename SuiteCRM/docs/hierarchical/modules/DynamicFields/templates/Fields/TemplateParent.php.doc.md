# Fichier : TemplateParent.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateParent.php`
**Type :** PHP — Template de champ (parent polymorphique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ de relation parent polymorphique (un enregistrement peut etre lie a differents types de modules parents). Utilise dans les modules comme les Appels, Reunions pour lier a un Compte, un Contact, etc.

## Role technique

Classe `TemplateParent` etendant `TemplateEnum`. Type `parent`. La liste des types parents est stockee dans `ext1` (liste d'options).

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateParent` | classe | Champ parent polymorphique |
| `$type` | propriete | `'parent'` |

---

## Relations cles

- **Etend :** `TemplateEnum`
- **Instanciee par :** `get_widget('parent')` dans `FieldCases.php`
