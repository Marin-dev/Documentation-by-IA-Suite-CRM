# JsonRPCServerUtils.php

**Chemin :** `service/JsonRPCServer/JsonRPCServerUtils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe utilitaire pour le serveur JSON-RPC. Fournit deux fonctions : l'authentification de l'utilisateur via la session PHP, et la construction de clauses SQL WHERE à partir des conditions de la requête JSON-RPC.

**Type :** helper

---

## Dépendances clés
- `DBManagerFactory` — pour `quote()` et `getValidDBName()`
- `BeanFactory::newBean('Users')` — chargement utilisateur
- Globals : `$sugar_config`, `$_SESSION`

---

## Exports/Symboles principaux
- `JsonRPCServerUtils` — classe utilitaire
  - `constructWhere(&$query_obj, $table, $module)` — construit une clause SQL WHERE depuis un tableau de conditions ; supporte `contains`, `like_custom`, `starts_with` ; gestion spéciale email1/email2 via sous-requête JOIN
  - `authenticate()` — valide la session via `unique_key` + `authenticated_user_id`, retourne l'objet `User` ou `null`

---

## Interactions
- **Appelé par :** `JsonRPCServer->processRequest()` (authenticate), `JsonRPCServerCalls->query()` (constructWhere)

---

## Notes
- `constructWhere()` force `status='Active'` pour la table `users` (ligne 98)
- Gestion SQL email via sous-requête sur `email_addr_bean_rel` et `email_addresses` (lignes 72-75)
- L'opérateur `like_custom` permet d'injecter des patterns LIKE personnalisés (début/fin) — attention aux injections SQL : les valeurs sont quotées mais la structure du LIKE dépend des paramètres `begin`/`end`
- L'authentification ne vérifie que `unique_key` et `authenticated_user_id` — pas de vérification IP contrairement à `SoapHelperWebServices`
