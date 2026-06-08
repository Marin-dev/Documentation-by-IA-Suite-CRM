# Fichier : ContactFeed.php

**Chemin :** `modules/Contacts/SugarFeeds/ContactFeed.php`
**Type :** PHP - Hook logique (SugarFeed)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Publie une entree dans le flux d'activite SugarFeed lors de la creation d'un nouveau contact. Affiche un message de type "Contact cree : [Nom Prenom]" dans le flux.

## Role technique

Etend `FeedLogicBase` (`modules/SugarFeed/feedLogicBase.php`). Implemente `pushFeed($bean, $event, $arguments)`. Publie uniquement lors de la creation (si `$bean->fetched_row` est vide).

---

## Dependances cles

- `modules/SugarFeed/feedLogicBase.php` — classe parente
- `$locale->getLocaleFormattedName()` — formatage du nom du contact

## Exports / Symboles principaux

- `ContactFeed` — classe
  - `pushFeed($bean, $event, $arguments)` — publie dans le flux lors de la creation (l.52)

## Consommateurs identifies

- Systeme de logic hooks SugarFeed (hook `after_save` sur le module Contacts)

## Relations cles

- **Position dans le flux :** Publication dans le flux d'activite apres creation d'un contact

---

## Points d'attention

- Ne publie que lors de la creation (`fetched_row` vide) — pas lors des mises a jour.
