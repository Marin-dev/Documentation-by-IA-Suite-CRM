# SoapHelperWebService.php

**Chemin :** `service/core/SoapHelperWebService.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe utilitaire centrale partagée par toutes les implémentations de services web SOAP/REST. Fournit les opérations transversales : validation de session, contrôle d'accès ACL, conversion bean<->name_value_list, gestion des relations, création/mise à jour de beans, et décryptage de mot de passe. C'est le "helper" injecté dans `SugarWebServiceImpl` via `$helperObject`.

**Type :** service / helper

---

## Dépendances clés
- `BeanFactory` (data/BeanFactory.php) — création et chargement des beans
- `AuthenticationController` — validation des credentials de login
- `LogicHook` — hooks `login_failed`
- `SugarSQLValidate` (include/SugarSQLValidate.php) — validation des clauses SQL
- `ACLController`, `ACLAction` — contrôle d'accès
- Globals : `$current_user`, `$sugar_config`, `$beanList`, `$beanFiles`

---

## Exports/Symboles principaux
- `SoapHelperWebServices` — classe helper
  - `validate_user($user_name, $password)` — authentifie par MD5 ou openssl_decrypt (TripleDES)
  - `validate_authenticated($session_id)` — valide la session PHP courante
  - `is_valid_ip_address($session_var)` — vérifie l'IP contre `$_SESSION` (classe C)
  - `checkSessionAndModuleAccess(...)` — combine validation session + accès module
  - `checkACLAccess($bean, $viewType, ...)` — vérifie les ACL sur un bean
  - `checkQuery($errorObject, $query, $order_by)` — valide les clauses SQL
  - `get_field_list($value, $fields, $translate)` — retourne la liste des champs d'un bean
  - `get_name_value_list($value)` / `get_name_value_list_for_fields($value, $fields)` — convertit un bean en tableau name/value
  - `new_handle_set_entries($module_name, $name_value_lists, $select_fields)` — crée/met à jour des beans en masse
  - `new_handle_set_relationship(...)` — crée/supprime des relations entre beans
  - `get_return_value_for_fields(...)`, `get_return_value_for_link_fields(...)` — formate la réponse API
  - `getRelationshipResults($bean, $link_field_name, $link_module_fields)` — charge les beans liés
  - `login_success($name_value_list)` — initialise la langue courante après login
  - `add_create_account($seed)` — crée ou lie un compte pour un Contact (logic spécifique)
  - `check_for_duplicate_contacts($seed)` — détection doublon Contact par email
  - `decrypt_string($string)` — déchiffrement TripleDES via `ldap_enc_key`

---

## Interactions
- **Appelé par :** `SugarWebServiceImpl` (via `self::$helperObject`), `SugarRestUtils`, `SugarWebServiceUtilv3/v3_1/v4/v4_1`
- **Appelle :** `BeanFactory`, `AuthenticationController`, `LogicHook`, `ACLController`, `DBManagerFactory`

---

## Notes
- `$disable_date_format = true` est défini au niveau fichier (ligne 47)
- La validation IP compare les 3 premiers octets (classe C) — non configurable via le code
- `verify_client_ip` dans `$sugar_config` permet de désactiver la validation IP (ligne 279)
- Le module `Users` bénéficie de protections spéciales : impossibilité de modifier `user_hash` d'un autre utilisateur (lignes 888-889)
- Gestion spécifique Meetings/Calls : recherche par `outlook_id` pour éviter les doublons (lignes 931-946)
- Clé TripleDES : `substr(md5($ldap_enc_key), 0, 24)`, IV fixe `"password"` — dette de sécurité notable (ligne 1244)
