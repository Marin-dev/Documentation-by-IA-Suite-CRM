# preflightJson.php

**Chemin :** `modules/UpgradeWizard/preflightJson.php`
**Type :** PHP - Script AJAX (réponse JSON preflight)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Version AJAX/JSON de `preflight.php`. Retourne la progression des vérifications pré-mise à jour au format JSON.

## Type
helper (AJAX/JSON)

## Dépendances clés
- INCONNU (contenu non lu)

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (AJAX polling pendant le preflight)
- **Appelle :** fonctions de uw_utils.php

## Notes
- Variante JSON de `preflight.php` pour les requêtes AJAX de polling.
