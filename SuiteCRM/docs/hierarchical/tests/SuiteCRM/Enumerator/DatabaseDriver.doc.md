# DatabaseDriver.php (fixture / enum)

**Chemin :** `tests/SuiteCRM/Enumerator/DatabaseDriver.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Enumérateur de constantes représentant les pilotes de base de données supportés dans les tests automatisés. Sert de valeur de référence pour configurer le driver DB utilisé dans les tests d'acceptance et d'installation.

## Type
fixture / enum

## Dependances cles
- Aucune dépendance externe

## Scenarios couverts
Pas de logique de test : fournit uniquement les constantes `NO_DRIVER`, `MYSQL`, `MSSQL`.

## Notes
- Consommé par `WebDriverHelper`, `PhpBrowserDriverHelper`, `InstallTester` pour sélectionner le type de base de données.
- Namespace : `SuiteCRM\Enumerator`.
