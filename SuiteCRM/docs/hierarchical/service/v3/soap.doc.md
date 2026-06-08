# soap.php (v3)

**Chemin :** `service/v3/soap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée SOAP pour la version 3 de l'API. Configure et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Exports/Symboles principaux
- `$webservice_impl_class = 'SugarWebServiceImplv3'`
- `$location = '/service/v3/soap.php'`

---

## Interactions
- **Appelé par :** clients SOAP via HTTP
- **Appelle :** `service/core/webservice.php`
