# 📄 OAuthToken.php

**Chemin :** `modules/OAuthTokens/OAuthToken.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle des tokens OAuth 1.0 (request tokens et access tokens). Gère le cycle de vie complet d'un token : génération aléatoire, autorisation par un utilisateur, échange request→access, invalidation, nettoyage des tokens expirés et vérification des nonces anti-replay.

## Rôle technique

Classe `OAuthToken` héritant de `SugarBean` (table `oauth_tokens`). Implémente les 3 états du token (REQUEST=1, ACCESS=2, INVALID=3). La clé primaire est le token lui-même (pas un UUID standard). Fournit des méthodes statiques de factory et de nettoyage.

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `modules/OAuthKeys/OAuthKey.php` (require_once) — association clé consommateur
- `BeanFactory::getBean('OAuthKeys', ...)` — chargement du consommateur
- `SuiteCRM\Zend_Oauth_Provider` — génération de tokens aléatoires, vérification nonce
- `DBManagerFactory` — nettoyage et vérification nonce

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuthToken` | classe | Modèle token OAuth 1.0 |
| `REQUEST`, `ACCESS`, `INVALID` | constantes | États du token |
| `generate()` | méthode statique | Crée un token aléatoire (token + secret) |
| `load($token)` | méthode statique | Charge un token existant par ID |
| `createAuthorized($consumer, $user)` | méthode statique | Crée un access token directement (bypass OAuth flow) |
| `authorize($authdata)` | méthode | Autorise un request token → génère un verifier |
| `invalidate()` | méthode | Invalide le token |
| `copyAuthData(OAuthToken)` | méthode | Copie les données d'autorisation entre tokens |
| `checkNonce($key, $nonce, $ts)` | méthode statique | Vérifie l'unicité du nonce (anti-replay) |
| `cleanup()` | méthode statique | Supprime les tokens INVALID/REQUEST de plus de 24h |
| `deleteByConsumer($consumer_id)` | méthode statique | Supprime tous les tokens d'un consommateur |
| `deleteByUser($user_id)` | méthode statique | Supprime tous les tokens d'un utilisateur |
| `displayDateFromTs()` | fonction globale | Formate un timestamp Unix pour l'affichage (utilisé dans les vues) |

---

## Relations clés

- **Appelé par :** serveur OAuth 1.0 SuiteCRM (SOAP/REST legacy), `modules/OAuthTokens/views/view.authorize.php`
- **Appelle :** `OAuthKey::fetchKey()`, `Zend_Oauth_Provider`, `DBManagerFactory`
- **Position dans le flux global :** authentification OAuth 1.0, précède chaque appel API SOAP authentifié

---

## Notes

- La clé primaire dans `oauth_tokens` est le token lui-même (ligne 142-143 : `$this->id = $this->token`).
- Les suppressions sont physiques (DELETE) — pas de soft delete.
- `checkNonce()` utilise une table dédiée `oauth_nonce` — les nonces sont supprimés en rolling après chaque appel.
- `createAuthorized()` permet de bypasser le flux OAuth standard — utilisé pour les intégrations système.
