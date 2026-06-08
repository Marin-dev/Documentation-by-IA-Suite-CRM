# en_us.lang.php (OptimisticLock)

**Chemin :** `modules/OptimisticLock/language/en_us.lang.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Fichier de langue anglaise du module OptimisticLock. Definit les chaines affichees lors de la resolution des conflits de concurrence (edition simultanee d'un enregistrement).

**Type :** config (langue)

---

## Dependances cles
- Aucune (fichier de donnees pur)

## Exports / Symboles principaux

Tableau `$mod_strings` :

| Cle | Valeur | Usage |
|---|---|---|
| `LBL_YOURS` | `'Yours'` | En-tete colonne version utilisateur |
| `LBL_IN_DATABASE` | `'In Database'` | En-tete colonne version base |
| `LBL_CONFLICT_EXISTS` | `'A Conflict Exists For - '` | Message de conflit |
| `LBL_ACCEPT_DATABASE` | `'Accept Database'` | Lien pour accepter la version base |
| `LBL_ACCEPT_YOURS` | `'Accept Yours'` | Lien pour forcer sa propre version |
| `LBL_RECORDS_MATCH` | `'Records Match'` | Message si pas de conflit |
| `LBL_NO_LOCKED_OBJECTS` | `'No Locked Objects'` | Message si session vide |

## Interactions
- **Appele par :** `LockResolve.php` via `return_module_language('OptimisticLock')`
- **Appelle :** rien

## Notes
- Petit fichier avec seulement 7 chaines — module tres ciblé.
