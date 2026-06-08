# Fichier : LoggedOut.php

**Chemin :** `modules/Users/LoggedOut.php`
**Type :** PHP — Vue (page deconnexion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la page de confirmation de deconnexion. Si l'utilisateur est encore authentifie en session, le redirige immediatement vers la page d'accueil.

## Role technique

Script procedural. Verifie `$_SESSION['authenticated_user_id']` : si present, redirige via `$GLOBALS['app']->getLoginRedirect()`. Sinon, instancie `Sugar_Smarty` et affiche `LoggedOut.tpl` avec le lien de reconnexion et la feuille de style login.

---

## Dependances principales

| Dependance | Role |
|---|---|
| `Sugar_Smarty` | Affichage template |
| `$GLOBALS['app']` | Redirection si encore connecte |
| `getJSPath()` | URL versionnee de `login.css` |

## Exports / Symboles principaux

Aucun. Produit HTML ou redirection.

---

## Relations cles

- **Appele par :** routeur CRM (`action=LoggedOut`) — generalement apres `Logout.php`
- **Affiche :** `modules/Users/LoggedOut.tpl`
