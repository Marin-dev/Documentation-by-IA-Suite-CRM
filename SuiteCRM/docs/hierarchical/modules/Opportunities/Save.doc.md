# Fichier : Save.php

**Chemin :** `modules/Opportunities/Save.php`
**Type :** `PHP`
**Categorie :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree pour l'action `Save` du module Opportunities. Delegue la sauvegarde a `OpportunityFormBase::handleSave()`.

## Role technique

Script procedural minimal. Instancie `OpportunityFormBase` et appelle `handleSave('', true, false)`.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `OpportunityFormBase` | `modules/Opportunities/OpportunityFormBase.php` | Gestion complete de la sauvegarde |

## Points d'attention

- Equivalent de `modules/Accounts/Save.php` et `modules/Leads/Save.php`. Toute la logique dans `OpportunityFormBase::handleSave()`.
