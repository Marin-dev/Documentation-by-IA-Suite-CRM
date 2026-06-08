# webservice.php

**Chemin :** `service/core/webservice.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Script bootstrap commun à tous les points d'entrée de services web (SOAP et REST, toutes versions). Il initialise le service, enregistre le registre et la classe d'implémentation, puis appelle `serve()` pour traiter la requête. Il est inclus par tous les fichiers `rest.php` et `soap.php` des versions v2 à v4_1.

**Type :** entrypoint (bootstrap partagé)

---

## Dépendances clés
- `include/entryPoint.php` — bootstrap SuiteCRM global
- `soap/SoapError.php` — classe d'erreur
- Variables attendues dans le scope appelant :
  - `$webservice_class` — nom de la classe de service (ex. `SugarRestService`)
  - `$webservice_path` — chemin vers le fichier de la classe de service
  - `$registry_class` — nom de la classe de registre
  - `$registry_path` — chemin vers le fichier de registre
  - `$webservice_impl_class` — nom de la classe d'implémentation
  - `$webservice_impl_class_path` — chemin vers la classe d'implémentation (optionnel)
  - `$location` — chemin URL du service (ex. `/service/v2/rest.php`)

---

## Exports/Symboles principaux
- Aucune classe/fonction exportée — script procédural
- Crée et expose `$service_object` dans le scope global (pour la gestion d'erreur)

---

## Interactions
- **Inclus par :** `service/v2/rest.php`, `service/v2/soap.php`, `service/v2_1/rest.php`, ... `service/v4_1/soap.php`
- **Appelle :** `$service->registerClass()`, `$service->register()`, `$service->registerImplClass()`, `$service->serve()`

---

## Notes
- Utilise `chdir(__DIR__.'/../../')` pour rétablir la racine du projet (ligne 50)
- Le `$service_object` global est nécessaire pour que `SoapHelperWebServices->setFaultObject()` puisse accéder au service depuis n'importe où (ligne 168 de SoapHelperWebService.php)
- `ob_start()` au début (ligne 49) — la sortie est bufferisée pour éviter les sorties prématurées
