# MailMerge.php

**Chemin :** `modules/MailMerge/MailMerge.php`
**Type :** PHP - Service
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe principale du publipostage (mail merge). Gère la création de documents Word/DOC avec données fusionnées depuis SuiteCRM. Produit un fichier datasource (`ds.doc`) et un fichier d'en-tête (`header.doc`) pour la fusion avec un modèle de document.

## Type
service

## Dépendances clés
- Fichiers Word/DOC (manipulation via propriétés objet)

## Exports / Symboles principaux
- `MailMerge` (classe)
  - `$mm_data_dir` — répertoire des fichiers de fusion
  - `$datasource_file` (`ds.doc`) — fichier de données
  - `$header_file` (`header.doc`) — fichier d'en-tête
  - `$fieldcnt`, `$rowcnt` — compteurs champs/lignes
  - `$template`, `$list`, `$fieldList`

## Interactions
- **Appelé par :** `modules/MailMerge/Step*.php`, `Merge.php`

## Notes
- Module intégré pour le publipostage Word ; dépend de la présence de templates de documents.
