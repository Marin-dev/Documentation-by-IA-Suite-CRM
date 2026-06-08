# view.step4.php

**Chemin :** `modules/Import/views/view.step4.php`
**Type :** PHP - Vue (étape 4 d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de la quatrième étape du wizard d'import : exécution de l'import et affichage du résumé (nombre de lignes importées, erreurs, doublons). Lance le processus d'import via `Importer`.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/Importer.php` — exécution de l'import

## Exports / Symboles principaux
- `ImportViewStep4` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)

## Interactions
- **Appelé par :** wizard d'import après confirmation (étape confirm)
- **Appelle :** `Importer::import()`

## Notes
- Étape finale d'exécution — affiche le résumé et les liens vers les erreurs/doublons.
