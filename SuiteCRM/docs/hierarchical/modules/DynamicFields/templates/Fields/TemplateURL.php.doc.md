# Fichier : TemplateURL.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateURL.php`
**Type :** PHP — Template de champ (URL)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ URL personnalise. Stocke une adresse web et la rend cliquable en vue detail. Sert de classe parente pour `TemplateIFrame`.

## Role technique

Classe `TemplateURL` etendant `TemplateText`. Type `url`. Rendu en lien `<a href="">` en vue detail.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateURL` | classe | Champ URL |
| `$type` | propriete | `'url'` |

---

## Relations cles

- **Etend :** `TemplateText`
- **Etendue par :** `TemplateIFrame`
- **Instanciee par :** `get_widget('url')` dans `FieldCases.php`
