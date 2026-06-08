# UpgradeRemoval.php

**Chemin :** `modules/UpgradeWizard/UpgradeRemoval.php`
**Type :** PHP - Classe de base (suppression de fichiers lors de mise à jour)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base permettant la suppression de fichiers et répertoires lors d'une mise à jour SuiteCRM. Conçue pour être étendue par des classes custom dans `custom/scripts/files_to_remove/` afin de définir des listes de fichiers à supprimer spécifiques à une version.

## Type
helper (base class)

## Dépendances clés
Aucune dépendance externe directe.

## Exports / Symboles principaux
- `UpgradeRemoval` (classe)
  - `$version` — version minimale pour la suppression
  - `getFilesToRemove($version)` — retourne un tableau vide (à surcharger)
  - `processFilesToRemove()` — supprime les fichiers/répertoires retournés par `getFilesToRemove()`

## Interactions
- **Appelé par :** `uw_utils.php::unlinkUpgradeFiles()` pendant le processus de mise à jour
- **Appelle :** fonctions PHP de suppression de fichiers

## Notes
- Pattern Template Method : sous-classer et surcharger `getFilesToRemove()` pour personnaliser.
- Placer les sous-classes dans `custom/scripts/files_to_remove/` pour qu'elles soient découvertes automatiquement.
