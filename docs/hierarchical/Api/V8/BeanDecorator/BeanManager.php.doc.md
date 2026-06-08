# BeanManager.php

## Rôle
Service central de gestion des beans SuiteCRM pour l'API V8. Fournit une interface unifiée et sécurisée pour créer, récupérer, lister et gérer les relations entre les enregistrements SugarBean, en gérant les alias de modules et en levant des exceptions typées en cas d'erreur.

## Responsabilités
- Résoudre les alias de modules (ex : `Account::class` → `'Accounts'`) avant d'appeler `BeanFactory`
- Instancier un bean vide via `newBeanSafe()` avec validation
- Récupérer un bean par ID via `getBeanSafe()` avec validation complète (ID vide, module inconnu, enregistrement introuvable)
- Construire et retourner un `BeanListRequest` via `getList()`
- Créer et supprimer des relations entre beans via `createRelationshipSafe()` et `deleteRelationshipSafe()`
- Résoudre le nom du champ de liaison entre deux beans via `getLinkedFieldName()`
- Compter les enregistrements d'un module avec support des tables custom (`_cstm`)
- Filtrer les champs acceptables pour les beans de type `Person` via `filterAcceptanceFields()`

## Dépendances internes
- `Api\V8\BeanDecorator\BeanListRequest` — instancié dans `getList()` (ligne 115)
- `\SugarBean` — type de base de tous les beans manipulés
- `\Person` — utilisé dans `filterAcceptanceFields()` pour filtrage spécifique (ligne 292)
- `\BeanFactory` — appels `newBean()`, `getBean()`, `getObjectName()` (lignes 46, 65, 88)
- `\DBManager` — exécution des requêtes SQL dans `countRecords()` (ligne 262)
- `\Relationship` — `retrieve_by_modules()` dans `getLinkedFieldName()` (ligne 186)

## Exports / Points d'entrée
- `class BeanManager` — service injectable via le conteneur DI
- `const DEFAULT_OFFSET = 0`
- `const DEFAULT_LIMIT = -1`
- `const DEFAULT_ALL_RECORDS = -99`
- `newBeanSafe(string $module) : \SugarBean` — instanciation validée
- `getBean(string $module, ?string $id, array $params, bool $deleted) : \SugarBean|bool`
- `getBeanSafe(string $module, string $id, array $params, bool $deleted) : \SugarBean`
- `getList(string $module) : BeanListRequest`
- `createRelationshipSafe(\SugarBean, \SugarBean, string) : void`
- `deleteRelationshipSafe(\SugarBean, \SugarBean, string) : void`
- `getLinkedFieldName(\SugarBean, \SugarBean) : string`
- `getLinkedFieldBean(\SugarBean, string) : \SugarBean`
- `countRecords(string $module, string $where) : int`
- `getDefaultFields(\SugarBean) : array`
- `filterAcceptanceFields(\SugarBean, array) : array`

## Notes techniques
- Le tableau `$beanAliases` est injecté depuis `services/beanAliases.php` et permet de mapper les noms de classes PHP vers les noms de modules SugarCRM.
- `countRecords()` effectue un JOIN LEFT sur la table custom (`_cstm`) si elle existe, pour inclure les champs personnalisés dans le comptage.
- `filterAcceptanceFields()` exclut les champs de type `relationship_info` pour les beans `Person` uniquement — comportement spécifique potentiellement fragile.
- Attribut `#[\AllowDynamicProperties]` : compatibilité PHP 8.2+.
- Consommateurs identifiés : `services/beanAliases.php`, `services/helpers.php`, `services/middlewares.php`, `services/params.php`, `services/services.php`.
