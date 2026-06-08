# Fichier : TemplateAddress.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateAddress.php`
**Type :** PHP — Template de champ (adresse)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ adresse personnalise (groupe de champs : rue, ville, etat, code postal, pays). Type interne `varchar` bien que logiquement composite.

## Role technique

Classe `TemplateAddress` etendant directement `TemplateField`. Type declare `varchar`. Gere le rendu d'un groupe de champs adresse comme un champ custom unique.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateAddress` | classe | Champ adresse composite |
| `$type` | propriete | `'varchar'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Instanciee par :** `get_widget('address')` dans `FieldCases.php`
