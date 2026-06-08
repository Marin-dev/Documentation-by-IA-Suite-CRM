# SoapDeprecated.php

**Chemin :** `soap/SoapDeprecated.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural contenant des types WSDL et fonctions SOAP dépréciés, maintenus uniquement pour la compatibilité ascendante avec d'anciens clients. Le commentaire en tête indique explicitement : "the types/methods defined in this file are deprecated -- please see SoapSugarUsers.php, SoapPortalUsers.php, SoapStudio.php, etc."

**Type :** service (déprécié)

---

## Dépendances clés
- Variable globale `$server` (instance NuSOAP avec accès à `$server->wsdl`)

---

## Exports/Symboles principaux
- Types WSDL dépréciés enregistrés via `$server->wsdl->addComplexType()` :
  - `contact_detail` — type avec champs `email_address`, `name1`, `name2`, `association`, `id`, `msi_id`
  - Autres types : INCONNU (fichier non lu en entier)

---

## Interactions
- **Inclus par :** INCONNU — probablement `soap.php` (API SOAP v1)

---

## Notes
- A ne pas modifier / ne pas étendre — contenu obsolète
- Les remplaçants sont : `SoapSugarUsers.php`, `SoapPortalUsers.php`, `SoapStudio.php`
