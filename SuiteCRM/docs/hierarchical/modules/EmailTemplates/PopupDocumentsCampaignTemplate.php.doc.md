# PopupDocumentsCampaignTemplate.php

**Chemin :** `modules/EmailTemplates/PopupDocumentsCampaignTemplate.php`
**Type :** vue

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Vue popup de sélection de documents pour l'attachement à un gabarit de campagne email. Étend `Popup_Picker` pour afficher un sélecteur de documents dans une fenêtre contextuelle.

## Type

vue

---

## Dépendances clés

- `Popup_Picker` (`include/Popups/Popup_picker.php`) — classe parente
- `Documents` (modèle)

## Exports / Symboles principaux

- `DocumentPopupPicker` — classe — popup de sélection de documents pour les templates email

## Interactions

- **Appelé par :** éditeur de template email (bouton "Joindre document")
- **Appelle :** `Popup_Picker` (héritage)

## Notes

- Réutilise l'infrastructure popup générique de SugarCRM.
