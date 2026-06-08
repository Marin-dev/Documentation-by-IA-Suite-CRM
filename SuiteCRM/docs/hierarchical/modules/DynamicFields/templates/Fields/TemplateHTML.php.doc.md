# Fichier : TemplateHTML.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateHTML.php`
**Type :** PHP — Template de champ (HTML statique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ HTML statique personnalise. Permet d'afficher du contenu HTML fixe dans les vues d'un module sans valeur saisie par l'utilisateur.

## Role technique

Classe `TemplateHTML` etendant directement `TemplateField`. Type `html`. Champ non stocke en base — uniquement affichage.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateHTML` | classe | Champ HTML statique |
| `$type` | propriete | `'html'` |

---

## Relations cles

- **Etend :** `TemplateField`
- **Instanciee par :** `get_widget('html')` dans `FieldCases.php`
