# DocumentPopupPicker.php

**Chemin :** `modules/Documents/DocumentPopupPicker.php`
**Type :** vue

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vue popup de sélection de documents depuis n'importe quel formulaire SuiteCRM (ex. relation document-contrat, pièces jointes email).

## Type

vue

---

## Dépendances clés

- `Popup_Picker` (`include/Popups/Popup_picker.php`) — classe parente
- `Document` (modèle)

## Exports / Symboles principaux

- `DocumentPopupPicker` — classe — popup de sélection de documents

## Interactions

- **Appelé par :** formulaires avec champs de relation vers Documents
- **Appelle :** `Popup_Picker` (héritage)

## Notes

- Pattern standard SuiteCRM popup picker.
