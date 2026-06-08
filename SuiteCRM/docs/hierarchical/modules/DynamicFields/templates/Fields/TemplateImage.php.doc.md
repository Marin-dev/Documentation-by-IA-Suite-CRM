# Fichier : TemplateImage.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateImage.php`
**Type :** PHP — Template de champ (image)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ image personnalise permettant le tele-chargement et l'affichage d'une image associee a un enregistrement.

## Role technique

Classe `TemplateImage` etendant `TemplateText`. Type `image`. Stocke probablement le nom/chemin du fichier image.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateImage` | classe | Champ image |
| `$type` | propriete | `'image'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Instanciee par :** `get_widget('image')` dans `FieldCases.php`
