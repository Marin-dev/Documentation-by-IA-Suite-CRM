# Fichier : TemplateCurrency.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateCurrency.php`
**Type :** PHP — Template de champ (devise)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ devise personnalise. A la sauvegarde, cree automatiquement un champ `currency_id` associe pour stocker la devise de reference. A la suppression, supprime egalement ce champ `currency_id`.

## Role technique

Classe `TemplateCurrency` etendant `TemplateRange`. Type `currency`. Surcharge `save($df)` pour normaliser la valeur par defaut (`unformat_number`), appeler le save parent, puis instancier et sauvegarder un `TemplateCurrencyId` avec `name='currency_id'`. Surcharge `delete($df)` pour supprimer egalement le `TemplateCurrencyId`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateCurrency` | classe | Champ devise |
| `$type` | propriete | `'currency'` |
| `$precision` | propriete | `6` (decimales) |
| `$len` | propriete | `26` |

## Dependances principales

| Import | Role |
|---|---|
| `TemplateCurrencyId` | Champ ID devise associe |
| `TemplateRange` | Classe parente (support recherche par plage) |

---

## Relations cles

- **Etend :** `TemplateRange`
- **Cree automatiquement :** `TemplateCurrencyId` (champ `currency_id`)
- **Instanciee par :** `get_widget('currency')` dans `FieldCases.php`

---

## Points d'attention

- La sauvegarde d'un champ currency cree toujours deux champs : le champ valeur ET `currency_id` — a prendre en compte lors de suppressions manuelles en base.
- `unformat_number($this->default)` normalise la valeur independamment de la locale.
