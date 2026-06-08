# Fichier : en_us.lang.php

**Chemin :** `modules/Campaigns/language/en_us.lang.php`
**Type :** PHP - Configuration (pack de langue anglais)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit toutes les chaines de traduction anglaises pour le module Campaigns. Contient les labels des champs, les messages d'erreur, les titres de pages, les textes de boutons et les etiquettes de navigation du module.

## Role technique

Script procedural. Peuple `$mod_strings` avec les paires cle/valeur de traduction. Charge par le framework lors du rendu de n'importe quelle vue du module Campaigns en langue anglaise.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$mod_strings` — tableau associatif — toutes les chaines de traduction du module Campaigns

## Consommateurs identifies

- Toutes les vues et scripts du module Campaigns (via `$mod_strings`)
- `return_module_language()` du framework

## Relations cles

- **Traduit les labels de :** `vardefs.php` (vname), vues, menus

---

## Points d'attention

- Fichier de reference pour les traductions — toute personnalisation doit aller dans `custom/modules/Campaigns/language/en_us.lang.php`.
