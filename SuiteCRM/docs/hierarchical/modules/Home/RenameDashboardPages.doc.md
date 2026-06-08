# RenameDashboardPages.php

**Chemin :** `modules/Home/RenameDashboardPages.php`
**Type :** PHP - Action controller (script)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Renomme un onglet de tableau de bord. Affiche un formulaire si pas encore soumis, puis sauvegarde le nouveau titre dans les préférences utilisateur et renvoie le JSON avec le nouveau nom.

## Type
action / controller

## Dépendances clés
- `$current_user->getPreference/setPreference`
- `$GLOBALS['app_strings']`

## Exports / Symboles principaux
Aucun.

## Interactions
- **Appelé par :** action `RenameDashboardPages`

## Notes
- Retourne JSON (nom + page_id) en cas de succès — utilisé côté JS pour mise à jour de l'onglet sans rechargement.
