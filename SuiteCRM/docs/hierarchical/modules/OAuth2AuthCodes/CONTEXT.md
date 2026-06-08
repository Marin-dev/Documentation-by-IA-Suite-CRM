# 📁 OAuth2AuthCodes

**Chemin :** `modules/OAuth2AuthCodes/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OAuth2AuthCodes gère les codes d'autorisation OAuth 2.0 dans le cadre du flux Authorization Code Grant de l'API V8 de SuiteCRM. Il stocke les codes d'autorisation temporaires générés lors du processus d'authentification OAuth2, vérifie leur validité (expiration, révocation, scope) et fournit l'interface d'autorisation utilisateur.

## ⚙️ Responsabilité technique
La classe `OAuth2AuthCodes` étend `SugarBean` avec `disable_row_level_security = true`. Elle persiste dans la table `oauth2authcodes`. Elle implémente `is_revoked()` (vérifie expiration et flag de révocation) et `is_scope_authorized()` (vérifie si le client/user a déjà autorisé). `OAuthCodeGrantManager` orchestre le flux Authorization Code avec la librairie `League\OAuth2\Server`. `OAuthCodeMarkDeletedService` nettoie les codes expirés. La vue `view.authorize.php` affiche la page de consentement utilisateur.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `services/` | Services métier : gestion du grant Authorization Code et nettoyage des codes | Pas de CONTEXT.md |
| `views/` | Vues MVC (liste, page d'autorisation) | Pas de CONTEXT.md |
| `metadata/` | Définitions de vues (list, search) | Pas de CONTEXT.md |
| `tpl/` | Template Smarty de la page d'autorisation OAuth | Pas de CONTEXT.md |
| `language/` | Traductions | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OAuth2AuthCodes.php` | Modèle SugarBean des codes d'autorisation OAuth2 | Pas de fiche |
| `controller.php` | Contrôleur du module | Pas de fiche |
| `vardefs.php` | Définition des champs (auth_code, scopes, state, expires, client) | Pas de fiche |
| `services/OAuthCodeGrantManager.php` | Orchestration du flux Authorization Code Grant | Pas de fiche |
| `services/OAuthCodeMarkDeletedService.php` | Nettoyage des codes expirés/révoqués | Pas de fiche |
| `views/view.authorize.php` | Page de consentement utilisateur OAuth2 | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |
| `metadata/listviewdefs.php` | Définition de vue liste standard |
| `metadata/searchdefs.php` | Définition de recherche standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `League\OAuth2\Server\AuthorizationServer` (librairie OAuth2), `Api\V8\OAuth2\Entity\UserEntity`, `SugarBean` (persistance), `OAuth2Clients` (référence client).
- **Expose :** Table `oauth2authcodes`, page de consentement `/index.php?module=OAuth2AuthCodes&action=authorize`, méthodes `is_revoked()` et `is_scope_authorized()` utilisées par les repositories OAuth2.
- **Flux typique :** Client API → redirect vers page d'autorisation (`view.authorize`) → utilisateur consent → `OAuthCodeGrantManager` génère et persiste le code → redirect vers client avec code → échange du code contre token (`OAuth2Tokens`).

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle de données du code d'autorisation | [`OAuth2AuthCodes.php`](OAuth2AuthCodes.php) |
| Comprendre le flux Authorization Code Grant | [`services/OAuthCodeGrantManager.php`](services/OAuthCodeGrantManager.php) |
| Modifier la page de consentement | [`views/view.authorize.php`](views/view.authorize.php) |
| Nettoyer les codes expirés | [`services/OAuthCodeMarkDeletedService.php`](services/OAuthCodeMarkDeletedService.php) |

---

## ⚠️ Zones INCONNU
- Mécanisme de stockage du code (hashé ou en clair dans la table) : non confirmé sans lecture complète de `OAuthCodeGrantManager`.
- Lien exact avec `AuthCodeRepository` dans `SuiteCRM\Api\V8\OAuth2\Repository\` : INCONNU sans traçage complet.
