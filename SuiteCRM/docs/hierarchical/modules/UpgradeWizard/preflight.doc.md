# preflight.php

**Chemin :** `modules/UpgradeWizard/preflight.php`
**Type :** PHP - Script d'action (vérifications pré-mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script legacy de vérification pré-mise à jour (preflight). Émule l'ancien `upload.php` et rafraîchit les chaînes de traduction du module. Contient les vérifications préliminaires avant de lancer le processus de mise à jour.

## Type
helper (legacy)

## Dépendances clés
- `$mod_strings` (global)

## Exports / Symboles principaux
Aucune classe. Script procédural minimal.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape preflight)
- **Appelle :** INCONNU (contenu limité visible)

## Notes
- Commentaire interne : "LEGACY for old versions - emulating upload.php".
