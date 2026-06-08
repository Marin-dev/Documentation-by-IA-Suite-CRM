# rest.php (v4_1)

**Chemin :** `service/v4_1/rest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée REST pour la version 4_1 de l'API SuiteCRM — **version recommandée**. Configure et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Exports/Symboles principaux
- `$webservice_impl_class = 'SugarWebServiceImplv4_1'`
- `$location = '/service/v4_1/rest.php'`

---

## Interactions
- **Appelé par :** clients REST via HTTP (URL recommandée pour intégrations)
- **Appelle :** `service/core/webservice.php`
