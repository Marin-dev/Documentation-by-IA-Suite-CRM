# CasesJjwg_MapsLogicHook.php

**Chemin :** `modules/Cases/CasesJjwg_MapsLogicHook.php`
**Type :** Logic Hook
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Logic hook de geocodage pour le module Cases. Gere le geocodage du cas lui-meme et la propagation aux reunions liees et aux entites nouvellement reliees/deliees.

## Role technique
Classe `CasesJjwg_MapsLogicHook`. Quatre methodes : `before_save`, `after_save` (reunions), `after_relationship_add`, `after_relationship_delete`. Pas de propagation aux projets (contrairement aux Accounts).

---

## Points d'attention
- Identique a `AccountsJjwg_MapsLogicHook` sans les methodes projets/opportunites.
- Toutes conditionnees par `logic_hooks_enabled`.
