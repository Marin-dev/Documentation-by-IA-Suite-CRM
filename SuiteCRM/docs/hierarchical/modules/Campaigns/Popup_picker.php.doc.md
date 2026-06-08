# Fichier : Popup_picker.php

**Chemin :** `modules/Campaigns/Popup_picker.php`
**Type :** PHP - Composant UI (selecteur popup)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Fournit la classe `Popup_Picker` utilisee dans les vues popup de selection de campagnes depuis d'autres modules. Permet de rechercher et selectionner une campagne dans une fenetre modale.

## Role technique

Classe `Popup_Picker`. Contient la logique de rendu HTML du selecteur (champ de recherche, liste de resultats paginee). Utilise les globales de theme.

---

## Dependances cles

- Globales : `$theme`
- Tables : `campaigns` (requetes de recherche)

## Exports / Symboles principaux

- `Popup_Picker` — classe — selecteur popup de campagnes

## Consommateurs identifies

- INCONNU — chercher les usages de `Popup_Picker` dans le repo

## Relations cles

- **Position dans le flux :** Selecteur modal pour associer une campagne a un autre enregistrement

---

## Points d'attention

- Fichier sans `require_once` visible en entete — dependances implicites sur les globales du framework.
