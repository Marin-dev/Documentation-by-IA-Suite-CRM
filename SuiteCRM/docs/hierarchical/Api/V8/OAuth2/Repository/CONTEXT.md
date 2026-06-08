# 📁 Repository

**Chemin :** `Api/V8/OAuth2/Repository/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les repositories OAuth2 de l'API V8. Ils gèrent la persistance et la validation de tous les artefacts du protocole OAuth2 : access tokens, refresh tokens, codes d'autorisation, clients, scopes et utilisateurs. Ces repositories font le pont entre la bibliothèque `league/oauth2-server` et la couche de données SuiteCRM (beans `OAuth2Clients`, `OAuth2Tokens`, `OAuth2AuthCodes`).

## ⚙️ Responsabilité technique
Chaque repository implémente une interface de `league/oauth2-server` (ex: `AccessTokenRepositoryInterface`). Les interactions avec la DB passent exclusivement par `BeanManager` qui encapsule `BeanFactory`. Les opérations de révocation utilisent le soft-delete SuiteCRM (`mark_deleted`).

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AccessTokenRepository.php` | Création, persistance, révocation et validation des access tokens OAuth2 | [→ fiche](AccessTokenRepository.doc.md) |
| `AuthCodeRepository.php` | Gestion du cycle de vie des codes d'autorisation (`authorization_code` grant) | [→ fiche](AuthCodeRepository.doc.md) |
| `ClientRepository.php` | Récupération et validation des clients OAuth2 (secret SHA-256, type de grant) | [→ fiche](ClientRepository.doc.md) |
| `RefreshTokenRepository.php` | Gestion des refresh tokens liés aux records `OAuth2Tokens` existants | [→ fiche](RefreshTokenRepository.doc.md) |
| `ScopeRepository.php` | Repository de scopes — implémentation minimale, scopes non filtrés | [→ fiche](ScopeRepository.doc.md) |
| `UserRepository.php` | Authentification utilisateur pour le flux `password` grant via beans SuiteCRM | [→ fiche](UserRepository.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\V8\BeanDecorator\BeanManager`, `Api\V8\OAuth2\Entity\*`, `league/oauth2-server` (interfaces), beans SuiteCRM `OAuth2Clients`, `OAuth2Tokens`, `OAuth2AuthCodes`, `Users`
- **Expose :** services OAuth2 injectés dans `AuthorizationServer` et `ResourceServer` via `Api/V8/Config/services/middlewares.php`
- **Flux typique :** une demande `/access_token` → `AuthorizationServer` appelle `ClientRepository::validateClient()` → `UserRepository::getUserEntityByUserCredentials()` → `AccessTokenRepository::persistNewAccessToken()` → token JWT retourné au client.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la persistance des access tokens | [`AccessTokenRepository.php`](AccessTokenRepository.doc.md) |
| Comprendre la validation des clients OAuth2 | [`ClientRepository.php`](ClientRepository.doc.md) |
| Comprendre l'authentification utilisateur (password grant) | [`UserRepository.php`](UserRepository.doc.md) |
| Comprendre pourquoi les scopes ne sont pas restrictifs | [`ScopeRepository.php`](ScopeRepository.doc.md) |

---

## ⚠️ Zones INCONNU
- `ScopeRepository` : implémentation stub — les scopes ne sont pas validés, à compléter si restriction des droits OAuth2 nécessaire.
- `AuthCodeRepository` : couplage direct avec `$_POST['confirmed']` — testabilité réduite.
- `ClientRepository` : secret SHA-256 sans sel — vérifier la politique de stockage des secrets côté `OAuth2Clients`.
- `UserRepository` : messages d'erreur exposent les identifiants en clair — risque d'information disclosure en mode debug.
