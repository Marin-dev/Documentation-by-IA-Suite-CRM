# undoupdateclass.php

**Chemin :** `modules/Administration/undoupdateclass.php`
**Type :** PHP (helper / migration)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Annule les modifications apportees par `updateclass.php`. Pour chaque bean, supprime le fichier `SugarCore.{NomBean}.php` genere par updateclass et restaure le fichier original.

## Role technique
Itere sur `$beanFiles`, derive le chemin du fichier `SugarCore.*` par insertion dans le chemin, et annule les modifications.

---

## Interactions
- **Complement de :** `updateclass.php`
- **Appele par :** Processus d'upgrade/rollback (INCONNU - contexte exact)
