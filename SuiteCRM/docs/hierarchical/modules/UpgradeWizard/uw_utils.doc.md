# uw_utils.php

**Chemin :** `modules/UpgradeWizard/uw_utils.php`
**Type :** PHP - Helper / Utilitaires
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Fichier de fonctions utilitaires pour l'assistant de mise à niveau (UpgradeWizard). Fournit notamment la fonction de normalisation/comparaison des numéros de version SuiteCRM (gestion des suffixes beta, rc, sous-versions).

## Type
helper

## Dépendances clés
- `include/dir_inc.php` — utilitaires de gestion des répertoires

## Exports / Symboles principaux
- Fonctions de manipulation de version (INCONNU — lecture partielle, exemples dans les commentaires : `versionToInt`, `implodeVersion`)

## Interactions
- **Appelé par :** scripts d'upgrade (`preflight.php`, `commit.php`, `silentUpgrade*.php`)

## Notes
- Normalise des numéros de version comme "6.5.6beta2" → "656" ou "6.6.0.1" → "6601".
