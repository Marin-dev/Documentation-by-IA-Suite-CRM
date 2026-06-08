# SoapPortalHelper.php

**Chemin :** `soap/SoapPortalHelper.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural définissant les modules accessibles au portail (`$portal_modules`) et des fonctions d'aide spécifiques au portail, notamment `get_bugs_in_contacts()`. Utilisé par `SoapPortalUsers.php`.

**Type :** helper (procédural)

---

## Dépendances clés
- Modules portail : `Contacts`, `Accounts`, `Notes`, `Cases`, `Bugs`

---

## Exports/Symboles principaux
- `$portal_modules` — tableau des modules accessibles via le portail
- `get_bugs_in_contacts($in, $orderBy)` — requête bugs liés à des contacts (INCONNU : logique complète non lue)
- Autres fonctions : INCONNU (fichier lu partiellement)

---

## Interactions
- **Inclus par :** `soap/SoapPortalUsers.php`

---

## Notes
- Fait partie de l'ancienne API SOAP v1 (portail client)
