# Fichier : Menu.php

**Chemin :** `modules/AOBH_BusinessHours/Menu.php`
**Type :** PHP — configuration (menu module)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le menu de navigation du module AOBH_BusinessHours (entrees Creer et Lister). Conditionne l'affichage selon les droits ACL de l'utilisateur courant.

## Parametres cles
- Lien "Creer" : `action=EditView` si acces `edit`
- Lien "Lister" : `action=index` si acces `list`

## Impacte par / impacte
- Charge par le framework SugarCRM a chaque acces au module
- `ACLController::checkAccess('AOBH_BusinessHours', 'edit'|'list', true)`

## Points d'attention
- RAS — fichier config standard de menu.
