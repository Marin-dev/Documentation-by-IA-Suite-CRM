# Fichier : TemplateIFrame.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateIFrame.php`
**Type :** PHP — Template de champ (IFrame)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ IFrame personnalise. Permet d'afficher une URL externe dans une iframe dans les vues d'un module. La valeur stockee est l'URL de l'iframe.

## Role technique

Classe `TemplateIFrame` etendant `TemplateURL`. Type `iframe`. Herite la logique de gestion d'URL de `TemplateURL`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateIFrame` | classe | Champ IFrame |
| `$type` | propriete | `'iframe'` |

---

## Relations cles

- **Etend :** `TemplateURL`
- **Instanciee par :** `get_widget('iframe')` dans `FieldCases.php`
