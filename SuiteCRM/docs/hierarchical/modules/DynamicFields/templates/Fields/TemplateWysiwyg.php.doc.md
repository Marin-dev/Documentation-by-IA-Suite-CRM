# Fichier : TemplateWysiwyg.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateWysiwyg.php`
**Type :** PHP — Template de champ (editeur WYSIWYG)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ editeur de texte riche WYSIWYG personnalise. Permet la saisie de contenu HTML formate via un editeur visuel (probablement TinyMCE).

## Role technique

Classe `TemplateWysiwyg` etendant directement `TemplateField`. Type `wysiwyg`. Gere l'integration de l'editeur TinyMCE dans les vues.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateWysiwyg` | classe | Champ editeur WYSIWYG |
| `$type` | propriete | `'wysiwyg'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Instanciee par :** `get_widget('wysiwyg')` dans `FieldCases.php` (INCONNU si presente dans le switch)
