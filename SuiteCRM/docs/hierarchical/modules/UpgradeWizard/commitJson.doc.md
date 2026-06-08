# commitJson.php

**Chemin :** `modules/UpgradeWizard/commitJson.php`
**Type :** PHP - Script AJAX (réponse JSON commit)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Version AJAX/JSON de `commit.php`. Retourne la progression du commit de mise à jour au format JSON pour la mise à jour de la barre de progression dans l'interface.

## Type
helper (AJAX/JSON)

## Dépendances clés
- `uw_utils.php` (via includes UpgradeWizard)
- `getJSONobj()` — encodage JSON

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (AJAX polling pendant le commit)
- **Appelle :** fonctions de uw_utils.php

## Notes
- Variante JSON de `commit.php` pour les requêtes AJAX de polling.
