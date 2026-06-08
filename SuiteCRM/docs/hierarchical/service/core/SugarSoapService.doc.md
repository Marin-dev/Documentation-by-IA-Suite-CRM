# SugarSoapService.php

**Chemin :** `service/core/SugarSoapService.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe abstraite intermédiaire pour les services SOAP. Étend `SugarWebService` et ajoute les propriétés et méthodes propres à SOAP : namespace, URL, version SOAP, gestion des observers. Sert de base commune à `NusoapSoap` et `PHP5Soap`.

**Type :** service

---

## Dépendances clés
- `service/core/SugarWebService.php` — classe parente abstraite
- `service/core/SugarWebServiceImpl.php` — implémentation par défaut (chargée ici)

---

## Exports/Symboles principaux
- `SugarSoapService` — classe abstraite (étend `SugarWebService`)
  - Propriétés : `$soap_version` (1.1), `$namespace` (`http://www.sugarcrm.com/sugarcrm`), `$implementationClass`, `$registryClass`, `$soapURL`
  - Méthodes abstraites : `registerFunction()`, `registerType()`
  - `setObservers()` — appelle `set_soap_server()` sur tous les observers globaux (`$GLOBALS['observers']`)
  - `getSoapURL()`, `getSoapVersion()`, `getNameSpace()` — accesseurs
  - `getRegisteredImplClass()`, `getRegisteredClass()`, `getServer()` — accesseurs

---

## Interactions
- **Étendu par :** `NusoapSoap`, `PHP5Soap`
- **Appelle :** `SugarWebServiceImpl` (chargé à l'initialisation du fichier, ligne 45)

---

## Notes
- L'assignation `SugarWebServiceImpl::$helperObject = new SoapHelperWebServices()` est dans `SugarWebServiceImpl.php` qui est chargé ici
- Le mécanisme `$observers` avec `set_soap_server()` permet d'injecter le serveur SOAP dans des modules tiers
