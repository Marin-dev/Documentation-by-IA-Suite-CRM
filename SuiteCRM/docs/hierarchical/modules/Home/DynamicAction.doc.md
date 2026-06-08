# DynamicAction.php

**Chemin :** `modules/Home/DynamicAction.php`
**Type :** PHP - Script AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Script AJAX permettant d'invoquer dynamiquement une méthode de la classe `MySugar` (ex. `displayDashlet`, `saveDashletOrdering`, etc.) via `$_REQUEST['DynamicAction']`. Utilisé pour les opérations de tableau de bord sans rechargement de page.

## Type
controller / script AJAX

## Dépendances clés
- `include/MySugar/MySugar.php` — classe `MySugar`

## Exports / Symboles principaux
Aucun (script procédural).

## Interactions
- **Appelé par :** JavaScript de la page Home (AJAX)
- **Appelle :** `MySugar::$dynamicAction()` (méthode dynamique)

## Notes
- Appel dynamique via `$mySugar->$dynamicAction()` — risque si `DynamicAction` n'est pas filtré correctement en amont.
- `session_write_close()` si `$_REQUEST['commit_session']` est présent (sérialisation des requêtes AJAX).
