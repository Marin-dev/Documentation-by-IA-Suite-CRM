# ImportMap.php

**Chemin :** `modules/Import/maps/ImportMap.php`
**Type :** PHP - Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean SuiteCRM représentant un mapping d'import sauvegardé (`import_map` table). Stocke la correspondance entre colonnes du fichier source et champs du module cible, permettant de réutiliser un mapping.

## Type
model

## Dépendances clés
- `SugarBean` (classe parente)

## Exports / Symboles principaux
- `ImportMap` (classe) — étend `SugarBean`
  - Champs : `$id`, `$name`, et autres (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** `Importer::saveMappingFile()`, vues d'import

## Notes
- Fichier lu partiellement. Les autres champs (module_name, content, etc.) sont INCONNUS.
