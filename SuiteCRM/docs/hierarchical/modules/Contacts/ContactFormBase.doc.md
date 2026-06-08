# ContactFormBase.php

**Chemin :** `modules/Contacts/ContactFormBase.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Classe de gestion des formulaires du module Contacts. Hérite de `PersonFormBase`. Fournit la requête SQL de détection des doublons et toute la logique de sauvegarde (validate, save, redirect) via le parent.

## Type

`helper` (form handler)

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `PersonFormBase` (extend) | Gestion formulaire personne de base |
| `include/SugarObjects/forms/PersonFormBase.php` | Inclusion explicite |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactFormBase` | classe | Handler formulaire contact |
| `getDuplicateQuery()` | méthode | Requête SQL de détection doublons (first_name + last_name) |

---

## Interactions

- **Appelé par :** `Save.php`, `WebToLeadCapture.php` (via `LeadFormBase` parent analogue)
- **Appelle :** `PersonFormBase::handleSave()` (hérité)

---

## Points d'attention

- La requête doublon (bug #46427) inclut la sécurité équipes.
- Le champ `account_name` est traité séparément car de type `relate`.
