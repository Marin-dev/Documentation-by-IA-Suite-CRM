# 📄 services.php

**Chemin :** `Api/V8/Config/services.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Fichier d'agrégation de la configuration du conteneur d'injection de dépendances (IoC) de l'API V8. Il fusionne toutes les définitions de services partielles en un seul tableau retourné au conteneur Slim. Il déclare également deux services transversaux : `foundHandler` (stratégie d'invocation) et `BeanManager`.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Service central d'accès aux beans SuiteCRM |
| `Api\V8\Controller\InvocationStrategy\SuiteInvocationStrategy` | Stratégie d'invocation des contrôleurs Slim |
| `Psr\Container\ContainerInterface` | Interface du conteneur PSR-11 |
| `Api\Core\Loader\CustomLoader` | Fusion avec les définitions personnalisées |

---

## Fichiers agrégés

Ce fichier `require` les sous-fichiers suivants et fusionne leurs tableaux :

| Fichier | Contenu |
|---|---|
| `services/beanAliases.php` | Aliases module → classe bean |
| `services/controllers.php` | Définitions des contrôleurs |
| `services/factories.php` | Définitions des factories |
| `services/globals.php` | Variables globales (config, DB) |
| `services/helpers.php` | Helpers (VarDef, Attribute, Pagination...) |
| `services/middlewares.php` | Serveurs OAuth2 (Authorization + Resource) |
| `services/params.php` | Classes de paramètres de routes |
| `services/services.php` | Services métier |
| `services/validators.php` | Validateur Symfony |

---

## Exports / Symboles principaux

- Retourne un tableau PHP (array) de définitions DI consommé par le conteneur Slim.
- `foundHandler` — remplace le handler par défaut de Slim par `SuiteInvocationStrategy`
- `BeanManager::class` — instancié avec `DBManager` et `beanAliases`

---

## Interactions

- **Appelé par :** point d'entrée applicatif (INCONNU — probablement `Api/entryPoint.php` lors de la construction du conteneur Slim)
- **Appelle :** les 9 fichiers de services partiels + `CustomLoader::mergeCustomArray`
- **Position dans le flux :** configuration initiale au démarrage de l'application, avant tout traitement de requête

---

## Notes

- `CustomLoader::mergeCustomArray` permet aux projets clients de surcharger les services sans modifier ce fichier (extension point).
- La surcharge de `foundHandler` est nécessaire pour adapter le comportement d'invocation de Slim aux contrôleurs SuiteCRM.
- `DBManager::class` référencé dans la factory de `BeanManager` mais non importé dans ce fichier — il est attendu globalement dans l'environnement PHP (classe SuiteCRM native).
