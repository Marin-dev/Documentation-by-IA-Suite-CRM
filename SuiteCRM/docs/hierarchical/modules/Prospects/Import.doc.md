# Import.php

**Chemin :** `modules/Prospects/Import.php`
**Type :** PHP - Délégation (import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Délègue l'import de Prospects au module Import générique via `include('modules/Import/index.php')`.

## Type
helper (délégation)

## Dépendances clés
- `modules/Import/index.php` — module d'import générique

## Exports / Symboles principaux
Aucune classe. Script trivial de délégation.

## Interactions
- **Appelé par :** action Import du module Prospects
- **Appelle :** `modules/Import/index.php`

## Notes
- Fichier trivial : uniquement un `include('modules/Import/index.php')`.
