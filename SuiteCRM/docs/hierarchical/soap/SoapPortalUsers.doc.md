# SoapPortalUsers.php

**Chemin :** `soap/SoapPortalUsers.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural qui enregistre les fonctions SOAP dédiées aux utilisateurs du portail client (accès externe limité). Expose des opérations comme la connexion, la récupération de contacts et bugs, la création de cas, etc. pour les utilisateurs portail.

**Type :** service (procédural, API SOAP v1)

---

## Dépendances clés
- `soap/SoapHelperFunctions.php` — helpers généraux
- `soap/SoapTypes.php` — types WSDL
- `soap/SoapPortalHelper.php` — helpers spécifiques portail
- Variable globale `$server` (NuSOAP)

---

## Exports/Symboles principaux
- Fonctions SOAP pour portail enregistrées sur `$server` : INCONNU (fichier lu partiellement)
- Section commentaire : `THIS IS FOR PORTAL USERS`

---

## Interactions
- **Inclus par :** INCONNU — probablement `soap.php` (ancienne API v1 portail)
- **Appelle :** `SoapPortalHelper`, `SoapHelperFunctions`, `SoapTypes`

---

## Notes
- Partie de l'ancienne architecture SOAP v1 — obsolète par rapport aux versions versionnées v2-v4_1
