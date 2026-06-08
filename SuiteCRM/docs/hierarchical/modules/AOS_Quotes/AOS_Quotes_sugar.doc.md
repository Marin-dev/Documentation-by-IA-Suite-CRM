# AOS_Quotes_sugar.php

**Chemin :** `modules/AOS_Quotes/AOS_Quotes_sugar.php`
**Type :** PHP - Modele genere (classe de base generee)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe de base generee par SugarCRM Studio pour le module AOS_Quotes. Definit les attributs et la structure de base du bean devis. Ne doit pas etre modifiee directement — les customisations vont dans `AOS_Quotes.php`.

## Role technique
Etend `Basic`. Declare tous les attributs du bean correspondant aux colonnes de la table `aos_quotes`. Positionne `$lineItems = true` pour indiquer que ce module supporte les lignes de produits.

---

## Attributs cles declares
- `$table_name = 'aos_quotes'`
- `$module_dir = 'AOS_Quotes'`
- `$importable = true`
- `$lineItems = true` — indicateur de support des lignes produits
- `$disable_row_level_security = true` — compatibilite CE

**Attributs metier (INCONNU partiels — suite non lue) :** `number`, `quote_stage`, `valid_until`, `total_amt`, `total_amount`, `discount_amount`, `subtotal_amount`, `tax_amount`, `shipping_amount`, etc.

## Relations cles
- **Etendue par :** `AOS_Quotes`
- **Table DB :** `aos_quotes`

---

## Points d'attention
- Fichier genere — ne pas modifier manuellement.
- Les modifications de schema Studio regenerent ce fichier.
