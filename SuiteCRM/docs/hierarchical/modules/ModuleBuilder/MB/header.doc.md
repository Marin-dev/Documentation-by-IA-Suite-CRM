# header.php

**Chemin :** `modules/ModuleBuilder/MB/header.php`
**Type :** PHP (config / template)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Fichier de header de licence SugarCRM/SuiteCRM. Utilisé comme entête PHP généré dans tous les fichiers créés par ModuleBuilder (manifests, vardefs, config, fichiers de langue) via `file_get_contents('modules/ModuleBuilder/MB/header.php')`.

## Type
config

## Dépendances clés
Aucune.

## Exports/Symboles principaux
Aucun symbole PHP — contient uniquement la balise `<?php` et le bloc de commentaire de licence.

## Interactions
- **Appelé par :** `MBVardefs::save()`, `MBVardefs::build()`, `MBLanguage::save()`, `MBModule::saveConfig()`, `MBPackage::getManifest()`, `ParserSearchFields::saveSearchFields()`
- Utilisé pour préfixer tous les fichiers PHP générés par le Module Builder

## Notes
- Fichier volontairement vide de logique. Son seul rôle est de fournir le header de copyright aux fichiers générés.
