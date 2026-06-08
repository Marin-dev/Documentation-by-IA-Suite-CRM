# TestEnvironmentCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/TestEnvironmentCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commandes Robo pour configurer l'environnement de test, installer ChromeDriver, et simuler un environnement Travis CI. Permet de preparer automatiquement les variables d'environnement necessaires aux tests automatises.

## Role technique
Utilise `OperatingSystem` pour la detection d'OS et l'ecriture des variables d'env (Unix: `~/.bash_aliases`, Windows: `setx`). Telecharge et dezipe ChromeDriver depuis `chromedriver.storage.googleapis.com`.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Utility\{OperatingSystem, Paths}`
- `SuiteCRM\Robo\Traits\RoboTrait`

## Exports / Symboles principaux
- `TestEnvironmentCommands` — classe commandes Robo
  - `configureTests(array $opts): void` — configuration environnement de test interactif
  - `chromeDriverInstall($opts): void` — installation ChromeDriver
  - `chromeDriverRun($opts): void` — lancement ChromeDriver
  - `fakeTravis(array $opts): void` — simulation Travis CI

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo configure:tests`, `chromedriver:*`)
- **Variables d'environnement configurees :** `DATABASE_DRIVER/NAME/HOST/USER/PASSWORD`, `INSTANCE_URL/ADMIN_USER/PASSWORD/CLIENT_ID/SECRET`

---

## Points d'attention
- `getChromeWebDriverUrl()` accede en ligne a `chromedriver.storage.googleapis.com` — necessite Internet.
- `fakeTravis()` et `configureTests()` modifient des fichiers systeme (`~/.bash_aliases`) apres confirmation.
- BSD et Solaris : `chromeDriverInstall` leve une `DomainException` (non supporte).
