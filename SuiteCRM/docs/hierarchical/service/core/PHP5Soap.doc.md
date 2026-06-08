# PHP5Soap.php

**Chemin :** `service/core/PHP5Soap.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe abstraite qui implémente le protocole SOAP via l'extension PHP native `SoapServer` (SOAP 1.2). Elle maintient également un serveur NuSOAP interne pour la génération de WSDL (mise en cache dans `upload://`). Utilisée en alternative à `NusoapSoap` quand on souhaite exploiter le SoapServer PHP natif plutôt que la bibliothèque NuSOAP pour le traitement des requêtes.

**Type :** service

---

## Dépendances clés
- `service/core/SugarSoapService.php` — classe parente abstraite
- `include/nusoap/nusoap.php` — utilisé uniquement pour générer le WSDL
- `SoapServer` (PHP natif, SOAP 1.2, encoding ISO-8859-1)

---

## Exports/Symboles principaux
- `PHP5Soap` — classe abstraite (étend `SugarSoapService`)
  - `serve()` — sert la requête : WSDL via NuSOAP ou requête SOAP via `SoapServer` PHP natif
  - `getWSDLPath($generateWSDL)` — génère et met en cache le WSDL dans `upload://wsdlcache-{md5}`
  - `registerImplClass($implementationClass)` — instancie `SoapServer` et attache la classe d'implémentation
  - `registerFunction(...)` — enregistre une fonction dans le serveur NuSOAP (pour le WSDL)
  - `registerType(...)` — enregistre un type complexe dans NuSOAP
  - `setSoapVersion($version)` — définit la version SOAP (1.1 ou 1.2)
  - `error($errorObject)` — transmet une erreur via `$server->fault()`

---

## Interactions
- **Appelé par :** INCONNU (non référencé explicitement dans les fichiers lus — probablement une variante non activée par défaut)
- **Appelle :** `soap_server` (NuSOAP pour WSDL), `SoapServer` (PHP natif pour requêtes)

---

## Notes
- Désactive le cache WSDL PHP : `ini_set("soap.wsdl_cache_enabled", "0")` (ligne 49)
- Duplique la logique `QUERY_STRING` (lignes 71-76 — code mort identique dans les deux branches)
- Couplage fort NuSOAP pour WSDL + PHP SOAP pour l'exécution : architecture hybride complexe
- Le fichier commence par le bloc de copyright avant la balise `<?php` (anomalie de format)
