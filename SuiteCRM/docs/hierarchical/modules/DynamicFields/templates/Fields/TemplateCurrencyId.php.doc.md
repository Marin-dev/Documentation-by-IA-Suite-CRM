# Fichier : TemplateCurrencyId.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateCurrencyId.php`
**Type :** PHP — Template de champ (ID devise)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente le champ `currency_id` associe automatiquement a tout champ devise personnalise. Stocke la reference a la devise utilisee pour le champ currency parent.

## Role technique

Classe `TemplateCurrencyId` etendant `TemplateId`. Type `currency_id`. Cree et supprime automatiquement par `TemplateCurrency::save()` et `delete()`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateCurrencyId` | classe | Champ ID devise |
| `$type` | propriete | `'currency_id'` |

---

## Relations cles

- **Etend :** `TemplateId`
- **Cree par :** `TemplateCurrency::save()`
- **Supprime par :** `TemplateCurrency::delete()`
