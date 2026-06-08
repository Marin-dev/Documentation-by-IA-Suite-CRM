# 📁 OAuthTokens

**Chemin :** `modules/OAuthTokens/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OAuthTokens gère les tokens du protocole OAuth 1.0 dans SuiteCRM (à distinguer des tokens OAuth 2.0 dans OAuth2Tokens). Il couvre le cycle de vie complet des tokens OAuth 1.0 : token de requête, autorisation utilisateur, échange contre un token d'accès. Il fournit également la page de consentement utilisateur et gère la validation des nonces pour prévenir les attaques de rejeu.

## ⚙️ Responsabilité technique
La classe `OAuthToken` étend `SugarBean` (table `oauth_tokens`) et implémente les états de token via des constantes (`REQUEST = 1`, `ACCESS = 2`, `INVALID = 3`). Elle fournit des méthodes statiques : `generate()` (création aléatoire), `load()` (chargement par ID), `createAuthorized()` (bypass du flux OAuth), `cleanup()` (nettoyage des tokens périmés). `checkNonce()` gère la table `oauth_nonce` pour la protection anti-rejeu. `mark_deleted()` effectue une suppression directe (hard delete) en SQL.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `metadata/subpanels/` | Sous-panneaux (tokens par clé, tokens par utilisateur) | Pas de CONTEXT.md |
| `tpl/` | Templates de la page d'autorisation OAuth 1.0 | Pas de CONTEXT.md |
| `views/` | Vue de la page d'autorisation | Pas de CONTEXT.md |
| `language/` | Traductions | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OAuthToken.php` | Modèle complet du token OAuth 1.0 avec gestion d'état et nonce | Pas de fiche |
| `controller.php` | Contrôleur du module | Pas de fiche |
| `vardefs.php` | Définition des champs (token, secret, tstate, consumer, verify) | Pas de fiche |
| `views/view.authorize.php` | Page de consentement utilisateur OAuth 1.0 | Pas de fiche |
| `action_view_map.php` | Mapping actions/vues du module | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `tpl/authorize.tpl` | Template HTML de la page d'autorisation |
| `tpl/authorized.tpl` | Template de confirmation d'autorisation |
| `metadata/subpanels/ForKeys.php` | Sous-panneau standard |
| `metadata/subpanels/ForUser.php` | Sous-panneau standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (persistance), `OAuthKeys/OAuthKey.php` (via `require_once`), `SuiteCRM\Zend_Oauth_Provider` (génération de tokens aléatoires et validation), `DBManagerFactory` (requêtes directes sur `oauth_nonce`).
- **Expose :** Table `oauth_tokens`, table `oauth_nonce`, méthodes statiques `OAuthToken::load()`, `generate()`, `createAuthorized()`, `checkNonce()` utilisées par le provider Zend OAuth.
- **Flux typique :** Client OAuth 1.0 → demande token de requête (`generate()`) → redirect vers page d'autorisation (`view.authorize`) → utilisateur accepte → `authorize()` génère le verifier → client échange contre token d'accès → accès API avec validation nonce.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le cycle de vie d'un token OAuth 1.0 | [`OAuthToken.php`](OAuthToken.php) |
| Comprendre la page d'autorisation | [`views/view.authorize.php`](views/view.authorize.php) |
| Comprendre la protection anti-rejeu (nonce) | `checkNonce()` dans [`OAuthToken.php`](OAuthToken.php) |
| Créer un token d'accès sans flux OAuth (bypass) | `OAuthToken::createAuthorized()` dans [`OAuthToken.php`](OAuthToken.php) |

---

## ⚠️ Zones INCONNU
- Différence de périmètre exact entre `OAuthTokens` (OAuth 1.0) et `OAuth2Tokens` (OAuth 2.0) dans les cas d'usage réels de SuiteCRM : documentation incomplète.
- La table `oauth_nonce` n'est jamais nettoyée que partiellement (DELETE WHERE nonce_ts < ts courant) : risque de croissance non documenté.
