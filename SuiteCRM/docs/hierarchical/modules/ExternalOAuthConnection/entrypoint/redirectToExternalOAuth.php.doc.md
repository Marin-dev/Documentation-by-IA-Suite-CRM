# 📄 redirectToExternalOAuth.php

**Chemin :** `modules/ExternalOAuthConnection/entrypoint/redirectToExternalOAuth.php`
**Type :** PHP — entrypoint
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Point d'entrée HTTP qui initie le flux d'autorisation OAuth externe. Reçoit l'ID du fournisseur et les credentials depuis `$_GET`, vérifie que le fournisseur existe, stocke l'ID en session et redirige l'utilisateur vers l'URL d'autorisation du fournisseur tiers.

## Rôle technique

Fichier procédural. Instancie `OAuthAuthorizationService`, vérifie le fournisseur via `hasProvider()`, puis appelle `authorizationRedirect()` qui émet un header `Location:`.

---

## Dépendances clés

- `include/entryPoint.php` — bootstrap SuiteCRM
- `OAuthAuthorizationService` — service d'autorisation
- `$_GET['provider']`, `$_GET['clientId']`, `$_GET['clientSecret']` — paramètres d'entrée
- `$_SESSION['provider']` — persistance de l'ID fournisseur

---

## Relations clés

- **Appelé par :** UI SuiteCRM (bouton "Autoriser" sur ExternalOAuthConnection/Provider)
- **Appelle :** `OAuthAuthorizationService::hasProvider()`, `authorizationRedirect()`
- **Position dans le flux global :** étape 1 du flux OAuth externe — déclenche la redirection vers Google/Microsoft/etc.

---

## Notes

- `clientId` et `clientSecret` passés en GET — attention à la sécurité (HTTPS requis).
- En cas d'erreur, log fatal + `exit()` sans redirection.
