# Fichier : OpportunitiesJjwg_MapsLogicHook.php

**Chemin :** `modules/Opportunities/OpportunitiesJjwg_MapsLogicHook.php`
**Type :** `PHP`
**Categorie :** logic hook
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook de geocodage pour le module Opportunities. Synchronise les coordonnees GPS d'une opportunite avec `jjwg_Maps`. Propage le geocodage aux projets et reunions lies.

## Role technique

Classe `OpportunitiesJjwg_MapsLogicHook`. Meme pattern que `AccountsJjwg_MapsLogicHook` sans propagation aux cases. Cinq methodes pour les evenements `before_save`, `after_save`, `after_relationship_add/delete`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `updateGeocodeInfo($bean, $event, $args)` | methode | before_save : geocode l'opportunite |
| `updateRelatedProjectGeocodeInfo($bean, $event, $args)` | methode | after_save : projets lies |
| `updateRelatedMeetingsGeocodeInfo($bean, $event, $args)` | methode | after_save : reunions liees |
| `addRelationship($bean, $event, $args)` | methode | after_relationship_add |
| `deleteRelationship($bean, $event, $args)` | methode | after_relationship_delete |

## Points d'attention

- Identique a `AccountsJjwg_MapsLogicHook` sans les methodes pour Cases.
- Toutes les operations conditionnees par `logic_hooks_enabled`.
