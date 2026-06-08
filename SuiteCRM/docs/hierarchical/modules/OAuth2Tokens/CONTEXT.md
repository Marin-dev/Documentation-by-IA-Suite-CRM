# 📁 OAuth2Tokens

**Chemin :** `modules/OAuth2Tokens/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OAuth2Tokens gère les tokens d'accès et de rafraîchissement OAuth 2.0 de l'API V8 de SuiteCRM. Il stocke les access tokens et refresh tokens émis aux clients OAuth2 autorisés, gère leur révocation individuelle ou en masse, et contrôle leur expiration. Les administrateurs peuvent consulter et révoquer les tokens via l'interface.

## ⚙️ Responsabilité technique
La classe `OAuth2Tokens` étend `SugarBean` (table `oauth2tokens`) avec `disable_row_level_security = true`. Elle surcharge `create_new_list_query()` pour filtrer les tokens par utilisateur courant (sauf admin). Elle stocke `access_token`, `refresh_token`, leurs dates d'expiration, les `scopes`, le client associé et le `token_type`. `OAuthTokenMarkDeletedService` gère le nettoyage. `RevokeBulk.js` permet la révocation en masse depuis l'interface.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `metadata/` | Définitions de vues (list, detail, search, subpanel) | Pas de CONTEXT.md |
| `service/` | Service de nettoyage/révocation des tokens | Pas de CONTEXT.md |
| `include/` | Scripts JS pour la révocation en masse | Pas de CONTEXT.md |
| `language/` | Traductions | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OAuth2Tokens.php` | Modèle SugarBean des tokens OAuth2 (access + refresh) | Pas de fiche |
| `controller.php` | Contrôleur du module | Pas de fiche |
| `vardefs.php` | Définition des champs (tokens, expiration, scopes, client) | Pas de fiche |
| `service/OAuthTokenMarkDeletedService.php` | Service de révocation et nettoyage des tokens | Pas de fiche |
| `include/RevokeBulk.js` | JavaScript pour révocation en masse de tokens | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |
| `metadata/metafiles.php` | Registre des métadonnées |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (persistance), `OAuth2Clients` (référence client), `SuiteCRM\Api\V8\OAuth2\Repository\AccessTokenRepository` et `RefreshTokenRepository` (utilisent ce module).
- **Expose :** Table `oauth2tokens`, interface d'administration des tokens, méthodes de révocation via `OAuthTokenMarkDeletedService`.
- **Flux typique :** Après échange du code ou credentials → `AccessTokenRepository` crée un enregistrement `OAuth2Tokens` → l'API valide les requêtes en vérifiant le token → admin peut révoquer depuis l'interface via `RevokeBulk.js`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle de données du token | [`OAuth2Tokens.php`](OAuth2Tokens.php) |
| Comprendre la révocation de tokens | [`service/OAuthTokenMarkDeletedService.php`](service/OAuthTokenMarkDeletedService.php) |
| Implémenter la révocation en masse | [`include/RevokeBulk.js`](include/RevokeBulk.js) |
| Voir les champs stockés | [`vardefs.php`](vardefs.php) |

---

## ⚠️ Zones INCONNU
- Les tokens sont-ils stockés hachés ou en clair dans la table ? : non confirmé sans lecture de `AccessTokenRepository`.
- Durée de vie effective des tokens : dépend de `OAuth2Clients.duration_value`, lien exact non tracé.
