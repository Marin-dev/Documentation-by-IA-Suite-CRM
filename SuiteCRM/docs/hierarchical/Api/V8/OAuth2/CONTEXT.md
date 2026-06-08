# 📁 OAuth2

**Chemin :** `Api/V8/OAuth2/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier implémente la couche OAuth2 de l'API V8 SuiteCRM. Il contient les entités représentant les artefacts OAuth2 (tokens, clients, utilisateurs) et les repositories gérant leur persistance/validation en base de données SuiteCRM.

## ⚙️ Responsabilité technique
Deux sous-dossiers : `Entity/` (objets de valeur OAuth2 basés sur les traits de `league/oauth2-server`) et `Repository/` (services implémentant les interfaces de persistance de `league/oauth2-server`). Les repositories sont injectés dans les serveurs OAuth2 (`AuthorizationServer`, `ResourceServer`) configurés dans `middlewares.php`. Les clés cryptographiques RSA (`private.key`, `public.key`) sont aussi stockées ici.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Entity/` | Entités OAuth2 (access token, refresh token, auth code, client, utilisateur) — objets de valeur via traits league | [→ CONTEXT](Entity/CONTEXT.md) |
| `Repository/` | Repositories OAuth2 : persistance, révocation et validation des tokens/clients/utilisateurs via beans SuiteCRM | [→ CONTEXT](Repository/CONTEXT.md) |

### Fichiers documentés
Aucun fichier direct dans ce dossier (les clés `private.key`/`public.key` ne sont pas documentées car fichiers de configuration, non du code).

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `private.key` | Fichier de clé cryptographique RSA — pas de code à documenter |
| `public.key` | Fichier de clé cryptographique RSA — pas de code à documenter |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `league/oauth2-server`, `Api\V8\BeanDecorator\BeanManager`, beans SuiteCRM `OAuth2Clients`, `OAuth2Tokens`, `OAuth2AuthCodes`, `Users`
- **Expose :** repositories injectés dans `AuthorizationServer`/`ResourceServer` via `Api/V8/Config/services/middlewares.php`
- **Flux typique :** client POST `/access_token` → `AuthorizationServer` → `ClientRepository::validateClient()` → `UserRepository::getUserEntityByUserCredentials()` → `AccessTokenRepository::persistNewAccessToken()` → JWT retourné.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la persistance des access tokens | [`Repository/`](Repository/CONTEXT.md) |
| Comprendre les modèles de données OAuth2 | [`Entity/`](Entity/CONTEXT.md) |
| Comprendre la validation des clients OAuth2 | [`Repository/ClientRepository.php`](Repository/ClientRepository.doc.md) |

---

## ⚠️ Zones INCONNU
- Scopes OAuth2 non implémentés (`ScopeRepository` stub) — restriction des droits non opérationnelle.
- Clés RSA doivent exister avant déploiement — processus de génération INCONNU.
