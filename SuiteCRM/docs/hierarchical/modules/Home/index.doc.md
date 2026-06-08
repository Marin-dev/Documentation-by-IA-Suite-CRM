# index.php

**Chemin :** `modules/Home/index.php`
**Type :** PHP - Vue principale (script d'affichage)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Point d'entrée de la page d'accueil SuiteCRM (tableau de bord). Charge les préférences de l'utilisateur courant (pages et dashlets), instancie chaque dashlet, construit la structure de colonnes et transmet tout à Smarty pour rendu via `MySugar.tpl`.

## Type
view / script d'affichage

## Dépendances clés
- `include/MySugar/MySugar.php` — classe `MySugar`, vérifie l'affichage des dashlets
- `include/Dashlets/DashletCacheBuilder.php` — construction du cache des dashlets
- `modules/Home/dashlets.php` — liste `$defaultDashlets`
- `include/SuiteGraphs/RGraphIncludes.php` — ressources graphiques
- `include/SugarCharts/SugarChartFactory.php` — ressources chartes JS
- `Sugar_Smarty` — moteur de template
- `$current_user->getPreference/setPreference` (global)

## Exports / Symboles principaux
- Aucun export de classe ou fonction ; script procédural qui produit le HTML du dashboard via Smarty.

## Interactions
- **Appelé par :** `modules/Home/views/view.list.php` (via `include`)
- **Appelle :** dashlets individuels (chargés dynamiquement via `$dashletsFiles`), `MySugar`, `Sugar_Smarty`

## Notes
- Logique de migration depuis l'ancien module `Dashboard` (versions pré-5.0) : lignes 156-174.
- Si `$sugar_config['lock_homepage']` est `true`, la page est verrouillée (pas de modification).
- `max_dashlets_homepage` (config) limite le nombre de dashlets (défaut : 15).
- Les dashlets peuvent implémenter `shouldDisplay()` pour se masquer dynamiquement.
