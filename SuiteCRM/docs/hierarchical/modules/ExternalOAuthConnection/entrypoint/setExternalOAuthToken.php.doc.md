# 📄 setExternalOAuthToken.php

**Chemin :** `modules/ExternalOAuthConnection/entrypoint/setExternalOAuthToken.php`
**Type :** PHP — entrypoint (callback OAuth)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Point d'entrée HTTP servant de callback OAuth (redirect_uri). Reçoit le code d'autorisation et le state depuis le fournisseur tiers, valide le state anti-CSRF, échange le code contre un access token, et affiche le token via un template Smarty (pour transmission à l'UI parent).

## Rôle technique

Fichier procédural. Valide `$_GET['state']` contre `$_SESSION['oauth2state']`. Appelle `OAuthAuthorizationService::getAccessToken()` puis `mapToken()`. Rendu via `Sugar_Smarty` + template `tpl/setToken.tpl`.

---

## Dépendances clés

- `include/entryPoint.php` — bootstrap SuiteCRM
- `OAuthAuthorizationService` — service d'autorisation
- `Sugar_Smarty` — rendu du template
- `$_GET['code']` — code d'autorisation OAuth
- `$_GET['state']` / `$_SESSION['oauth2state']` — validation anti-CSRF
- `$_SESSION['provider']` — fallback pour l'ID fournisseur

---

## Relations clés

- **Appelé par :** fournisseur OAuth externe (Google/Microsoft) via redirect_uri
- **Appelle :** `OAuthAuthorizationService::getAccessToken()`, `mapToken()`, `Sugar_Smarty`
- **Position dans le flux global :** étape 2 du flux OAuth externe — reçoit le code et l'échange contre un token

---

## Notes

- Template `tpl/setToken.tpl` INCONNU — probablement un script JS qui transmet le token à la fenêtre parente (popup flow).
- Validation du state par égalité stricte (ligne 62) — protection CSRF correcte.
- Les paramètres GET sont loggés au niveau debug (ligne 70) — peut exposer des codes sensibles dans les logs.
