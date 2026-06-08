# rest.php (v4)

**Chemin :** `service/v4/rest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée REST pour la version 4 de l'API. Configure et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Exports/Symboles principaux
- `$webservice_impl_class = 'SugarWebServiceImplv4'`
- `$location = '/service/v4/rest.php'`

---

## Interactions
- **Appelé par :** clients REST via HTTP
- **Appelle :** `service/core/webservice.php`
