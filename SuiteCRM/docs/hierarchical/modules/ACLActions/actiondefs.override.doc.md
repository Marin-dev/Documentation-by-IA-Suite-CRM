# actiondefs.override.php

**Chemin :** `modules/ACLActions/actiondefs.override.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Surcharge des definitions d'actions ACL standard. Cree et utilise par le module SecurityGroups pour modifier les niveaux d'acces par defaut ou ajouter des actions specifiques aux groupes.

## Type
config (surcharge)

## Interactions
- **Remplace :** `actiondefs.php` si present (verifie dans `ACLController` et `ACLAction`)

## Notes
- Ce fichier n'est charge que s'il existe physiquement (`file_exists` verifie).
- Contenu exact INCONNU sans lecture complete.
