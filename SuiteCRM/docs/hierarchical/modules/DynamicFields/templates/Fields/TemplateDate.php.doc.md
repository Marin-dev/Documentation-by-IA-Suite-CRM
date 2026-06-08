# Fichier : TemplateDate.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateDate.php`
**Type :** PHP — Template de champ (date)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ date personnalise. Propose une liste de valeurs par defaut relatives (hier, aujourd'hui, demain, semaine prochaine, etc.) en plus de la saisie libre.

## Role technique

Classe `TemplateDate` etendant `TemplateRange`. Type `date`. Le constructeur initialise `$dateStrings` : tableau associatif `label => expression_date_relative` (format PHP strtotime ou expressions speciales). La chaine `'first day of next month'` necessite une gestion particuliere dans `SugarBean->populateDefaultValues` (commentaire ligne 68).

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateDate` | classe | Champ date |
| `$type` | propriete | `'date'` |
| `$dateStrings` | propriete | Tableau label => expression date relative |

---

## Relations cles

- **Etend :** `TemplateRange`
- **Instanciee par :** `get_widget('date')` dans `FieldCases.php`

---

## Points d'attention

- `'first day of next month'` est une expression non-GNU — `SugarBean::populateDefaultValues` doit la traiter specialement, sinon elle donne 1969.
