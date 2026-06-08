# SoapRelationshipHelper.php

**Chemin :** `soap/SoapRelationshipHelper.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Fichier procédural fournissant des fonctions utilitaires pour la gestion des relations entre modules via SOAP. Expose notamment `check_for_relationship()` qui vérifie l'existence d'une relation entre deux modules dans les métadonnées de relations.

**Type :** helper (procédural)

---

## Dépendances clés
- `soap/SoapError.php` — classe d'erreur

---

## Exports/Symboles principaux
- `check_for_relationship($relationships, $module)` — cherche dans le tableau de relations si `$module` est en `rhs_key`
- Autres fonctions : INCONNU (fichier lu partiellement)

---

## Interactions
- **Inclus par :** `soap/SoapData.php`
- **Potentiellement :** autres fichiers SOAP v1

---

## Notes
- Fait partie de l'architecture SOAP v1 procédurale
