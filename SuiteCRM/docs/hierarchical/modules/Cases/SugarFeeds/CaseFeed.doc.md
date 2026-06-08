# CaseFeed.php

**Chemin :** `modules/Cases/SugarFeeds/CaseFeed.php`
**Type :** Logic Hook (SugarFeed)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Publie dans le fil SugarFeed lors de la creation d'un cas ou de sa fermeture. Inclut le nom du compte et la description du cas.

## Role technique
Classe `CaseFeed` heritant de `FeedLogicBase`. Deux evenements : creation (`empty(fetched_row) && in_save`) et fermeture (changement de statut contenant "Closed").

---

## Points d'attention
- Creation detectee par `$bean->in_save` ET `empty(fetched_row)` (plus strict que les autres feeds).
- Si `account_name` n'est pas dans le bean lors de la creation, effectue un `BeanFactory::getBean('Accounts')` supplementaire pour le recuperer.
- Fermeture : tout statut contenant "Closed" genere un message (pas seulement "Closed").
