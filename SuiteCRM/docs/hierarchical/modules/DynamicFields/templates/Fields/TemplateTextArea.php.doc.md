# Fichier : TemplateTextArea.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateTextArea.php`
**Type :** PHP — Template de champ (zone de texte multiligne)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ zone de texte multiligne (textarea) personnalise. Permet la saisie de texte long non formate.

## Role technique

Classe `TemplateTextArea` etendant `TemplateText`. Type `text`. Rendu en `<textarea>` au lieu d'un `<input>`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateTextArea` | classe | Champ textarea |
| `$type` | propriete | `'text'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Instanciee par :** `get_widget('text')` dans `FieldCases.php`
