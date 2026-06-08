# 📄 controller.php

**Chemin :** `modules/OAuth2AuthCodes/controller.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Contrôleur du module OAuth2AuthCodes. Gère les deux actions du flux Authorization Code : affichage de la page de consentement et traitement de la réponse de consentement (approval/denial).

## Rôle technique

Classe `OAuth2AuthCodesController` héritant de `SugarController`. L'action `action_authorize_confirm` reconstruit la `AuthorizationRequest` depuis la session (via `OAuthCodeGrantManager`), valide l'anti-CSRF, et complète le flux OAuth2 via `League\OAuth2\Server\AuthorizationServer`. Utilise le conteneur DI Slim (`ContainerLoader`).

---

## Dépendances clés

- `OAuthCodeGrantManager` — gestion de la requête d'autorisation en session
- `Api\Core\Loader\ContainerLoader` — conteneur DI
- `League\OAuth2\Server\AuthorizationServer` — serveur OAuth2
- `Slim\App` — framework HTTP
- `SugarController` — classe parente

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2AuthCodesController` | classe | Contrôleur du flux Authorization Code |
| `action_Authorize()` | méthode | Affiche la vue de consentement |
| `action_authorize_confirm()` | méthode | Traite le consentement et complète le flux OAuth2 |

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM (actions `Authorize`, `authorize_confirm`)
- **Appelle :** `OAuthCodeGrantManager`, `AuthorizationServer`, `ContainerLoader`
- **Position dans le flux global :** étape centrale du flux Authorization Code — entre la page de login et l'émission du code

---

## Notes

- Si `confirmed === 'always'` ou `'once'`, l'autorisation est approuvée (ligne 87).
- Si `oauth2_authcode_logout === '1'`, la session est détruite après le flux (SSO logout).
- La réponse HTTP est envoyée via `$app->respond($response)` (Slim).
