# soap.php (v4_1)

**Chemin :** `service/v4_1/soap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée SOAP pour la version 4_1 de l'API SuiteCRM — **version recommandée**. Configure et délègue à `service/core/webservice.php`.

**Type :** entrypoint

---

## Exports/Symboles principaux
- `$webservice_impl_class = 'SugarWebServiceImplv4_1'`
- `$location = '/service/v4_1/soap.php'`

---

## Interactions
- **Appelé par :** clients SOAP via HTTP (URL recommandée pour intégrations Outlook, mobile)
- **Appelle :** `service/core/webservice.php`
