# CheckLogins.php

**Chemin :** `modules/EAPM/CheckLogins.php`
**Type :** helper (AJAX)

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vérifie si les comptes d'APIs externes OAuth de l'utilisateur connecté sont toujours valides. Seuls les comptes OAuth sont vérifiés (les logins/mots de passe n'expirent pas).

## Type

helper (AJAX)

---

## Dépendances clés

- `ExternalAPIFactory` (`include/externalAPI/ExternalAPIFactory.php`)
- `$app_strings`

## Exports / Symboles principaux

- Aucun — script procédural (retourne JSON ou HTML)

## Interactions

- **Appelé par :** tableau de bord ou vues EAPM (vérification périodique AJAX)
- **Appelle :** `ExternalAPIFactory::listAPI()` puis vérification OAuth par API

## Notes

- Uniquement les APIs OAuth sont vérifiées (`listAPI('', true)`).
