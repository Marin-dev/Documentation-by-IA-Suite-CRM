# Fichier : AccountsJjwg_MapsLogicHook.php

**Chemin :** `modules/Accounts/AccountsJjwg_MapsLogicHook.php`
**Type :** `PHP`
**Categorie :** logic hook
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook qui synchronise les informations de geocodage (coordonnees GPS) d'un compte avec le module de cartographie `jjwg_Maps`. Declenche egalement la mise a jour du geocodage sur les enregistrements lies (Projets, Opportunites, Cases, Reunions) apres chaque sauvegarde de compte.

## Role technique

Classe `AccountsJjwg_MapsLogicHook` sans heritage. Recupere le module `jjwg_Maps` au constructeur via `get_module_info()`. Chaque methode correspond a un evenement de logic hook (before_save, after_save, after_relationship_add/delete). La mise a jour ne s'effectue que si `logic_hooks_enabled` est actif dans les parametres du module.

---

## Dependances cles

| Dependance | Role |
|---|---|
| `jjwg_Maps` (module) | Fournit `updateGeocodeInfo()` et les settings de geocodage |
| `modules/Project/Project.php` | Charge les projets lies (require_once dans la methode) |
| `modules/Opportunities/Opportunity.php` | Charge les opportunites liees |
| `modules/Cases/Case.php` | Charge les cases liees |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AccountsJjwg_MapsLogicHook` | classe | Hook principal |
| `updateGeocodeInfo($bean, $event, $args)` | methode | before_save : met a jour les coordonnees du compte |
| `updateRelatedProjectGeocodeInfo($bean, $event, $args)` | methode | after_save : propage le geocodage aux projets lies |
| `updateRelatedOpportunitiesGeocodeInfo($bean, $event, $args)` | methode | after_save : propage aux opportunites liees |
| `updateRelatedCasesGeocodeInfo($bean, $event, $args)` | methode | after_save : propage aux cases liees |
| `updateRelatedMeetingsGeocodeInfo($bean, $event, $args)` | methode | after_save : propage aux reunions liees |
| `addRelationship($bean, $event, $args)` | methode | after_relationship_add : geocode l'entite nouvellement liee |
| `deleteRelationship($bean, $event, $args)` | methode | after_relationship_delete : recalcule le geocodage |

## Relations cles

- **Appele par :** Framework SuiteCRM logic hooks (enregistrement dans `logic_hooks.php` du module)
- **Appelle :** `jjwg_Maps->updateGeocodeInfo()`, `bean->save(false)`
- **Position dans le flux :** apres chaque sauvegarde d'un Account, propage les coordonnees GPS aux entites liees

---

## Points d'attention

- Toutes les operations sont conditionnees par `$this->jjwg_Maps->settings['logic_hooks_enabled']` : si Maps est desactive, aucune action n'est executee.
- Les methodes `updateRelated*` sauvegardent le bean lie uniquement si le champ `jjwg_maps_address_c` a change (ligne 37 et equivalents) pour eviter les sauvegardes inutiles.
- Le commentaire en tete indique `custom/modules/Accounts/AccountsJjwg_MapsLogicHook.php` : anomalie de chemin (fichier dans core mais reference un chemin custom).
