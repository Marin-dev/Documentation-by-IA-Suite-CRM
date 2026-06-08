# updateclass.php

**Chemin :** `modules/Administration/updateclass.php`
**Type :** PHP (helper / migration)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Prepare la migration des beans SugarCRM en renommant chaque classe en prefixant `SugarCore` (ex: `SugarCoreCall`). Cree un fichier intermediaire pour le processus d'upgrade.

## Role technique
Itere sur `$beanFiles`, renomme la classe et son constructeur via regex/manipulation de code, cree un fichier `SugarCore.{NomOriginal}.php`. Utilise `sugar_file_utils.php`.

---

## Interactions
- **Annule par :** `undoupdateclass.php`
- **Appele par :** Processus d'upgrade SugarCRM (INCONNU - contexte exact)
