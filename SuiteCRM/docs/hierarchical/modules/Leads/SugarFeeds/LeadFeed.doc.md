# Fichier : LeadFeed.php

**Chemin :** `modules/Leads/SugarFeeds/LeadFeed.php`
**Type :** `PHP`
**Categorie :** logic hook (SugarFeed)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Publie des evenements dans le fil d'activite SugarFeed lors de la creation d'un lead ou de sa conversion. Deux evenements : creation (nouveau lead sans `fetched_row`) et conversion (changement de statut vers `Converted`).

## Role technique

Classe `LeadFeed` heritant de `FeedLogicBase`. Implemente `pushFeed()` : detecte le type d'evenement et pousse un message formate vers `SugarFeed::pushFeed2()`.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `FeedLogicBase` | `modules/SugarFeed/feedLogicBase.php` | Classe parente |
| `SugarFeed::pushFeed2()` | framework | Publication dans le fil d'activite |
| `$locale` | framework | Formatage du nom (prenom + nom) |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `LeadFeed` | classe | Feed pour les evenements lead |
| `pushFeed()` | methode | Detecte creation/conversion et publie le message |

## Points d'attention

- La detection de la conversion : `fetched_row['status'] != $bean->status && $bean->status == 'Converted'`.
- Les autres changements de statut ne generent pas de message dans le feed.
