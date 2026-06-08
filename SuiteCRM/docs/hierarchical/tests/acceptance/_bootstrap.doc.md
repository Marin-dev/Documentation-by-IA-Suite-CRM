# _bootstrap.php (helper / bootstrap acceptance)

**Chemin :** `tests/acceptance/_bootstrap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Bootstrap de la suite de tests acceptance Codeception. Charge l'environnement SuiteCRM complet (autoloader Composer, base de données, modules, entryPoint) nécessaire pour les tests d'acceptance UI.

## Type
helper / bootstrap

## Dependances cles
- `tests/_bootstrap.php` — bootstrap parent (Dotenv, constante sugarEntry)
- `DBManagerFactory` — instance DB globale (`$db`)
- `include/utils.php`, `include/modules.php`, `include/entryPoint.php`

## Notes
- Change le répertoire de travail vers la racine SuiteCRM (`chdir(__DIR__.'/../../')`) — toutes les chemins relatifs dans les tests acceptance sont relatifs à la racine.
- Initialise `$db` en global pour les Step Objects qui l'utilisent directement (ex: `Accounts.php`).
