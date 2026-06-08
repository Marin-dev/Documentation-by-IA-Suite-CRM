# systemCheck.php

**Chemin :** `modules/UpgradeWizard/systemCheck.php`
**Type :** PHP - Script de vérification système
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Effectue les vérifications système pré-mise à jour : permissions de fichiers, vérifications de compatibilité. Définit un flag `$stop` pour empêcher le passage à l'étape suivante si des problèmes critiques sont détectés.

## Type
helper

## Dépendances clés
- `logThis()` — journalisation (via uw_utils.php)
- `$stop` — flag de blocage de progression

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape systemCheck)
- **Appelle :** `logThis()`, fonctions de vérification de permissions

## Notes
- `$stop = false` initialement — devient `true` si une vérification critique échoue.
- Lance la vérification des permissions de fichiers en premier (ligne 50).
