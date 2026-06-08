# uw_files.php

**Chemin :** `modules/UpgradeWizard/uw_files.php`
**Type :** PHP - Configuration (liste des fichiers du wizard)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Génère dynamiquement la liste des fichiers du module UpgradeWizard. Gère la compatibilité lors de mises à jour depuis des versions 4.x qui n'avaient pas de module UpgradeWizard (liste statique de fallback avec moins de 5 fichiers détectés).

## Type
config / helper

## Dépendances clés
- `findAllFiles()` — inventaire dynamique du répertoire `modules/UpgradeWizard/`
- `$sugar_version` (global)

## Exports / Symboles principaux
- `$uwFilesCurrent` — liste dynamique des fichiers UpgradeWizard courants
- `$uwFiles` — liste statique de fallback pour compatibilité 4.x

## Interactions
- **Appelé par :** processus de mise à jour (pour la copie/vérification des fichiers)
- **Appelle :** `findAllFiles()`

## Notes
- Si `count($uwFilesCurrent) < 5`, utilise une liste statique codée en dur (compatibilité 4.x).
