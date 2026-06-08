# SoapHelperFunctions.php

**Chemin :** `soap/SoapHelperFunctions.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier de fonctions globales (procédurales) pour l'API SOAP v1. Fournit des utilitaires de manipulation de beans, notamment `get_field_list()` (version fonction globale de la méthode de classe du même nom dans `SoapHelperWebServices`). Utilisé par `JsonRPCServer` et les anciens fichiers SOAP.

**Type :** helper (procédural)

---

## Dépendances clés
- `BeanFactory` — chargement de beans
- Globals : `$app_list_strings`

---

## Exports/Symboles principaux
- `get_field_list($value, $translate)` — retourne la liste des champs d'un bean avec métadonnées (type, label, required, options)
- Autres fonctions : `get_name_value()`, et autres helpers (INCONNU : fichier lu partiellement)

---

## Interactions
- **Importé par :** `service/JsonRPCServer/JsonRPCServer.php`, `service/JsonRPCServer/JsonRPCServerCalls.php`, `soap/SoapPortalUsers.php`, `soap/SoapSugarUsers.php`

---

## Notes
- Doublon fonctionnel avec `SoapHelperWebServices::get_field_list()` (méthode de classe) — coexistence d'API procédurale (ancienne) et OOP (nouvelle)
