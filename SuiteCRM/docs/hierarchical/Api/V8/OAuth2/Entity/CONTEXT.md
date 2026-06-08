# 📁 Entity

**Chemin :** `Api/V8/OAuth2/Entity/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier regroupe les entités OAuth2 de l'API V8. Ces classes sont les objets de valeur représentant les artefacts du protocole OAuth2 : jetons d'accès, jetons de rafraîchissement, codes d'autorisation, clients et utilisateurs. Elles forment le modèle de données du flux d'authentification.

## ⚙️ Responsabilité technique
Chaque entité implémente une interface de `league/oauth2-server` via composition de traits. Les classes sont minimalistes : aucune logique propre, tout le comportement provient des traits standards de la bibliothèque. Elles sont instanciées exclusivement par leurs repositories respectifs dans `Api/V8/OAuth2/Repository/`.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AccessTokenEntity.php` | Entité jeton d'accès OAuth2 — implémente `AccessTokenEntityInterface` via traits | [→ fiche](AccessTokenEntity.doc.md) |
| `AuthCodeEntity.php` | Entité code d'autorisation OAuth2 (flux `authorization_code`) via traits | [→ fiche](AuthCodeEntity.doc.md) |
| `ClientEntity.php` | Entité client OAuth2 avec setters pour injection des données depuis la DB | [→ fiche](ClientEntity.doc.md) |
| `RefreshTokenEntity.php` | Entité jeton de rafraîchissement OAuth2 via traits | [→ fiche](RefreshTokenEntity.doc.md) |
| `UserEntity.php` | Entité utilisateur OAuth2 portant uniquement l'identifiant SuiteCRM | [→ fiche](UserEntity.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `league/oauth2-server` (interfaces et traits d'entités)
- **Expose :** objets de valeur OAuth2 instanciés par `Api/V8/OAuth2/Repository/` et enregistrés dans le DI via `Api/V8/Config/services/middlewares.php`
- **Flux typique :** un repository OAuth2 crée une entité (ex: `new AccessTokenEntity()`) → la peuple via ses setters/traits → la retourne au serveur OAuth2 de la bibliothèque league.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle d'un access token | [`AccessTokenEntity.php`](AccessTokenEntity.doc.md) |
| Comprendre le modèle d'un client OAuth2 | [`ClientEntity.php`](ClientEntity.doc.md) |
| Comprendre la structure d'un utilisateur OAuth2 | [`UserEntity.php`](UserEntity.doc.md) |

---

## ⚠️ Zones INCONNU
- Aucun INCONNU notable — classes entièrement basées sur les traits standards `league/oauth2-server`.
