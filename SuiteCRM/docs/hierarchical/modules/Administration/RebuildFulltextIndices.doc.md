# RebuildFulltextIndices.php

**Chemin :** `modules/Administration/RebuildFulltextIndices.php`
**Type :** PHP (action / maintenance BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Reconstruit les index de type `fulltext` pour tous les beans qui en ont. Executes uniquement pour le type de BDD courant.

## Role technique
Itere sur `$beanFiles`, pour chaque bean verifie les indices de type `fulltext` dans les vardefs, et execute `ALTER INDEX ... REBUILD` via `DBManagerFactory`.

---

## Notes
- Le code contient une duplication de la verification `$processed_tables` (lignes 57-67) — bug mineur sans consequence fonctionnelle.
- Specifique aux BDD supportant `ALTER INDEX ... REBUILD` (Oracle, MSSQL) — peu utilise avec MySQL/MariaDB.
