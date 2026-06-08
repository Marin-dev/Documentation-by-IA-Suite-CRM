# ImportDuplicateCheck.php

**Chemin :** `modules/Import/ImportDuplicateCheck.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère la détection des doublons lors de l'import. Maintient une référence privée au bean cible (`$_focus`) et fournit des méthodes pour obtenir la liste des champs de dédoublonnage et effectuer les vérifications.

## Type
service / helper

## Dépendances clés
- `SugarBean` (via `$_focus`)

## Exports / Symboles principaux
- `ImportDuplicateCheck` (classe)
  - `$_focus` — bean cible (private)
  - Méthodes de vérification de doublons (INCONNU — lecture partielle)

## Interactions
- **Appelé par :** `Importer::importRow()`

## Notes
- Lecture partielle. Les méthodes exactes sont INCONNUES.
