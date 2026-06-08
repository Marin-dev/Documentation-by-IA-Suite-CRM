# SugarWebServiceImpl.php

**Chemin :** `service/core/SugarWebServiceImpl.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe d'implémentation de base pour tous les web services SuiteCRM (SOAP et REST). Fournit les opérations CRUD sur les modules SugarBean via API : récupération d'enregistrements, listes, relations, création/modification, pièces jointes, login, etc. Elle délègue les vérifications de sécurité et la manipulation des beans à `$helperObject` (instance de `SoapHelperWebServices`).

**Type :** service / controller

---

## Dépendances clés
- `service/core/SoapHelperWebService.php` — helper injecté dans `$helperObject` (chargé à l'init du fichier, ligne 49)
- `SoapError` — classe d'erreur SOAP/REST
- `BeanFactory` — chargement des modules
- Globals : `$beanList`, `$beanFiles`, `$sugar_config`, `$current_user`

---

## Exports/Symboles principaux
- `SugarWebServiceImpl` — classe d'implémentation
  - `$helperObject` (static) — instance du helper (par défaut : `SoapHelperWebServices`)
  - `get_entry($session, $module_name, $id, $select_fields, $link_name_to_fields_array)` — récupère un bean par ID
  - `get_entries($session, $module_name, $ids, ...)` — récupère plusieurs beans par IDs
  - `get_entry_list($session, $module_name, $query, $order_by, $offset, ...)` — liste paginée de beans avec filtre SQL
  - Et de nombreuses autres méthodes API (set_entry, login, logout, get_relationships, set_relationship, get_module_fields, etc.) — INCONNU : liste complète non lue en totalité

---

## Interactions
- **Étendu par :** `SugarWebServiceImplv2_1`, `SugarWebServiceImplv3`, `SugarWebServiceImplv3_1`, `SugarWebServiceImplv4`, `SugarWebServiceImplv4_1`, `SugarRestServiceImpl`
- **Appelé par :** `SugarRestService`, `NusoapSoap`, `PHP5Soap` via la classe d'implémentation enregistrée
- **Appelle :** `SoapHelperWebServices` (via `self::$helperObject`), `BeanFactory`

---

## Notes
- `SugarWebServiceImpl::$helperObject = new SoapHelperWebServices()` est exécuté au chargement (ligne 49) — l'instance est remplacée par les sous-classes
- Le module `Reports` est interdit via `get_entries` (ligne 107-112) — protection explicite
- `CampaignProspects` est remappé vers `Prospects` (ligne 98-101)
- Les beans supprimés retournent un objet avec `deleted=1` et warning, plutôt qu'une erreur
