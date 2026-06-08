# ACLJSController.php

**Chemin :** `modules/ACL/ACLJSController.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Generateur de code JavaScript pour les regles ACL. Serialise les permissions du module courant en JS pour que le frontend puisse masquer/afficher les elements d'interface selon les droits de l'utilisateur.

## Type
helper / JS generator

## Dependances cles
- `ACLController::moduleSupportsACL()` — verifie si le module supporte ACL
- `$action` (global) — action courante

## Exports / Symboles principaux
- `class ACLJSController`
- `getJavascript()` — retourne le bloc JS serialisant les ACL du module

## Interactions
- **Appelle :** `ACLController::moduleSupportsACL()`
- **Appele par :** vues detail/edit SuiteCRM pour injection JS

## Notes
- Contenu complet du fichier non entierement lu.
