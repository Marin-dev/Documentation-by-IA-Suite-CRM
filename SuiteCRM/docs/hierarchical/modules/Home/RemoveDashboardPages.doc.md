# RemoveDashboardPages.php

**Chemin :** `modules/Home/RemoveDashboardPages.php`
**Type :** PHP - Action controller (script)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Supprime un onglet de tableau de bord. Affiche d'abord un formulaire de confirmation, puis sur validation (`$_POST['status'] = 'yes'`) supprime la page des préférences utilisateur et redirige vers Home.

## Type
action / controller

## Dépendances clés
- `$current_user->getPreference/setPreference`
- `SugarApplication::redirect()`
- `$GLOBALS['app_strings']`

## Exports / Symboles principaux
Aucun.

## Interactions
- **Appelé par :** action `RemoveDashboardPages`
- **Appelle :** `SugarApplication`

## Notes
- Suppression impossible s'il n'y a qu'une seule page (condition `count($pages) > 1`).
