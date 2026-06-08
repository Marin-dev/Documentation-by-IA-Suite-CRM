# JsonRPCServerUtils.php

## Rôle
Classe utilitaire pour le serveur JSON-RPC : construction des clauses SQL WHERE à partir des conditions JSON et authentification de l'utilisateur courant via la session PHP.

## Responsabilités
- `constructWhere` : transformer un tableau de conditions JSON (opérateurs `contains`, `like_custom`, `starts_with`) en clause SQL WHERE compatible SugarCRM
- Gérer les conditions sur les champs e-mail via sous-requête sur `email_addr_bean_rel` / `email_addresses`
- Filtrer automatiquement les utilisateurs actifs (`status='Active'`) si la table `users` est interrogée
- `authenticate` : valider la session PHP via `unique_key` et `authenticated_user_id`, renvoyer l'objet `User` ou `null`

## Dépendances internes
- `BeanFactory` (global SuiteCRM) — instanciation de `Users`
- `DBManagerFactory` (global SuiteCRM) — quote et validation des noms de colonnes

## Exports / Points d'entrée
- `JsonRPCServerUtils` — classe
- `JsonRPCServerUtils::constructWhere(&$query_obj, $table, $module)` — retourne une chaîne SQL WHERE
- `JsonRPCServerUtils::authenticate()` — retourne `User|null`

## Notes techniques
- Les opérateurs supportés sont `contains` (LIKE %val%), `like_custom` (LIKE custom), et le défaut `starts_with` (LIKE val%)
- La validation de session compare `$_SESSION['unique_key']` à `$sugar_config['unique_key']` (ligne 121-122)
- Aucune injection SQL possible grâce à `DBManagerFactory::getInstance()->quote()` et `getValidDBName()`
