# SoapSugarUsers.php

**Chemin :** `soap/SoapSugarUsers.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural qui enregistre les fonctions SOAP dédiées aux utilisateurs SugarCRM/SuiteCRM internes (par opposition aux utilisateurs portail). Expose notamment `is_user_admin()` et d'autres opérations d'authentification et de gestion utilisateur.

**Type :** service (procédural, API SOAP v1)

---

## Dépendances clés
- `soap/SoapHelperFunctions.php` — helpers généraux
- `soap/SoapTypes.php` — types WSDL
- Variable globale `$server` (NuSOAP)
- `$disable_date_format = true` défini globalement

---

## Exports/Symboles principaux
- `is_user_admin($session)` — retourne `xsd:int` (1 si admin, 0 sinon)
- Autres fonctions utilisateur : INCONNU (fichier lu partiellement)

---

## Interactions
- **Inclus par :** INCONNU — probablement `soap.php` (ancienne API v1)
- **Appelle :** `SoapHelperFunctions`, `SoapTypes`

---

## Notes
- Partie de l'ancienne architecture SOAP v1
- `$NAMESPACE` est attendu dans le scope global pour `$server->register()`
