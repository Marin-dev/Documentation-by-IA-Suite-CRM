# SoapData.php

**Chemin :** `soap/SoapData.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural qui enregistre la méthode SOAP `sync_get_modified_relationships` sur le serveur NuSOAP global `$server`. Implémente la fonction permettant de récupérer les relations modifiées entre deux dates — utilisée pour la synchronisation avec des clients mobiles ou Outlook.

**Type :** service (procédural, inclus dans un contexte SOAP)

---

## Dépendances clés
- `soap/SoapRelationshipHelper.php` — helper pour les fonctions de relation
- Variable globale `$server` (instance NuSOAP)
- Variable globale `$NAMESPACE`

---

## Exports/Symboles principaux
- Fonction globale `sync_get_modified_relationships($session, $module_name, $related_module, $from_date, $to_date, $offset, $max_results, $deleted, $module_id, $select_fields, $ids, $relationship_name, $deletion_date, $php_serialize)` — retourne `tns:get_entry_list_result_encoded`

---

## Interactions
- **Inclus par :** INCONNU — probablement par `soap.php` (ancienne API SOAP v1) ou un registre SOAP v1
- **Appelle :** `SoapRelationshipHelper` (fonctions de relation)

---

## Notes
- `set_time_limit(360)` au début — indique des opérations potentiellement longues (ligne 45)
- Ce fichier appartient à l'ancienne API SOAP v1 (style procédural avec `$server->register()`), distincte des services versionnés v2-v4_1
- `$php_serialize` : paramètre permettant de retourner les données en format PHP sérialisé plutôt qu'encodé
