# Fichier : WebToPersonCapture.php

**Chemin :** `modules/Campaigns/WebToPersonCapture.php`
**Type :** PHP - Script d'action (capture web generique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Version generalisee de `WebToLeadCapture.php` pour capturer des soumissions de formulaires web vers n'importe quel module "Person" (Contact, Lead, Prospect selon configuration). Traite la soumission, cree l'enregistrement dans le module cible et l'associe a la campagne.

## Role technique

Script procedural. Utilise `SuiteValidator` pour valider les IDs. Determine le module cible via `getValidWebToPersonModules()` depuis `utils.php`. Delague la creation de l'enregistrement au handler du module correspondant. Requiert `modules/Campaigns/utils.php`.

---

## Dependances cles

- `SuiteCRM\Utility\SuiteValidator`
- `include/formbase.php`
- `modules/Campaigns/utils.php` — `getValidWebToPersonModules()`, `isValidWebToPersonModule()`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Formulaires Web-to-Person generes pour les modules Contact, Prospect, etc.

## Relations cles

- **Appelle :** `getValidWebToPersonModules()`, creation d'enregistrement selon module
- **Position dans le flux :** Alternative generique a `WebToLeadCapture.php` pour modules Person

---

## Points d'attention

- Ne fonctionne qu'avec les modules retournes par `getValidWebToPersonModules()` (classes etendant `Person`).
