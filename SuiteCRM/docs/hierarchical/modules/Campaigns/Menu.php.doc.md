# Fichier : Menu.php

**Chemin :** `modules/Campaigns/Menu.php`
**Type :** PHP - Configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les entrees du menu de navigation du module Campaigns. Affiche conditionnellement les liens selon les droits ACL de l'utilisateur courant.

## Role technique

Script procedural qui peuple le tableau global `$module_menu`. Verifie `ACLController::checkAccess()` avant chaque entree. Liens vers : creation via wizard, liste des campagnes, creation/liste de templates email, ProspectLists.

---

## Dependances cles

- `ACLController::checkAccess()` — controle d'acces par action
- Globales : `$mod_strings`, `$app_strings`

## Exports / Symboles principaux

- `$module_menu` — tableau global — entrees du menu module

## Consommateurs identifies

- Framework SuiteCRM (charge automatiquement pour rendre la barre de navigation du module)

## Relations cles

- **Liens generes vers :** `Campaigns/WizardHome`, `Campaigns/index`, `EmailTemplates/EditView`, `EmailTemplates/index`, `ProspectLists/index`

---

## Points d'attention

- L'acces a la creation est controle par le droit `edit` sur `Campaigns`.
- Le lien vers la vue newsletter est commente dans le code source (l.66-70) — non affiche.
