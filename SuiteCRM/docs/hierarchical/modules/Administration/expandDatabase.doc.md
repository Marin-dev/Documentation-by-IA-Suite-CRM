# expandDatabase.php

**Chemin :** `modules/Administration/expandDatabase.php`
**Type :** PHP (view + action / maintenance BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Outil d'expansion des colonnes BDD de type varchar/char dont la longueur est inferieure a 255. Multiplie la longueur par 3 (plafonnee a 255) pour supporter les jeux de caracteres multi-octets. Specifique aux bases de type SQL Server (MSSQL).

## Role technique
Verifie `$db->supports('fix:expandDatabase')` — arrete si la BDD ne supporte pas. Requete sur `sys.sysobjects` et `sys.syscolumns` pour trouver les colonnes courtes. Modes : `display` (affiche SQL), `export` (telechargement SQL), `execute` (execute + cree `restoreExpand.sql` de restauration).

---

## Notes
- Exclusivement MSSQL/SQL Server (requete sur `sys.*`) — inutilisable sur MySQL/MariaDB.
- Cree `restoreExpand.sql` a la racine pour permettre le rollback.
- `set_time_limit(3600)`.
