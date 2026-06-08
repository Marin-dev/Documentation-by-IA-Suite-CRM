# UpgradeCommands.php

**Chemin :** `lib/Robo/Plugin/Commands/UpgradeCommands.php`
**Type :** PHP — Commandes Robo CLI
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Commande Robo pour lancer la mise a jour silencieuse de SuiteCRM depuis la ligne de commande via `silentUpgrade.php`.

## Role technique
Une seule commande `upgradeSuite`. Appelle `php modules/UpgradeWizard/silentUpgrade.php` avec les parametres fournis.

---

## Dependances cles
- `Robo\Tasks`
- `SuiteCRM\Robo\Traits\RoboTrait`

## Exports / Symboles principaux
- `UpgradeCommands` — classe commandes Robo
  - `upgradeSuite(string $upgradeZip, string $logFile, string $crmPath, string $adminUser): void`

## Relations cles
- **Appele par :** CLI Robo (`./vendor/bin/robo upgrade:suite`)
- **Appelle :** `modules/UpgradeWizard/silentUpgrade.php`

---

## Points d'attention
- L'upgrade est irreversible ; s'assurer de sauvegarder avant execution.
- `$crmPath` doit etre le chemin absolu vers l'installation SuiteCRM.
