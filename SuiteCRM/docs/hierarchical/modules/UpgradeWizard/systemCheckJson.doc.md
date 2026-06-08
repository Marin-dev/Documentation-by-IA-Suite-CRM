# systemCheckJson.php

**Chemin :** `modules/UpgradeWizard/systemCheckJson.php`
**Type :** PHP - Script AJAX (réponse JSON vérification système)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Version AJAX/JSON de `systemCheck.php`. Retourne les résultats des vérifications système au format JSON pour affichage dynamique dans l'interface.

## Type
helper (AJAX/JSON)

## Dépendances clés
- INCONNU (contenu non lu)

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** wizard UpgradeWizard (AJAX polling pendant systemCheck)
- **Appelle :** fonctions de systemCheck / uw_utils.php

## Notes
- Variante JSON de `systemCheck.php` pour les requêtes AJAX.
