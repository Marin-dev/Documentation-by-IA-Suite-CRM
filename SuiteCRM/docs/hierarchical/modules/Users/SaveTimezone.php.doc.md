# Fichier : SaveTimezone.php

**Chemin :** `modules/Users/SaveTimezone.php`
**Type :** PHP — Script d'action (sauvegarde fuseau horaire)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Sauvegarde le fuseau horaire choisi par l'utilisateur lors du wizard de premier demarrage, marque le wizard comme complete (`ut=1`), et redirige vers la page d'accueil.

## Role technique

Script procedural tres court. Lit `timezone` depuis POST ou GET, appelle `$current_user->setPreference('timezone', ...)` et `setPreference('ut', 1)`, puis `savePreferencesToDB()`. Ferme la session en ecriture avant la redirection pour eviter les conflits de verrou session.

---

## Exports / Symboles principaux

Aucun.

---

## Relations cles

- **Appele par :** wizard ou formulaire de choix de fuseau horaire (`SetTimezone.php`)
- **Appelle :** `$current_user->setPreference()`, `savePreferencesToDB()`, `session_write_close()`

---

## Points d'attention

- `session_write_close()` avant `header('Location:')` — pattern important pour eviter les verrous de session lors de redirections.
