# Fichier : LeadsVarDefHandler.php

**Chemin :** `modules/Leads/LeadsVarDefHandler.php`
**Type :** `PHP`
**Categorie :** helper (vardef handler)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge du gestionnaire de vardefs pour le module Leads. Filtre les champs legacy `oldcalls` et `oldmeetings` (relations pre-SugarCRM 5.1) lors de la construction des tableaux de filtrage de relations.

## Role technique

Classe `LeadsVarDefHandler` heritant de `VarDefHandler`. Surcharge `get_vardef_array()` : quand `$this->meta_array_name == 'rel_filter'`, supprime les cles `oldcalls` et `oldmeetings` du tableau retourne.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `VarDefHandler` | `include/VarDefHandler/VarDefHandler.php` | Classe parente |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadsVarDefHandler` | classe | Gestionnaire de vardefs filtre pour Leads |
| `get_vardef_array()` | methode | Surcharge : filtre les relations legacy oldcalls/oldmeetings |

## Points d'attention

- Filtre actif uniquement quand `meta_array_name == 'rel_filter'` : pas d'impact sur les autres usages.
- `oldcalls` et `oldmeetings` sont des artefacts de migration pre-5.1 : ils subsistent dans le schema mais ne doivent pas apparaitre dans les UI de filtre.
