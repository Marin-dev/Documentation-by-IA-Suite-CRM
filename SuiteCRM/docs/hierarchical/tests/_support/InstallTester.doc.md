# InstallTester.php (helper / acteur Codeception installation)

**Chemin :** `tests/_support/InstallTester.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Acteur Codeception spécialisé pour les tests du wizard d'installation de SuiteCRM. Encapsule les étapes du processus d'installation (acceptation de licence, configuration DB, configuration site, attente de fin d'installation).

## Type
helper / acteur Codeception (acceptance — installation)

## Dependances cles
- `Codeception\Actor` — classe parente
- `Helper\WebDriverHelper` — récupération de la configuration DB et des credentials
- `SuiteCRM\Enumerator\DatabaseDriver` — type de driver DB
- Trait `_generated\InstallTesterActions`

## Scenarios couverts
- `maySeeOldVersionDetected()` : gestion conditionnelle de l'écran d'avertissement PHP obsolète
- `acceptLicense()` : vérifie la page de licence et clique "I Accept"
- `seeValidSystemEnvironment()` : vérifie la page d'environnement système
- `configureInstaller(WebDriverHelper)` : remplit les champs DB (MySQL ou MSSQL) et les champs de configuration site
- `waitForInstallerToFinish()` : attend la fin de l'installation (timeout 90s)
- `dontSeeMissingLabels()` / `dontSeeErrors()` : assertions de qualité

## Notes
- Deux TODO dans `configureInstaller()` mentionnent des tests de validation de formulaire non implémentés (ligne 139-140).
- `isOldPhpVersionDetected()` exécute du JavaScript : dépendant du WebDriver.
