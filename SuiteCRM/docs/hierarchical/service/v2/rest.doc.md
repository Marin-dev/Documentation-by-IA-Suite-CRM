# rest.php (v2)

**Chemin :** `service/v2/rest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Point d'entrée REST pour la version 2 de l'API SuiteCRM. Définit les paramètres du service REST v2 et délègue à `service/core/webservice.php` pour l'initialisation et le traitement.

**Type :** entrypoint

---

## Dépendances clés
- `service/core/webservice.php` — bootstrap commun

---

## Exports/Symboles principaux
Variables définies avant l'inclusion :
- `$webservice_class = 'SugarRestService'`
- `$webservice_path = 'service/core/SugarRestService.php'`
- `$webservice_impl_class = 'SugarRestServiceImpl'`
- `$registry_class = 'registry'`
- `$location = '/service/v2/rest.php'`
- `$registry_path = 'service/v2/registry.php'`

---

## Interactions
- **Appelé par :** clients REST externes via HTTP GET/POST
- **Appelle :** `service/core/webservice.php`

---

## Notes
- Utilise `SugarRestServiceImpl` (implémentation base) — pas de surcharge versionnée pour REST v2
- Accessible via URL : `{site_url}/service/v2/rest.php`
