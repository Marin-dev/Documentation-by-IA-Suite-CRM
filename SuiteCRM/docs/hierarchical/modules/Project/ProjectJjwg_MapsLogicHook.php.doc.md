# Fichier : ProjectJjwg_MapsLogicHook.php

**Chemin :** `modules/Project/ProjectJjwg_MapsLogicHook.php`
**Type :** PHP - Logic Hook (integration cartographie)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Logic hook d'integration avec le module de cartographie `jjwg_Maps` pour les projets. Met a jour les coordonnees de geocodage du projet et de ses reunions liees lors de la sauvegarde, et gere les changements de relations.

## Role technique

Classe avec quatre methodes : `updateGeocodeInfo()` (before_save), `updateRelatedMeetingsGeocodeInfo()` (after_save), `addRelationship()` (after_relationship_add), `deleteRelationship()` (after_relationship_delete). Toutes les methodes verifient `logic_hooks_enabled` avant d'agir. Module `jjwg_Maps` charge via `get_module_info()` dans le constructeur.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `jjwg_Maps` (module) | Acces aux methodes de geocodage |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `ProjectJjwg_MapsLogicHook` | Classe | Logic hook geocodage projets |
| `updateGeocodeInfo()` | Methode | Geocodage avant sauvegarde |
| `updateRelatedMeetingsGeocodeInfo()` | Methode | Geocodage reunions liees apres sauvegarde |
| `addRelationship()` | Methode | Geocodage lors d'ajout de relation |
| `deleteRelationship()` | Methode | Geocodage lors de suppression de relation |

---

## Relations cles

- **Appele par :** Framework logic hooks SuiteCRM sur Project (before_save, after_save, after_relationship_*)
- **Appelle :** `jjwg_Maps::updateGeocodeInfo()`, `jjwg_Maps::updateRelatedMeetingsGeocodeInfo()`

---

## Points d'attention

- `addRelationship()` et `deleteRelationship()` sauvegardent le bean si l'adresse geocodee a change (ligne 48, 63) — peut provoquer une boucle si mal configure.
- N'agit que si `jjwg_Maps->settings['logic_hooks_enabled']` est vrai.
