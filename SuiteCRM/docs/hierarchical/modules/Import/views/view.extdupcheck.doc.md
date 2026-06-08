# view.extdupcheck.php

**Chemin :** `modules/Import/views/view.extdupcheck.php`
**Type :** PHP - Vue (vérification des doublons externes)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de vérification des doublons pour les sources de données externes (EAPM/Google). Variante de `view.dupcheck.php` adaptée au flux d'import depuis des sources externes.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/ImportDuplicateCheck.php`

## Exports / Symboles principaux
- `ImportViewExtdupcheck` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)

## Interactions
- **Appelé par :** wizard d'import externe (Google/EAPM) lors de détection de doublons
- **Appelle :** `ImportDuplicateCheck`

## Notes
- Variante du dupcheck standard pour les imports depuis sources externes.
