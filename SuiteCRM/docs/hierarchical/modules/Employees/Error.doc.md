# Error.php

**Chemin :** `modules/Employees/Error.php`
**Type :** PHP - Vue (affichage d'erreur)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche un message d'erreur depuis la chaîne passée en paramètre (`$_REQUEST['error_string']`). Fonctionnalité dépréciée : l'utilisation de `error_string` dans la requête est marquée deprecated et génère un avertissement log.

## Type
view

## Dépendances clés
- `include/utils.php`
- `$app_strings` — traductions
- `LoggerManager::getLogger()->warn()` — avertissement de dépréciation

## Exports / Symboles principaux
Aucune classe ni fonction. Script procédural + HTML.

## Interactions
- **Appelé par :** redirections d'erreur dans le module Employees
- **Appelle :** `getAppString()`, `LoggerManager`

## Notes
- Dépréciée : les deux chemins (REQUEST et variable `$request`) affichent un warning de dépréciation.
- Génère simplement un `<span class='error'>` avec le message traduit.
