# MyOpportunitiesDashlet.php

**Chemin :** `modules/Opportunities/Dashlets/MyOpportunitiesDashlet/MyOpportunitiesDashlet.php`
**Type :** Vue (dashlet)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Dashlet "Mes Opportunites" affichable sur le tableau de bord. Presente la liste configurable des opportunites de l'utilisateur courant.

## Role technique
Classe `MyOpportunitiesDashlet` heritant de `DashletGeneric`. Charge les colonnes et filtres depuis `MyOpportunitiesDashlet.data.php`. La methode `process()` est surchargee mais contient uniquement un appel parent (un fix pour le champ `amount` vs `amount_usdollar` est commente).

---

## Points d'attention
- Commentaire de correction concernant `amount` vs `amount_usdollar` (fix 4.5.0g pour upgrade) laisse en code commente — peut necessiter attention lors des mises a jour.
