# quotes_SeedData.php

**Chemin :** `install/seed_data/quotes_SeedData.php`
**Type :** `PHP (installeur — données de démo devis)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Crée les devis (Quotes) de démonstration lors de l'installation avec données de démo. Itère sur `$sugar_demodata['quotes_seed_data']['quotes']` et crée des enregistrements `Quote` avec leurs lignes de produits.

**Type :** installer / seed data

---

## Dépendances clés
- `sugarEntry` — protection d'accès
- `modules/Quotes/Quote.php` — classe `Quote`
- `modules/ProductBundleNotes/ProductBundleNote.php` — classe `ProductBundleNote`
- `modules/Products/Product.php` — classe `Product`
- `$current_user`, `$sugar_demodata` — globaux

## Exports / Symboles principaux
Aucune classe exportée. Logique procédurale : crée des instances de `Quote` via `new Quote()`.

## Interactions
- **Appelé par :** `install/populateSeedData.php` (INCONNU : inclusion explicite ou dynamique)
- **Appelle :** `Quote::save()`, `create_guid()`, `BeanFactory::newBean()`
- **Position dans le flux global :** création des devis de démo, après les utilisateurs et équipes

---

## Notes
- Utilise `create_guid()` pour les IDs (contrairement aux utilisateurs seed qui ont des IDs nommés).
- `$focus->new_with_id = true` : insertion avec ID prédéfini.
- Dépend de `$sugar_demodata['quotes_seed_data']['quotes']` défini dans `demoData.en_us.php` (INCONNU : structure exacte).
