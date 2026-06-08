# services.php

**Chemin :** `Api/V8/Config/services.php`
**Type :** PHP (configuration DI)
**Dernière mise à jour doc :** 2026-05-28

## Rôle

Point d'entrée principal du conteneur de dépendances de l'API V8. Ce fichier agrège l'ensemble des définitions de services, factories, middlewares, helpers, contrôleurs, validateurs et paramètres en un seul tableau retourné au framework Slim. Il surcharge également le `foundHandler` natif de Slim par une stratégie d'invocation personnalisée, et enregistre le service `BeanManager`.

## Responsabilités

- Surcharger le `foundHandler` de Slim avec `SuiteInvocationStrategy` (ligne 10-12).
- Enregistrer `BeanManager` dans le conteneur avec `DBManager` et la liste `beanAliases` comme dépendances (lignes 13-18).
- Fusionner (opérateur `+`) les tableaux de définitions issus des neuf sous-fichiers du dossier `services/` via `require` (lignes 20-28).
- Appliquer la surcharge customisation via `CustomLoader::mergeCustomArray` pour permettre l'extension sans modifier le core.

## Dépendances internes

| Symbole | Source | Rôle |
|---|---|---|
| `SuiteInvocationStrategy` | `Api\V8\Controller\InvocationStrategy` | Remplace le handler d'invocation par défaut de Slim |
| `BeanManager` | `Api\V8\BeanDecorator\BeanManager` | Gestionnaire central des beans SugarCRM |
| `DBManager` | Globale SugarCRM | Instance de la base de données |
| `CustomLoader` | `Api\Core\Loader\CustomLoader` | Fusionne les tableaux en autorisant la surcharge custom |
| `services/beanAliases.php` | local | Alias des modules CRM |
| `services/controllers.php` | local | Définitions des contrôleurs |
| `services/factories.php` | local | Définitions des factories |
| `services/globals.php` | local | Variables globales (config, DB) |
| `services/helpers.php` | local | Helpers JSON:API et VarDef |
| `services/middlewares.php` | local | Serveurs OAuth2 (AuthorizationServer, ResourceServer) |
| `services/params.php` | local | Objets Param pour chaque endpoint |
| `services/services.php` | local | Services métier |
| `services/validators.php` | local | Validateur Symfony |

## Exports / Points d'entrée

Ce fichier retourne un tableau PHP de closures indexées par FQCN (ou clé string). Il est consommé par le bootstrap de l'application Slim via le mécanisme de container DI.

- **Consommateurs identifiés :** INCONNU — le fichier est probablement chargé dans le bootstrap principal (`entryPoint.php` ou équivalent, non listé dans ce batch).

## Notes techniques

- L'opérateur `+` PHP préserve les clés du tableau de gauche en cas de doublon ; l'ordre de priorité est donc : `services.php` > `beanAliases` > `controllers` > … > `validators`.
- `CustomLoader::mergeCustomArray` permet à des personnalisations dans un dossier `custom/` d'écraser les définitions par défaut sans patch du core.
- La clé `foundHandler` est propre à Slim 3 ; elle est obsolète dans Slim 4.
