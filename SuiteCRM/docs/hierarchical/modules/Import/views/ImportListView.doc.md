# ImportListView.php

**Chemin :** `modules/Import/views/ImportListView.php`
**Type :** PHP - Vue (liste)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de vue pour l'affichage des résultats d'import sous forme de liste. Étend ou utilise `ListViewSmarty` pour rendre les enregistrements importés (succès, erreurs, doublons) sous forme tabulaire.

## Type
view

## Dépendances clés
- `include/ListView/ListViewSmarty.php` — moteur de liste

## Exports / Symboles principaux
- `ImportListView` (classe)
  - `$data` — données à afficher
  - `$headerColumns` — colonnes de l'entête

## Interactions
- **Appelé par :** vues d'import (view.confirm, view.error, view.dupcheck)
- **Appelle :** `ListViewSmarty`

## Notes
- Utilisée pour afficher les résultats de confirmation d'import, les erreurs, et les doublons détectés.
