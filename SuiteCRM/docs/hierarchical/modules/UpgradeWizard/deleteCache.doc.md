# deleteCache.php

**Chemin :** `modules/UpgradeWizard/deleteCache.php`
**Type :** PHP - Script d'action (nettoyage du cache)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Supprime les fichiers de cache SuiteCRM après une mise à jour pour forcer la régénération des fichiers compilés (templates Smarty, caches de modules, etc.).

## Type
helper

## Dépendances clés
- Fonctions de nettoyage du cache SugarCRM
- `logThis()` — journalisation

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (étape de nettoyage)
- **Appelle :** fonctions de suppression de cache

## Notes
- INCONNU : contenu détaillé non lu. Comportement basé sur le nom et le contexte d'utilisation.
