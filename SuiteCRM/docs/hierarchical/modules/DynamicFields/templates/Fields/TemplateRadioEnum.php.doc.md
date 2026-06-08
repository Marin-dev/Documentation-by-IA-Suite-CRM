# Fichier : TemplateRadioEnum.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateRadioEnum.php`
**Type :** PHP — Template de champ (boutons radio)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ de selection sous forme de boutons radio (affichage alternatif a la liste deroulante pour les enums). Partage la meme logique metier que `TemplateEnum`.

## Role technique

Classe `TemplateRadioEnum` etendant `TemplateEnum`. Type `radioenum`. Le rendu utilise des `<input type="radio">` au lieu d'un `<select>`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateRadioEnum` | classe | Champ boutons radio |
| `$type` | propriete | `'radioenum'` |

---

## Relations cles

- **Etend :** `TemplateEnum`
- **Instanciee par :** `get_widget('radioenum')` dans `FieldCases.php`
