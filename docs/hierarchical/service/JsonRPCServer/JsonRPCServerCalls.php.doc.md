# JsonRPCServerCalls.php

## Rôle
Contient les méthodes métier exposées via le serveur JSON-RPC : récupération d'un enregistrement (`retrieve`) et requête filtrée de liste (`query`). C'est la couche d'implémentation des appels RPC JSON de SuiteCRM.

## Responsabilités
- `retrieve` : récupérer un SugarBean unique par module et ID, le sérialiser via `json_config::populateBean`
- `query` : lister des SugarBeans selon des conditions, un tri et une limite, avec résolution des valeurs d'énumération vers leur libellé traduit

## Dépendances internes
- `soap/SoapHelperFunctions.php` — fonctions utilitaires partagées
- `include/json_config.php` — `json_config` (populateBean, listFilter)
- `include/utils.php` — `getJSONobj`, `get_current_language`, `return_app_list_strings_language`
- `service/JsonRPCServer/JsonRPCServerUtils.php` — `JsonRPCServerUtils::constructWhere`
- `BeanFactory` (global SuiteCRM) — instanciation des SugarBeans

## Exports / Points d'entrée
- `JsonRPCServerCalls` — classe
- `JsonRPCServerCalls::retrieve($request_id, $params)` — retourne `['id', 'result' => ['status', 'record']]`
- `JsonRPCServerCalls::query($request_id, $params)` — retourne `['id', 'result' => ['list']]`

## Notes techniques
- La méthode `query` surcharge temporairement `sugar_config['list_max_entries_per_page']` à 31 minimum (ligne 100-102)
- Le décodage des conditions utilise `mb_convert_encoding` ISO-8859-1 → UTF-8 avant de passer par `$db->quote` (ligne 111-113)
- Les valeurs d'énumérations sont résolues via `$app_list_strings` (chargement lazy, ligne 178-179)
