# 📁 OAuthKeys

**Chemin :** `modules/OAuthKeys/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module OAuthKeys gère les clés consommateurs OAuth 1.0 dans SuiteCRM (distinctes de l'OAuth 2.0 géré par OAuth2Clients). Il permet aux administrateurs d'enregistrer des paires clé/secret consommateur pour des applications tierces utilisant le protocole OAuth 1.0. La suppression d'une clé entraîne la suppression de tous les tokens associés.

## ⚙️ Responsabilité technique
La classe `OAuthKey` étend `Basic` (et non directement `SugarBean`) et persiste dans la table `oauth_consumer`. Elle fournit un cache statique (`$keys_cache`) pour optimiser les lookups répétés. `fetchKey()` charge une clé par sa valeur consumer key avec mise en cache. `mark_deleted()` effectue des suppressions directes en base (DELETE SQL) plutôt que du soft delete, cascadant aux tokens dans `oauth_tokens`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `metadata/` | Définitions de vues (list, detail, edit, search, subpanel) | Pas de CONTEXT.md |
| `language/` | Traductions | Pas de CONTEXT.md |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `OAuthKey.php` | Modèle de clé consommateur OAuth 1.0 avec cache et suppression en cascade | Pas de fiche |
| `controller.php` | Contrôleur du module | Pas de fiche |
| `vardefs.php` | Définition des champs (c_key, c_secret, name) | Pas de fiche |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `Menu.php` | Non présent dans la liste des fichiers du module |
| `metadata/metafiles.php` | Registre de métadonnées standard |
| `metadata/subpaneldefs.php` | Définition du sous-panneau tokens associés |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Classe `Basic` (parent), `BeanFactory::registerBean()` (enregistrement en cache global), table `oauth_tokens` (suppression en cascade).
- **Expose :** Table `oauth_consumer`, méthode statique `OAuthKey::fetchKey($key)` utilisée par `OAuthToken` et le provider Zend OAuth (`SuiteCRM\Zend_Oauth_Provider`).
- **Flux typique :** Application tierce OAuth 1.0 → présente sa consumer key → `OAuthKey::fetchKey()` récupère la clé avec son secret → validation HMAC de la signature → génération/validation du token via `OAuthTokens`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle de la clé consommateur OAuth 1.0 | [`OAuthKey.php`](OAuthKey.php) |
| Voir les champs disponibles | [`vardefs.php`](vardefs.php) |
| Comprendre la relation avec les tokens | [`metadata/subpaneldefs.php`](metadata/subpaneldefs.php) |

---

## ⚠️ Zones INCONNU
- La classe `Basic` dont hérite `OAuthKey` : son emplacement et ses fonctionnalités sont non documentés ici.
- Mécanisme de chiffrement/déchiffrement du `c_secret` (mentionné `check_date_relationships_load()` dans `getByKey()`) : INCONNU.
