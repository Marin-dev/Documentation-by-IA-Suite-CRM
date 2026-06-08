# _bootstrap.php (helper / bootstrap unit)

**Chemin :** `tests/unit/_bootstrap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Bootstrap de la suite de tests unitaires PHPUnit/Codeception. Charge l'environnement SuiteCRM complet (autoloader, DB, modules, entryPoint, chaînes de langue) et définit la constante `SUITE_PHPUNIT_RUNNER` pour identifier le contexte de test.

## Type

helper / bootstrap

## Dependances cles

- `vendor/autoload.php` — autoloader Composer (chargé directement ici, pas via parent)
- `DBManagerFactory`, `include/utils.php`, `include/modules.php`, `include/entryPoint.php`

## Notes

- Définit `SUITE_PHPUNIT_RUNNER = true` pour permettre aux classes testées de détecter le contexte de test si besoin.
- Même surcharge `resource_management['default_limit'] = 999999` que la suite API.
- Initialise `$db` et `$sugar_config` en globaux.
