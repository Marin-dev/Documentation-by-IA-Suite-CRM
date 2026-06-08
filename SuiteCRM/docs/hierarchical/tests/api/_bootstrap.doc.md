# _bootstrap.php (helper / bootstrap API)

**Chemin :** `tests/api/_bootstrap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Bootstrap de la suite de tests API Codeception. Charge l'environnement SuiteCRM complet et configure les chaînes de langue, les modules, et surcharge la limite de ressources pour permettre les tests API sans throttling.

## Type

helper / bootstrap

## Dependances cles

- `tests/_bootstrap.php` — bootstrap parent
- `DBManagerFactory`, `include/utils.php`, `include/modules.php`, `include/entryPoint.php`

## Notes

- Initialise `$GLOBALS['app_list_strings']` en `en_us` (l'entryPoint ne charge pas les app_list_strings).
- Surcharge `sugar_config['resource_management']['default_limit']` à 999999 — commenté `VERY BAD` dans le code : workaround temporaire pour éviter les limits API dans les tests.
- Namespace racine SuiteCRM via `chdir(__DIR__.'/../../')`.
