# uw_emptyFunctions.php

**Chemin :** `modules/UpgradeWizard/uw_emptyFunctions.php`
**Type :** PHP - Helper (stub de fonctions)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit des fonctions vides ("stubs") nécessaires pour satisfaire les dépendances du processus de mise à jour des métadonnées. Actuellement, contient uniquement `getJSPath()` vide.

## Type
helper (stub)

## Dépendances clés
Aucune.

## Exports / Symboles principaux
- `getJSPath($file = '')` (fonction vide) — stub pour compatibilité avec le meta upgrade

## Interactions
- **Appelé par :** `upgradeMetaHelper.php` et processus de mise à jour des métadonnées
- **Appelle :** rien

## Notes
- Commentaire en code : "empty function getJSPath().. there is some dependency in meta upgrade".
- Fichier de contournement de dépendance — peut évoluer si d'autres stubs sont nécessaires.
