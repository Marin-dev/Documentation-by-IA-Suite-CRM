# 📁 services

**Chemin :** `Api/V8/Config/services/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les fichiers de configuration partielle du conteneur d'injection de dépendances (DI) de l'API V8. Chaque fichier déclare un segment du conteneur : contrôleurs, services métier, factories, helpers, middlewares OAuth2, paramètres de routes, validateurs et globales PHP.

## ⚙️ Responsabilité technique
Chaque fichier retourne un tableau PHP de définitions DI (closures) agrégé par `Api/V8/Config/services.php`. Ils utilisent tous `CustomLoader::mergeCustomArray` pour permettre la surcharge sans modification du core. Le point de chargement est `ContainerLoader::configure()` au démarrage de l'application.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `beanAliases.php` | Table de correspondance FQCN/alias → nom de module SuiteCRM injectée dans `BeanManager` | [→ fiche](beanAliases.php.doc.md) |
| `controllers.php` | Enregistrement de tous les contrôleurs V8 avec leurs services injectés | [→ fiche](controllers.php.doc.md) |
| `factories.php` | Enregistrement des factories `ParamsMiddlewareFactory` et `ValidatorFactory` | [→ fiche](factories.php.doc.md) |
| `globals.php` | Exposition de `$sugar_config` et `DBManager` comme services DI | [→ fiche](globals.php.doc.md) |
| `helpers.php` | Enregistrement des helpers JSON:API (attributs, relations, pagination, modules) | [→ fiche](helpers.php.doc.md) |
| `middlewares.php` | Configuration des serveurs OAuth2 `AuthorizationServer` et `ResourceServer` avec les 4 grants | [→ fiche](middlewares.php.doc.md) |
| `params.php` | Enregistrement des classes `Param\*` pour la validation de chaque route | [→ fiche](params.php.doc.md) |
| `services.php` | Enregistrement des 8 services métier V8 avec leurs dépendances injectées | [→ fiche](services.php.doc.md) |
| `validators.php` | Enregistrement du validateur Symfony sous la clé `'Validation'` | [→ fiche](validators.php.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Api\Core\Loader\CustomLoader` (pour les surcharges), `league/oauth2-server`, `Symfony\Component\Validator`, `Api\V8\BeanDecorator\BeanManager`, toutes les classes contrôleurs/services/helpers/params de V8
- **Expose :** tableau de définitions DI consommé par `Api/V8/Config/services.php` (fichier parent)
- **Flux typique :** au démarrage, `ContainerLoader` charge `services.php` qui agrège ces 9 fichiers → le conteneur Slim est peuplé de toutes les dépendances.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la configuration OAuth2 (grants, clés) | [`middlewares.php`](middlewares.php.doc.md) |
| Ajouter un nouveau contrôleur dans le DI | [`controllers.php`](controllers.php.doc.md) |
| Ajouter un nouveau service métier | [`services.php`](services.php.doc.md) |
| Comprendre le mapping modules/beans | [`beanAliases.php`](beanAliases.php.doc.md) |
| Ajouter un nouveau paramètre de route | [`params.php`](params.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `globals.php` : légère incohérence — `suiteConfig` exposé dans le DI mais `middlewares.php` accède à `$GLOBALS['sugar_config']` directement.
- `validators.php` : `include_once` manuel inhabituel — possible dette technique d'autoloading.
- `middlewares.php` : fallback `'SCRM-DEFK'` si `oauth2_encryption_key` absent — risque sécurité majeur en production.
