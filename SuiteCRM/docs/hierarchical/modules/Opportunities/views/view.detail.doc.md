# view.detail.php

**Chemin :** `modules/Opportunities/views/view.detail.php`
**Type :** Vue (detail view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue de detail d'une opportunite. Enrichit l'affichage avec le symbole et le code ISO de la devise (CURRENCY) pour l'affichage du montant.

## Role technique
Classe `OpportunitiesViewDetail` heritant de `ViewDetail`. Surcharge `display()` : charge le bean `Currencies` correspondant au `currency_id` de l'opportunite et assigne la variable Smarty `CURRENCY` (format : "EUR €").

---

## Points d'attention
- Si la devise est supprimee (`deleted == 1`), utilise les valeurs par defaut via `getDefaultISO4217()` et `getDefaultCurrencySymbol()`.
- RAS autrement.
