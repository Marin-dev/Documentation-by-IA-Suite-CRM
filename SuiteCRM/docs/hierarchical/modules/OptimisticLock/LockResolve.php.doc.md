# LockResolve.php (OptimisticLock)

**Chemin :** `modules/OptimisticLock/LockResolve.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Gere la resolution des conflits de verrouillage optimiste dans SuiteCRM. Quand deux utilisateurs editent le meme enregistrement simultanement, affiche un tableau comparatif des differences et propose a l'utilisateur de garder sa version ou celle en base de donnees.

**Type :** controller / view (resolution de conflits)

---

## Dependances cles
- `$_SESSION['o_lock_object']` — objet en conflit (tableau de champs)
- `$_SESSION['o_lock_module']` — nom du module de l'objet en conflit
- `$_SESSION['o_lock_save']` — HTML de sauvegarde a re-executer si "Accept Yours"
- `BeanFactory::getBean($module, $id)` — charge l'etat actuel depuis la base
- `return_module_language('OptimisticLock')` — chaines de langue du module
- `SugarCleaner::cleanHtml()` — nettoyage XSS des valeurs a comparer
- `$timedate` — objet global de gestion des dates (conversion format utilisateur)

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `display_conflict_between_objects($obj1, $obj2, $field_defs, $module_dir, $display_name)` | fonction | Compare deux versions d'un objet et affiche un tableau HTML des differences |

## Interactions
- **Appele par :** routeur SuiteCRM via `index.php?module=OptimisticLock&action=LockResolve`
- **Appelle :** `BeanFactory::getBean()`, `return_module_language()`, `SugarCleaner::cleanHtml()`, `SugarApplication::redirect()`
- **Position dans le flux :** Declenche apres detection d'un conflit de sauvegarde concurrente dans n'importe quel module avec `optimistic_locking = true`

## Notes
- Si aucun conflit de champ different n'est detecte, redirige automatiquement vers `LockResolve&save=true` (sauvegarde silencieuse).
- "Accept Yours" : re-execute `$_SESSION['o_lock_save']` (HTML form hidden contenant la sauvegarde precedente).
- "Accept Database" : redirige vers la vue DetailView du bean en base (abandon des modifications).
- Champs ignores dans la comparaison : `team_name`, `date_entered`, `date_modified` (ligne 55).
- Gere les types `date`, `datetime`, `datetimecombo` et `bool` avec normalisation avant comparaison.
- Risque : si `$_SESSION['o_lock_save']` contient du code arbitraire, il est execute via `echo` (ligne 107) — attention a la securite.
