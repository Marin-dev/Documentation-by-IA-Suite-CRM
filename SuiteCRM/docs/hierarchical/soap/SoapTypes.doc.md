# SoapTypes.php

**Chemin :** `soap/SoapTypes.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural qui enregistre les types WSDL complexes pour l'API SOAP v1 via `$server->wsdl->addComplexType()`. Définit les structures de données partagées comme `note_attachment`, `new_note_attachment`, et d'autres types complexes.

**Type :** configuration WSDL (procédural)

---

## Dépendances clés
- Variable globale `$server` (instance NuSOAP avec accès WSDL)

---

## Exports/Symboles principaux
Types WSDL enregistrés (partiellement lus) :
- `note_attachment` — `id`, `filename`, `file`
- `new_note_attachment` — version enrichie
- Autres types : INCONNU

---

## Interactions
- **Inclus par :** `soap/SoapSugarUsers.php`, `soap/SoapPortalUsers.php`

---

## Notes
- Équivalent procédural des `registerType()` du registre OOP v2-v4
- Fait partie de l'ancienne architecture SOAP v1
