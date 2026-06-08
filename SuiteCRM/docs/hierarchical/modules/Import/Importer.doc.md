# Importer.php

**Chemin :** `modules/Import/Importer.php`
**Type :** PHP - Service / Model
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe principale d'importation de données. Lit chaque ligne d'une source d'import (`ImportDataSource`), sanitize les valeurs de chaque champ via `ImportFieldSanitize`, vérifie les doublons via `ImportDuplicateCheck`, et sauvegarde les beans SuiteCRM. Gère les erreurs ligne par ligne et écrit le statut final.

## Type
service / model

## Dépendances clés
- `modules/Import/ImportCacheFiles.php` — cache fichiers import
- `modules/Import/ImportFieldSanitize.php` — classe `ImportFieldSanitize`
- `modules/Import/ImportDuplicateCheck.php` — classe `ImportDuplicateCheck`
- `BeanFactory` — instanciation du bean cible
- `TrackerManager` — mis en pause pendant l'import
- `Localization` — conversion charset

## Exports / Symboles principaux
- `Importer` (classe)
  - `import()` — itère sur toutes les lignes et appelle `importRow()`
  - `importRow($row)` — traite une ligne (sanitize, dédoublonnage, save)
  - `handleImportErrors()` — gestionnaire d'erreurs PHP custom (static)

## Interactions
- **Appelé par :** `modules/Import/views/view.step4.php` (INCONNU — à confirmer)
- **Appelle :** `ImportFieldSanitize`, `ImportDuplicateCheck`, `BeanFactory`

## Notes
- `max_execution_time` forcé à `max(import_max_execution_time, 3600)` — risque si serveur avec limites strictes.
- Sauvegarde optionnelle du mapping d'import si `save_map_as` présent.
- `isUpdateOnly` : mode update-only si `import_type == 'update'`.
