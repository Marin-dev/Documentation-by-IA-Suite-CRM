# Person.php

**Chemin :** `include/SugarObjects/templates/person/Person.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Template de bean SuiteCRM pour les objets representant des personnes physiques (Contact, Lead, etc.). Etend `Basic` avec les champs specifiques aux personnes : nom, prenom, civilite, emails, telephones, et champs RGPD (`lawful_basis`, `date_reviewed`).

## Role technique

Etend `Basic`. Declare les proprietes publiques typiques d'une personne. Le corps complet des methodes n'a pas ete lu dans ce contexte.

---

## Dependances cles

- **Imports principaux :**
  - `Basic` (`include/SugarObjects/templates/basic/Basic.php`) — classe parente

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Person` | classe | Template bean personne |
| `$first_name`, `$last_name`, `$full_name`, `$salutation` | proprietes | Identite |
| `$email1`, `$phone_work`, `$phone_fax`, `$phone_other` | proprietes | Coordonnees |
| `$lawful_basis`, `$date_reviewed`, `$lawful_basis_source` | proprietes | Conformite RGPD |
| `$photo` | propriete | Photo de profil |

- **Consommateurs identifies :** modules `Contacts`, `Leads` (qui etendent `Person`)

## Relations cles

- **Appele par :** beans Contacts, Leads et autres personnes physiques
- **Appelle :** `Basic::__construct()` (via heritage)
- **Position dans le flux global :** template intermediaire dans la hierarchie SugarObject pour les personnes

---

## Points d'attention

- Contient des champs RGPD (`lawful_basis`, `lawful_basis_source`) — important pour la conformite reglementaire.
- Les methodes de la classe n'ont pas ete lues entierement — comportement complet INCONNU.
