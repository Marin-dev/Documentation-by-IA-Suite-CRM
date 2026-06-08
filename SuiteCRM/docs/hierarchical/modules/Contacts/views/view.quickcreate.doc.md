# view.quickcreate.php

**Chemin :** `modules/Contacts/views/view.quickcreate.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Vue de création rapide (Quick Create) pour le module Contacts. Surcharge `ViewQuickcreate` pour pré-remplir les champs d'adresse et de téléphone depuis un compte parent lorsque le formulaire est ouvert via le menu DC (Dashlet/Create).

**Type :** view

---

## Dépendances clés

- `ViewQuickcreate` (classe parente, framework SuiteCRM MVC)
- `$this->bean` — bean Contact en cours d'édition
- `$this->_isDCForm` — indicateur de formulaire via menu DC

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewQuickcreate` | classe | Surcharge la vue quick create pour pré-remplir depuis le compte parent |
| `preDisplay()` | méthode | Copie les champs billing_address → primary_address et phone_office → phone_work si formulaire DC |

---

## Interactions

**Appelle :**
- `parent::preDisplay()` — traitement standard

**Appelée par :** Routing MVC SuiteCRM — action `QuickCreate` du module Contacts.

**Position dans le flux global :** Formulaire inline de création rapide de contact depuis les dashlets ou sous-panneaux.

---

## Notes

- Le commentaire TODO (ligne 53) signale un hack pour la pré-population lors de l'utilisation via menu DC — les champs `sqs_objects` ne se remplissent pas correctement.
- Les champs copiés : `phone_office` → `phone_work`, `billing_address_*` → `primary_address_*`.
