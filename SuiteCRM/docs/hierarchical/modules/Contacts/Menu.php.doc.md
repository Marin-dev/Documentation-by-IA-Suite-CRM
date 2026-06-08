# Fichier : Menu.php (Contacts)

**Chemin :** `modules/Contacts/Menu.php`
**Type :** PHP - Configuration (menu module)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les entrees du menu de navigation du module Contacts. Affiche conditionnellement les liens selon les droits ACL : creation, import vCard, liste, import CSV.

## Role technique

Script procedural peuplant `$module_menu`. Verifie `ACLController::checkAccess()` pour chaque entree.

---

## Dependances cles

- `ACLController::checkAccess()` — controle d'acces
- Globales : `$mod_strings`, `$app_strings`, `$sugar_config`

## Exports / Symboles principaux

- `$module_menu` — tableau global — entrees du menu

## Consommateurs identifies

- Framework SuiteCRM (barre de navigation du module Contacts)

## Relations cles

- **Liens generes vers :** `Contacts/EditView`, `Contacts/ImportVCard`, `Contacts/index`, `Import/Step1`

---

## Points d'attention

- Import vCard et import CSV distincts — deux droits ACL `import` requis.
