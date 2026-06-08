# Fichier : Menu.php

**Chemin :** `modules/Emails/Menu.php`
**Type :** PHP — Configuration menu module
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les entrees du menu du module Emails visibles dans la barre de navigation SuiteCRM. Deux entrees conditionnelles aux droits ACL : "Composer un email" et "Ma boite de reception".

## Role technique

Script de configuration (non-classe). Remplit le tableau global `$module_menu` selon les droits ACL de l'utilisateur courant.

---

## Dependances

- **Globales :** `$mod_strings`, `$current_user`
- **Utilise :** `ACLController::checkAccess()`, `BeanFactory::newBean('Emails')`

## Exports / Symboles principaux

- `$module_menu` (global) — entrees de menu
  - `ComposeView` (si droit `edit`) — composer un email
  - `index` / `ListView` (si droit `list`) — boite de reception

## Relations cles

- **Appele par :** framework SuiteCRM (auto-inclusion du menu module)

---

## Points d'attention

- RAS
