# Fichier : en_us.lang.php (DynamicFields)

**Chemin :** `modules/DynamicFields/language/en_us.lang.php`
**Type :** PHP — Configuration (fichier de langue anglais)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Declare le tableau `$mod_strings` contenant toutes les chaines de traduction anglaises du module DynamicFields. Utilise par Studio pour les labels de colonnes, formulaires de configuration et messages d'interface.

## Role technique

Fichier de langue standard SugarCRM. Peuple `$mod_strings` avec des cles comme `COLUMN_TITLE_NAME`, `COLUMN_TITLE_DATA_TYPE`, `LBL_ADD_FIELD`, etc. Charge par `return_module_language($lang, 'DynamicFields')`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `$mod_strings` | tableau | Chaines de traduction du module DynamicFields |

## Exemples de cles notables

| Cle | Valeur |
|---|---|
| `COLUMN_TITLE_NAME` | `'Field Name'` |
| `COLUMN_TITLE_DATA_TYPE` | `'Data Type'` |
| `LBL_ADD_FIELD` | `'Add Field:'` |
| `COLUMN_TITLE_ENABLE_RANGE_SEARCH` | `'Enable Range Search'` |
| `COLUMN_TITLE_PRECISION` | `'Precision'` |

---

## Relations cles

- **Charge par :** `FieldViewer::getLayout()` via `return_module_language()`
- **Surcharge possible dans :** `custom/modules/DynamicFields/language/`
