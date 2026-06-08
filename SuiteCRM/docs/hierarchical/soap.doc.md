# soap.php

**Chemin :** `soap.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Point d'entrée HTTP pour le service web SOAP de SuiteCRM. Expose une API SOAP basée sur le namespace `http://www.sugarcrm.com/sugarcrm` pour l'intégration d'applications tierces avec le CRM.

**Type :** entrypoint

## Rôle technique

Charge l'environnement SuiteCRM et la bibliothèque NuSOAP, configure le serveur SOAP avec WSDL auto-généré, charge les modules de services SOAP (utilisateurs, données, portail, dépréciés), puis traite les requêtes HTTP entrantes via `$server->service($HTTP_RAW_POST_DATA)`.

---

## Dépendances clés

- **Imports principaux :**
  - `include/entryPoint.php` — initialisation SuiteCRM
  - `include/utils/file_utils.php` — utilitaires de fichiers
  - `soap/SoapError.php` — gestion des erreurs SOAP
  - `include/nusoap/nusoap.php` — bibliothèque NuSOAP (serveur SOAP)
  - `modules/Contacts/Contact.php` — bean Contact
  - `modules/Accounts/Account.php` — bean Account
  - `modules/Opportunities/Opportunity.php` — bean Opportunity
  - `service/core/SoapHelperWebService.php` — helpers SOAP
  - `modules/Cases/Case.php` — bean Case
  - `soap/SoapSugarUsers.php` — API utilisateurs SugarCRM
  - `soap/SoapData.php` — API données générique
  - `soap/SoapDeprecated.php` — méthodes SOAP dépréciées
  - `soap/SoapPortalUsers.php` — API portail (si `portal_on` activé)
  - `include/resource/ResourceManager.php` — gestion des observateurs de ressources
- **Variables de configuration :**
  - `$sugar_config['site_url']` — URL de base pour le WSDL
  - `$administrator->settings['portal_on']` — active le module portail SOAP

## Sorties / Comportement

- Expose un WSDL via `?wsdl` et répond aux requêtes SOAP
- Namespace SOAP : `http://www.sugarcrm.com/sugarcrm`
- Service WSDL nommé `sugarsoap`
- Flush et cleanup après traitement

## Relations clés

- **Appelé par :** clients SOAP tiers (intégrations legacy), Zend OAuth
- **Appelle :** `ResourceManager::getInstance()->setup('Soap')` pour les observers

---

## Points d'attention

- `$HTTP_RAW_POST_DATA` est déprécié en PHP 7+ — utilise `file_get_contents('php://input')` en fallback (ligne 85).
- NuSOAP (`include/nusoap/`) est une bibliothèque legacy non maintenue — alternative : l'API V8 REST (`Api/V8/`).
- Le portail SOAP n'est chargé que si `portal_on` est activé dans les paramètres admin (ligne 70).
- `$soap_server_object` est exposé en global (ligne 101) pour les observers.
- L'API SOAP est considérée legacy — l'API V8 REST OAuth2 est recommandée pour les nouvelles intégrations.
