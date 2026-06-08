# OppFeed.php

**Chemin :** `modules/Opportunities/SugarFeeds/OppFeed.php`
**Type :** Logic Hook (SugarFeed)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Publie des evenements dans le fil SugarFeed lors de la creation d'une opportunite ou de sa qualification en "Closed Won". Inclut le nom du compte et le montant dans les messages.

## Role technique
Classe `OppFeed` heritant de `FeedLogicBase`. Deux evenements : creation (pas de `fetched_row`) et transition vers `Closed Won` (changement de `sales_stage`).

---

## Dependances / Imports
| Dependance | Chemin | Role |
|---|---|---|
| `FeedLogicBase` | `modules/SugarFeed/feedLogicBase.php` | Classe parente |
| `BeanFactory::newBean('Currencies')` | Formatage du symbole devise |
| `SugarFeed::pushFeed2()` | Publication |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `OppFeed` | Classe | Feed opportunite |
| `pushFeed()` | Methode | Detecte creation/Closed Won et publie |

---

## Points d'attention
- Seule la transition vers `Closed Won` genere un message (pas `Closed Lost` ni les autres transitions).
- Le message inclut les references croisees : `[Accounts:id:name]` et `[Opportunities:id:name]`.
