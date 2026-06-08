# ContactFeed.php

**Chemin :** `modules/Contacts/SugarFeeds/ContactFeed.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Logic hook de flux d'activité (SugarFeed) pour le module Contacts. Publie une entrée dans le fil d'activité SugarFeed lorsqu'un nouveau contact est créé (pas lors des mises à jour).

**Type :** helper / logic hook

---

## Dépendances clés

- `modules/SugarFeed/feedLogicBase.php` — classe parente `FeedLogicBase`
- `SugarFeed::pushFeed2()` — publication dans le flux d'activité
- `$locale` global — formatage du nom localisé
- `$bean->fetched_row` — détecte si c'est une création (vide) ou mise à jour

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactFeed` | classe | Logic hook SugarFeed pour les contacts |
| `pushFeed($bean, $event, $arguments)` | méthode | Publie dans le flux si c'est une création de contact |

---

## Interactions

**Appelle :**
- `SugarFeed::pushFeed2($text, $bean)` — publie l'entrée de flux

**Appelée par :** Logic hook `after_save` sur le module Contacts (configuration dans `logic_hooks.php` du module SugarFeed ou du module Contacts).

**Position dans le flux global :** Génère des notifications dans le fil d'activité lors de la création de contacts.

---

## Notes

- Ne publie que lors de la création (quand `$bean->fetched_row` est vide) — pas lors des modifications.
- Le texte publié contient le tag `{SugarFeed.CREATED_CONTACT}` et un lien au format `[Contacts:id:nom]`.
