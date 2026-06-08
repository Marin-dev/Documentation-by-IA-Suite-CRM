# Fichier : Menu.php

**Chemin :** `modules/Schedulers/Menu.php`
**Type :** PHP — configuration (menu module)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le menu de navigation du module Schedulers (liens Creer, Lister). Conditionne l'affichage des entrees selon les droits ACL.

## Parametres cles
- Lien "Creer" : `action=EditView` si acces `edit`
- Lien "Liste" : `action=index` si acces `list`

## Impacte par / impacte
- Charge par le framework SugarCRM a chaque acces au module
- Conditionne par `ACLController::checkAccess()`

## Points d'attention
- RAS — fichier config standard.
