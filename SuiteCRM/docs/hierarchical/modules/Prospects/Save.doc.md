# Save.php

**Chemin :** `modules/Prospects/Save.php`
**Type :** PHP - Script d'action (sauvegarde)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Gère la sauvegarde d'un enregistrement Prospect via `ProspectFormBase::handleSave()`. Définit les valeurs de retour par défaut si absentes.

## Type
helper

## Dépendances clés
- `modules/Prospects/ProspectFormBase.php`
- `$_REQUEST['return_module']`, `$_REQUEST['return_action']`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** formulaires EditView du module Prospects
- **Appelle :** `ProspectFormBase::handleSave('', true, false)`

## Notes
- Délègue entièrement la logique de sauvegarde à `ProspectFormBase`.
