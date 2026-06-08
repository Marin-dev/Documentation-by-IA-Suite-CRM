# view.error.php

**Chemin :** `modules/Import/views/view.error.php`
**Type :** PHP - Vue (erreurs d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue d'affichage des erreurs d'import. Présente les lignes qui n'ont pas pu être importées (données invalides, champs requis manquants, etc.) sous forme de liste avec les messages d'erreur correspondants.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/views/ImportListView.php`

## Exports / Symboles principaux
- `ImportViewError` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)

## Interactions
- **Appelé par :** vue step4 après l'import (lien "Voir les erreurs")
- **Appelle :** `ImportListView`

## Notes
- Permet d'exporter les lignes en erreur pour correction et ré-import.
