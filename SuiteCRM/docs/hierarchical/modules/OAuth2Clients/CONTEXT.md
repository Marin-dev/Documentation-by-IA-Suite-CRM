# 📁 OAuth2Clients

**Chemin :** `modules/OAuth2Clients/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OAuth2Clients gère l'enregistrement et la configuration des clients OAuth 2.0 dans SuiteCRM. Il permet aux administrateurs de créer et gérer des applications tierces autorisées à accéder à l'API V8 via les différents flux OAuth2 (Authorization Code, Client Credentials, Password). Chaque client dispose d'un secret, d'une URI de redirection, d'un type de grant autorisé et d'une durée de validité des tokens.

## ⚙️ Responsabilité technique
La classe `OAuth2Clients` étend `SugarBean` (table `oauth2clients`). La méthode `save()` hache le secret via `hash('sha256', ...)` et calcule `duration_value` en secondes selon l'unité choisie. Des métadonnées spécifiques existent pour chaque type de grant (Authorization Code, Client Credentials, Password) : `detailauthorizationcodeviewdefs.php`, `detailcredentialsviewdefs.php`, etc. Les vues `view.edit.php` et `view.detail.php` sélectionnent la bonne définition selon le type de client.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `metadata/` | Définitions de vues multiples selon le type de grant OAuth2 | Pas de CONTEXT.md |
| `views/` | Vues édition/détail adaptées au type de client | Pas de CONTEXT.md |
| `js/` | Validation JavaScript côté client par type de grant | Pas de CONTEXT.md |
| `language/` | Traductions | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OAuth2Clients.php` | Modèle SugarBean du client OAuth2 avec hachage secret et calcul durée | Pas de fiche |
| `controller.php` | Contrôleur du module | Pas de fiche |
| `vardefs.php` | Définition des champs (secret, redirect_uri, allowed_grant_type, duration) | Pas de fiche |
| `views/view.edit.php` | Vue édition adaptée au type de grant | Pas de fiche |
| `views/view.detail.php` | Vue détail adaptée au type de grant | Pas de fiche |
| `js/ClientCredentialsValidation.js` | Validation JS pour le flux Client Credentials | Pas de fiche |
| `js/PasswordCredentialsValidation.js` | Validation JS pour le flux Password | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Menu standard |
| `metadata/metafiles.php` | Registre des métadonnées standard |
| `metadata/popupdefs.php` | Définition popup standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean` (persistance), `hash()` PHP natif (hachage SHA256 du secret).
- **Expose :** Table `oauth2clients`, référencée par `OAuth2AuthCodes` (champ `client`), `OAuth2Tokens` (champ `client`), et `SuiteCRM\Api\V8\OAuth2\Repository\ClientRepository`.
- **Flux typique :** Admin crée un client → choisit le type de grant → saisit secret + redirect_uri → `save()` hache le secret → le client est utilisable par `ClientRepository` pour valider les requêtes OAuth2 entrantes.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle de données d'un client OAuth2 | [`OAuth2Clients.php`](OAuth2Clients.php) |
| Comprendre comment le secret est stocké | `save()` dans [`OAuth2Clients.php`](OAuth2Clients.php) |
| Modifier la vue selon le type de grant | [`views/view.edit.php`](views/view.edit.php) |
| Voir les champs disponibles | [`vardefs.php`](vardefs.php) |

---

## ⚠️ Zones INCONNU
- Le champ `secret` est stocké haché (SHA256) : la validation lors de l'authentification se fait dans `ClientRepository` (Api/V8) — lien non tracé ici.
- Gestion de la rotation du secret : INCONNU (semble uniquement possible via `new_secret` au save).
