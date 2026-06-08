# Fichier : TemplateEnum.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateEnum.php`
**Type :** PHP — Template de champ (liste deroulante)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ liste deroulante (enum) personnalise. Gere la definition des options de la liste (via `$ext1`), les dependances entre champs (visibility_grid, trigger/action), et le support de la recherche unifiee.

## Role technique

Classe `TemplateEnum` etendant `TemplateText`. Type `enum`. Surcharge `populateFromPost()` pour decoder `visibility_grid` (JSON) et construire l'objet de dependance a partir des paires trigger/action. Supporte les dependances de visibilite inter-champs via `$dependency`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateEnum` | classe | Champ liste deroulante |
| `$type` | propriete | `'enum'` |
| `$ext1` | propriete | Cle de la liste d'options (app_list_strings) |
| `$dependency` | propriete | Regles de dependance entre champs |
| `$visibility_grid` | propriete | Grille de visibilite JSON |
| `$supports_unified_search` | propriete | `true` |

## Dependances principales

| Import | Role |
|---|---|
| `include/utils/array_utils.php` | Utilitaires tableaux |

---

## Relations cles

- **Etend :** `TemplateText`
- **Etendue par :** `TemplateMultiEnum`, `TemplateDynamicenum`, `TemplateRadioEnum`
- **Instanciee par :** `get_widget('enum')` dans `FieldCases.php`

---

## Points d'attention

- Les dependances trigger/action sont construites par paires a partir de `$_REQUEST['trigger'][]` et `$_REQUEST['action'][]` (tableaux paralleles) — toute modification du formulaire Studio doit maintenir cette structure.
- `$visibility_grid` est decode depuis JSON apres `html_entity_decode` — format depend du front-end Studio.
