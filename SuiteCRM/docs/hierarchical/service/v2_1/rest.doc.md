# rest.php (v2_1)

**Chemin :** `service/v2_1/rest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée REST pour la version 2_1 de l'API SuiteCRM. Configure et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Exports/Symboles principaux
- `$webservice_class = 'SugarRestService'`
- `$webservice_impl_class = 'SugarWebServiceImplv2_1'`
- `$registry_path = 'service/v2_1/registry.php'`
- `$location = '/service/v2_1/rest.php'`

---

## Interactions
- **Appelé par :** clients REST via HTTP
- **Appelle :** `service/core/webservice.php`
