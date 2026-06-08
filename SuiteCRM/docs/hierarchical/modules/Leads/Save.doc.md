# Fichier : Save.php

**Chemin :** `modules/Leads/Save.php`
**Type :** `PHP`
**Categorie :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree pour l'action `Save` du module Leads. Delegue entierement la sauvegarde a `LeadFormBase::handleSave()`.

## Role technique

Script procedural minimaliste : instancie `LeadFormBase` et appelle `handleSave('', true, false)` sans prefixe, avec redirection activee.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `LeadFormBase` | `modules/Leads/LeadFormBase.php` | Gestion complete de la sauvegarde |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing action=Save, module=Leads)
- **Appelle :** `LeadFormBase::handleSave()`

---

## Points d'attention

- Prefixe vide (`''`) : pas de gestion de doublon avec prefixe comme dans `modules/Accounts/Save.php`.
- Toute la logique est dans `LeadFormBase::handleSave()` (heritee de `PersonFormBase`).
