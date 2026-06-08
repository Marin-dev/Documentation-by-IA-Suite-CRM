# upgradeTimeCounter.php

**Chemin :** `modules/UpgradeWizard/upgradeTimeCounter.php`
**Type :** PHP - Helper (compteur de temps de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de comptage du temps écoulé lors des étapes de mise à jour. Initialise la session, charge les utilitaires JSON, DB et ZIP, puis utilise `uw_utils.php` pour calculer les temps d'exécution des différentes étapes.

## Type
helper

## Dépendances clés
- `include/JSON.php`
- `include/utils/db_utils.php`
- `include/utils/php_zip_utils.php`
- `modules/UpgradeWizard/uw_utils.php`
- `getJSONobj()`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (AJAX) pour afficher la progression temporelle
- **Appelle :** `uw_utils.php`

## Notes
- Appelle `session_start()` et définit `$GLOBALS['installing'] = true` (ligne 45-46).
- Code AJAX commenté visible en ligne 60 (décoratif pour le compteur de temps).
