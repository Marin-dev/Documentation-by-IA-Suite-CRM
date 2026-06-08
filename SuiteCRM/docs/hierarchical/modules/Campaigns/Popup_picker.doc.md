# Popup_picker.php

**Chemin :** `modules/Campaigns/Popup_picker.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Classe de sélection en popup pour le module Campaigns. Fournit une interface de recherche et sélection de campagnes dans une fenêtre popup, utilisée lors de l'association d'une campagne depuis d'autres modules.

**Type :** helper / composant popup

---

## Dépendances clés

- `$theme` global — pour le CSS/thème de la popup
- Table `campaigns` — requête de recherche/liste
- `$_REQUEST['query']` — paramètre de recherche

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Popup_Picker` | classe | Gère l'affichage et la recherche dans la popup de sélection de campagne |
| `_get_where_clause()` | méthode | Construit la clause WHERE pour la recherche de campagnes |
| `__construct()` | méthode | Initialisation de la classe |

---

## Interactions

**Appelle :**
- Requêtes directes sur la table `campaigns`

**Appelée par :** INCONNU — probablement invoquée depuis des popups dans d'autres modules pour sélectionner une campagne.

**Position dans le flux global :** Composant d'interface de sélection, chargé via un appel popup depuis les formulaires d'édition.

---

## Notes

- Le fichier source n'expose que le début de la classe — la méthode principale d'affichage (`process_page()` ou similaire) est INCONNU sans lecture complète.
