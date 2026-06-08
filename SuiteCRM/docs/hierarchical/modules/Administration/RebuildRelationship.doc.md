# RebuildRelationship.php

**Chemin :** `modules/Administration/RebuildRelationship.php`
**Type :** PHP (action / maintenance BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Reconstruit entierement la table `relationships` en BDD. Supprime toutes les entrees existantes, puis reinsere les metadonnees de relation pour chaque bean et chaque relation de `TableDictionary`. Vide le cache des relations. Retire le flag session `rebuild_relationships` pour cesser les avertissements dans `DisplayWarnings.php`.

## Role technique
Script procedral. `DELETE FROM relationships` puis iteration sur `$beanFiles` et `$dictionary` (TableDictionary + extensions custom). Appelle `SugarBean::createRelationshipMeta()` pour chaque module. `Relationship::delete_cache()` + `build_relationship_cache()` en fin.

---

## Dependances cles
| Element | Role |
|---|---|
| `include/modules.php` | $beanFiles |
| `modules/TableDictionary.php` | Relations N-N |
| `SugarBean::createRelationshipMeta()` | Insertion metadonnees relation |
| `Relationship::delete_cache()` | Suppression cache relations |
| `VardefManager::clearVardef()` | Reinitialisation vardefs |

## Interactions
- **Appele par :** `index.php?module=Administration&action=RebuildRelationship`
- **Modifie :** Table `relationships` (DELETE total puis INSERT)

---

## Notes
- `DELETE FROM relationships` sans condition : destructif si execute manuellement. Les relations sont recrees depuis les vardefs.
- `$_REQUEST['silent']` desactive les echoes HTML.
- Supprime `$_SESSION['rebuild_relationships']` pour retirer le bandeau rouge de l'admin.
