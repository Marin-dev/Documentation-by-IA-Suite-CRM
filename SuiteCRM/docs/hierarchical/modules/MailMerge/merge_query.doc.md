# merge_query.php

**Chemin :** `modules/MailMerge/merge_query.php`
**Type :** PHP - Helper (requêtes SQL de fusion)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit la fonction `get_merge_query()` qui retourne les requêtes SQL appropriées pour la fusion de courrier selon le module source et le module de fusion. Contient un tableau de requêtes SQL hardcodées pour les relations entre modules.

## Type
helper

## Dépendances clés
- `SugarBean $seed` — bean source
- `$merge_module`, `$key` — module et ID de l'enregistrement à fusionner

## Exports / Symboles principaux
- `get_merge_query($seed, $merge_module, $key)` (fonction) — retourne la requête SQL de sélection pour la fusion
  - Supporte : Contacts ↔ Accounts, Opportunities, Cases, Bugs, Quotes ; Opportunities ↔ Accounts

## Interactions
- **Appelé par :** scripts Step du wizard MailMerge
- **Appelle :** rien (données statiques)

## Notes
- Requêtes SQL codées en dur dans un tableau multi-dimensionnel (lignes 50-60+).
- Utilise des LEFT JOIN pour les tables de relation inter-modules.
- À étendre si de nouveaux modules doivent être supportés dans la fusion.
