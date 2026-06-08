# silentUpgrade_step1.php

**Chemin :** `modules/UpgradeWizard/silentUpgrade_step1.php`
**Type :** PHP - Script CLI (étape 1 mise à jour silencieuse)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Première étape de la mise à jour silencieuse en ligne de commande. Prépare le système pour la mise à jour (création des répertoires d'upgrade, extraction du package). Accepte 3 paramètres CLI : chemin du package zip, chemin du log, chemin de l'instance.

## Type
helper (CLI)

## Dépendances clés
- `$sugar_config` — configuration globale
- `mkdir_recursive()` — création de répertoires
- `$subdirs` — liste des sous-répertoires d'upgrade

## Exports / Symboles principaux
- `prepSystemForUpgradeSilent()` (fonction) — prépare les répertoires d'upgrade

## Interactions
- **Appelé par :** ligne de commande : `php.exe -f silentUpgrade.php [zip] [log] [instance]`
- **Appelle :** `mkdir_recursive()`, fonctions uw_utils.php

## Notes
- `ini_set('memory_limit', -1)` — désactive la limite mémoire pour la mise à jour.
- Usage CLI documenté dans le commentaire en-tête du fichier.
