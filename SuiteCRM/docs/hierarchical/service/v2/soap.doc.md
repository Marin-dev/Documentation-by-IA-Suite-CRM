# soap.php (v2)

**Chemin :** `service/v2/soap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée SOAP pour la version 2 de l'API SuiteCRM. Définit les paramètres du service SOAP v2 (NuSOAP) et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Dépendances clés
- `service/core/webservice.php` — bootstrap commun

---

## Exports/Symboles principaux
Variables définies :
- `$webservice_class = 'SugarSoapService2'`
- `$webservice_path = 'service/v2/SugarSoapService2.php'`
- `$registry_class = 'registry'`
- `$registry_path = 'service/v2/registry.php'`
- `$webservice_impl_class = 'SugarWebServiceImpl'`
- `$location = '/service/v2/soap.php'`

---

## Interactions
- **Appelé par :** clients SOAP externes via HTTP POST
- **Appelle :** `service/core/webservice.php`

---

## Notes
- Accessible via URL : `{site_url}/service/v2/soap.php`
- Utilise `SugarWebServiceImpl` (base) comme implémentation
