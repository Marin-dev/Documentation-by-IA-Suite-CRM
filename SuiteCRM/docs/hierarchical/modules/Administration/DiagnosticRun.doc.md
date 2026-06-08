# DiagnosticRun.php

**Chemin :** `modules/Administration/DiagnosticRun.php`
**Type :** PHP (action / traitement)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Execute le diagnostic systeme de SuiteCRM : collecte config.php (sans mot de passe), phpinfo, repertoire custom (zip), informations BDD (schema, dumps de tables cles), verification MD5 des fichiers, liste des beanFiles, log SuiteCRM, et vardefs de tous les modules. Compresse le tout dans un ZIP teleChargeable.

## Role technique
Script procedral structurant 10+ fonctions de collecte. Chaque fonction cree des fichiers dans un repertoire cache temporaire (`cache/diagnostic/{guid}/...`). Une barre de progression est mise a jour. A la fin, `finishDiag()` zippe le repertoire et supprime les fichiers temporaires. Masque les mots de passe sensibles (smtppass, ldap admin_password, proxy password) dans les dumps.

---

## Dependances cles
| Import | Role |
|---|---|
| `include/utils/progress_bar_utils.php` | Barre de progression |
| `include/utils/php_zip_utils.php` | Compression ZIP |
| `SugarLogger` | Copie du fichier log |
| `DBManagerFactory` | Acces schema et donnees BDD |
| `VardefManager` | Non utilise directement mais contexte global |

## Fonctions principales

| Fonction | Role |
|---|---|
| `prepareDiag()` | Initialise le repertoire cache, la barre de progression |
| `executeconfigphp()` | Copie config.php (mot de passe BDD masque) |
| `executephpinfo()` | Capture la sortie de phpinfo() |
| `executecustom_dir()` | Zippe le repertoire `custom/` |
| `execute_sql($getinfo, $getdumps, $getschema)` | Schema BDD + dumps tables config/fields_meta_data/upgrade_history/versions |
| `executebeanlistbeanfiles()` | Verifie l'existence de chaque fichier beanFile |
| `executesugarlog()` | Copie suitecrm.log |
| `executevardefs()` | HTML de tous les vardefs par table |
| `executemd5($filesmd5, $md5calculated)` | Compare fichiers avec files.md5 |
| `finishDiag()` | Zippe et supprime le repertoire temporaire |
| `getFullTableDump($tableName)` | Dump HTML d'une table (masque smtppass/ldap/proxy passwords) |
| `deleteDir($dir)` | Supprime un repertoire recursivement |
| `sodUpdateProgressBar($itemweight)` | MAJ barre de progression |
| `array_as_table($header, $values)` | Formate un tableau en HTML |

## Interactions
- **Appele par :** Formulaire `Diagnostic.tpl` (POST)
- **Lie a :** `DiagnosticDownload.php` (lien de telechargement genere), `DiagnosticDelete.php` (lien de suppression)
- **Ecrit dans :** `cache/diagnostic/{guid}/diagnostic{datetime}/`

---

## Notes
- `set_time_limit(3600)` : peut prendre du temps sur de grosses instances.
- Les mots de passe sont masques par `'********'` dans les dumps — logique explicite ligne 218-234.
- `$skip_md5_diff = true` si `files.md5` est absent — certaines installations n'ont pas ce fichier.
- Les constantes de poids (`CONFIG_WEIGHT`, `MD5_WEIGHT=5`, etc.) ponderent la barre de progression.
