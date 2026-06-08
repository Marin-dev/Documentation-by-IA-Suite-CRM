# AddDashboardPages.php

**Chemin :** `modules/Home/AddDashboardPages.php`
**Type :** PHP - Action controller (script)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère l'ajout d'un nouvel onglet (page) au tableau de bord. Deux comportements : si `$_POST['dashName']` absent, affiche un formulaire HTML ; si présent, crée la page avec 1, 2 ou 3 colonnes et sauvegarde dans les préférences utilisateur.

## Type
action / controller

## Dépendances clés
- `$current_user->getPreference/setPreference` — stockage préférences utilisateur
- `include/MySugar/retrieve_dash_page.php` — helper de récupération de page
- `Sugar_Smarty` — rendu template de la nouvelle page
- `$GLOBALS['app_strings']` — libellés

## Exports / Symboles principaux
Aucun (script procédural).

## Interactions
- **Appelé par :** action `AddDashboardPages` (`?module=Home&action=AddDashboardPages`)
- **Appelle :** `Sugar_Smarty`, `retrieve_dash_page.php`

## Notes
- Le nombre de colonnes détermine les largeurs (1: 100%, 2: 60%/40%, 3: 30%/30%/30%).
