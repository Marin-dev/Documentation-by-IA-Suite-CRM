# SugarSoapService2.php

**Chemin :** `service/v2/SugarSoapService2.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Classe de service SOAP concrète pour la version 2. Étend `NusoapSoap` et implémente la méthode `register()` pour invoquer le registre de fonctions/types. C'est la classe de service SOAP v2.

**Type :** service

---

## Dépendances clés
- `service/core/NusoapSoap.php` — classe parente

---

## Exports/Symboles principaux
- `SugarSoapService2` — (étend `NusoapSoap`)
  - `register($excludeFunctions)` — crée l'instance du registre et appelle `register()` ; gère `$excludeFunctions`

---

## Interactions
- **Appelé par :** `service/v2/soap.php` (via `service/core/webservice.php`)
- **Appelle :** `registry->register()`

---

## Notes
- Même pattern que les services SOAP v3, v4 — seul le registre et l'implémentation changent entre versions
