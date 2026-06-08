# view.dupcheck.php

**Chemin :** `modules/Import/views/view.dupcheck.php`
**Type :** PHP - Vue (vérification des doublons)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de vérification des doublons lors de l'import. Affiche les enregistrements importés qui correspondent à des enregistrements existants (via `ImportDuplicateCheck`) et permet à l'utilisateur de décider comment les traiter (ignorer, mettre à jour, créer quand même).

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `modules/Import/ImportDuplicateCheck.php`

## Exports / Symboles principaux
- `ImportViewDupcheck` (classe, étend `ImportView`) — INCONNU (classe non lue en détail)

## Interactions
- **Appelé par :** wizard d'import lors de la détection de doublons
- **Appelle :** `ImportDuplicateCheck`

## Notes
- Étape optionnelle du wizard — n'apparaît que si des doublons sont détectés.
