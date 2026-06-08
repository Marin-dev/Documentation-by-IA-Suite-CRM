# NusoapSoap.php

**Chemin :** `service/core/NusoapSoap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe abstraite qui implémente le protocole SOAP via la bibliothèque NuSOAP. Elle sert de couche d'adaptation entre le framework de services SugarCRM et le serveur NuSOAP, en prenant en charge la gestion du WSDL, la réception des requêtes HTTP brutes et l'envoi des réponses SOAP.

**Type :** service

---

## Dépendances clés
- `service/core/SugarSoapService.php` — classe parente abstraite SOAP
- `include/nusoap/nusoap.php` — bibliothèque NuSOAP (classe `soap_server`)

---

## Exports/Symboles principaux
- `NusoapSoap` — classe abstraite (étend `SugarSoapService`)
  - `__construct($url)` — initialise le serveur NuSOAP et configure le WSDL
  - `serve()` — traite la requête POST entrante via `$GLOBALS['HTTP_RAW_POST_DATA']`
  - `registerType(...)` — enregistre un type complexe WSDL via `$server->wsdl->addComplexType()`
  - `registerFunction(...)` — enregistre une fonction exposée en SOAP ; supporte les paramètres `use=literal` et `style=document`
  - `registerImplClass($implementationClass)` — lie la classe d'implémentation au serveur NuSOAP
  - `registerClass($registryClass)` — mémorise la classe de registre
  - `error($errorObject)` — transmet une erreur `SoapError` au serveur NuSOAP
  - `shutdown()` — fonction de fallback en cas d'erreur fatale pendant la requête SOAP

---

## Interactions
- **Appelé par :** `SugarSoapService2` (service/v2), `service/v*/soap.php` (points d'entrée versionnés)
- **Appelle :** `soap_server` (NuSOAP), `SugarSoapService` (parent)

---

## Notes
- Lit `$GLOBALS['HTTP_RAW_POST_DATA']` si non défini : `file_get_contents('php://input')` (ligne 65)
- Utilise `ob_start()` / `ob_end_flush()` pour bufferiser la sortie NuSOAP
- Le mécanisme `shutdown()` + `register_shutdown_function()` garantit une réponse SOAP même en cas d'erreur fatale PHP
- Namespace SOAP par défaut : `http://www.sugarcrm.com/sugarcrm` (défini dans `SugarSoapService`)
