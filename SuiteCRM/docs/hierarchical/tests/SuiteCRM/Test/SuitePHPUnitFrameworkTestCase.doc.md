# SuitePHPUnitFrameworkTestCase.php (helper / classe de base)

**Chemin :** `tests/SuiteCRM/Test/SuitePHPUnitFrameworkTestCase.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Classe de base abstraite pour tous les tests unitaires PHPUnit du projet SuiteCRM. Elle initialise l'environnement d'exécution (connexion DB, utilisateur courant, logger de test, configuration Sugar) et garantit une remise à l'état initial entre chaque test.

## Type
helper / classe de base de test unitaire

## Dependances cles
- `BeanFactory` — création de l'utilisateur courant
- `DBManagerFactory` — accès à la base de données et gestion des instances
- `LoggerManager` — substitué par `TestLogger` pendant les tests
- `SuiteCRM\TestCaseAbstract` — classe parente (logique de setup générique)
- `SuiteCRM\Exception\Exception`

## Scenarios couverts
Pas de scénario de test propre. Fournit :
- `setUp()` : connexion DB, substitution du logger, snapshot de `sugar_config`
- `tearDown()` : restauration du logger, de `sugar_config`, et des instances DBManager
- `setUpBeforeClass()` : reconnexion DB propre avant la classe

## Notes
- Le `TestLogger` est injecté dans `$GLOBALS['log']` pour capturer les appels de log pendant les tests (voir `TestLogger.php`).
- La restauration de `$sugar_config` est manuelle par valeur, ce qui peut poser des problèmes si un test modifie un objet de configuration imbriqué par référence.
- Consommé par la quasi-totalité des tests unitaires PHPUnit du dossier `tests/unit/phpunit/`.
