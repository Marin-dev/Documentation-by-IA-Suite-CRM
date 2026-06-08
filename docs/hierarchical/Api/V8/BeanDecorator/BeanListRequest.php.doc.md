# BeanListRequest.php

## Rôle
Objet de construction de requête (builder pattern) pour interroger une liste d'enregistrements SugarBean. Encapsule les paramètres d'une requête de liste (filtres, tri, pagination, champs) et déclenche l'exécution via `fetch()`.

## Responsabilités
- Stocker les paramètres d'une requête de liste : `orderBy`, `where`, `offset`, `limit`, `max`, `deleted`, `singleSelect`, `fields`
- Exposer des méthodes fluentes (chaînage) pour configurer chaque paramètre
- Déléguer l'exécution à `$bean->get_list()` et encapsuler le résultat dans un `BeanListResponse`
- Fournir des valeurs par défaut cohérentes via les constantes de `BeanManager`

## Dépendances internes
- `Api\V8\BeanDecorator\BeanManager` — constantes `DEFAULT_OFFSET` et `DEFAULT_ALL_RECORDS` utilisées comme valeurs par défaut (lignes 25, 35)
- `Api\V8\BeanDecorator\BeanListResponse` — type de retour de la méthode `fetch()` (ligne 161)
- `\SugarBean` — bean injecté en constructeur, dont la méthode `get_list()` est appelée

## Exports / Points d'entrée
- `class BeanListRequest` — builder fluent pour requête de liste SugarBean
- `fetch() : BeanListResponse` — déclenche la requête et retourne le résultat encapsulé

## Notes techniques
- Pattern Builder : toutes les méthodes de configuration retournent `$this` pour le chaînage.
- La valeur par défaut de `$limit` est `-1` (illimité) et `$max` est `BeanManager::DEFAULT_ALL_RECORDS` (-99), ce qui correspond au comportement natif de `SugarBean::get_list()`.
- Attribut `#[\AllowDynamicProperties]` : compatibilité PHP 8.2+.
- Consommateur principal : `BeanManager::getList()` qui instancie cette classe (ligne 115 de `BeanManager.php`).
