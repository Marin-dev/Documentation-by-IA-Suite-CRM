# soap.php

**Chemin :** `soap.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-28

---

## Rôle
Point d'entrée HTTP pour le service web SOAP legacy de SuiteCRM. Expose une API SOAP compatible avec les clients SugarCRM existants (namespace `http://www.sugarcrm.com/sugarcrm`), incluant les fonctions utilisateur, données CRM, et optionnellement le portail.

## Responsabilités
- Initialiser l'environnement SuiteCRM et bufferiser la sortie
- Créer un serveur SOAP (`soap_server` nusoap) configuré avec un WSDL dynamique
- Charger conditionnellement les fonctions du portail si `portal_on` est activé en administration
- Enregistrer les fonctions SOAP des modules : utilisateurs (`SoapSugarUsers`), données (`SoapData`), fonctions dépréciées (`SoapDeprecated`)
- Configurer le `ResourceManager` pour le contexte Soap
- Déléguer le traitement de la requête à `$server->service($HTTP_RAW_POST_DATA)`

## Dépendances internes
- `include/entryPoint.php` — bootstrap global
- `include/utils/file_utils.php` — utilitaires fichiers
- `soap/SoapError.php` — gestion des erreurs SOAP
- `include/nusoap/nusoap.php` — librairie nusoap (serveur SOAP PHP)
- `service/core/SoapHelperWebService.php` — helpers SOAP
- `soap/SoapSugarUsers.php`, `soap/SoapData.php`, `soap/SoapDeprecated.php` — définitions des méthodes SOAP
- `soap/SoapPortalUsers.php` — méthodes portail (chargement conditionnel)
- `modules/Contacts/Contact.php`, `modules/Accounts/Account.php`, `modules/Opportunities/Opportunity.php`, `modules/Cases/Case.php` — beans chargés pour le contexte SOAP
- `include/resource/ResourceManager.php` — gestionnaire de ressources/observateurs

## Exports / Points d'entrée
- **Point d'entrée HTTP :** `POST /soap.php`
- WSDL disponible : `GET /soap.php?wsdl`
- Namespace SOAP : `http://www.sugarcrm.com/sugarcrm`

## Notes techniques
- Utilise nusoap (librairie tierce PHP) et non l'extension SOAP native PHP — choix de compatibilité historique.
- API considérée comme legacy ; la nouvelle API REST V8 est recommandée pour les nouvelles intégrations.
- La lecture de `$HTTP_RAW_POST_DATA` via `file_get_contents('php://input')` est nécessaire car `$HTTP_RAW_POST_DATA` est déprécié depuis PHP 5.6.
