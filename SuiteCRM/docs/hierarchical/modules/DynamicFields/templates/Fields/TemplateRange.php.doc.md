# Fichier : TemplateRange.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateRange.php`
**Type :** PHP — Template de champ (classe intermediaire avec support plage)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe intermediaire ajoutant le support de la recherche par plage (range search) aux champs numeriques et de date. Sert de base pour `TemplateInt`, `TemplateFloat`, `TemplateDate`, `TemplateDatetimecombo`, `TemplateCurrency`.

## Role technique

Classe `TemplateRange` etendant `TemplateText`. Ajoute probablement des proprietes et methodes pour gerer les criteres de recherche `min`/`max`. La propriete `range_search_option_enabled` dans `FieldViewer` controle l'affichage de l'option.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateRange` | classe | Base pour champs avec recherche par plage |

---

## Relations cles

- **Etend :** `TemplateText`
- **Etendue par :** `TemplateInt`, `TemplateFloat`, `TemplateDate`, `TemplateDatetimecombo`, `TemplateCurrency`
