# view.confirm.php

**Chemin :** `modules/Import/views/view.confirm.php`
**Type :** PHP - Vue (étape d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de confirmation d'import : affiche un aperçu des données (3 premières lignes) avant l'import définitif. Charge le fichier, détecte le format CSV, et permet à l'utilisateur de valider ou corriger le mapping des colonnes.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/sources/ImportFile.php` — lecture du fichier
- `modules/Import/ImportFileSplitter.php` — découpage du fichier
- `modules/Import/CsvAutoDetect.php` — détection auto du format
- `include/upload_file.php` — gestion de l'upload

## Exports / Symboles principaux
- `ImportViewConfirm` (classe, étend `ImportView`)
  - `SAMPLE_ROW_SIZE` = 3 — nombre de lignes d'aperçu
  - `$pageTitleKey` = `'LBL_CONFIRM_TITLE'`
  - `display()` — affiche l'aperçu de confirmation

## Interactions
- **Appelé par :** wizard d'import après l'étape 3 (mapping des champs)
- **Appelle :** `ImportFile`, `ImportFileSplitter`, `CsvAutoDetect`

## Notes
- Étape centrale du wizard d'import : c'est ici que le débogage du mapping se fait.
