# silentUpgrade.php

**Chemin :** `modules/UpgradeWizard/silentUpgrade.php`
**Type :** PHP - Script CLI (mise à jour silencieuse)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script d'orchestration des mises à jour silencieuses (sans interface utilisateur). Fournit la fonction utilitaire `build_argument_string()` pour construire des chaînes d'arguments CLI, utilisée lors de l'exécution des scripts de mise à jour en mode non interactif.

## Type
helper (CLI)

## Dépendances clés
Aucune dépendance directe visible.

## Exports / Symboles principaux
- `build_argument_string($arguments)` (fonction) — construit une chaîne d'arguments CLI à partir d'un tableau, en substituant `.` par `getcwd()` et `..` par le répertoire parent

## Interactions
- **Appelé par :** scripts `silentUpgrade_step1.php`, `silentUpgrade_step2.php`
- **Appelle :** `getcwd()`

## Notes
- Conçu pour une exécution en ligne de commande (CLI) sans interaction utilisateur.
