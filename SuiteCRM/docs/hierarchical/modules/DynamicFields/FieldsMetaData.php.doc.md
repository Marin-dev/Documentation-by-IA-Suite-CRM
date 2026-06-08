# Fichier : FieldsMetaData.php

**Chemin :** `modules/DynamicFields/FieldsMetaData.php`
**Type :** PHP — Modele (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un enregistrement de la table `fields_meta_data`, qui stocke les metadonnees de chaque champ dynamique personnalise cree via Studio. Chaque ligne correspond a un champ custom d'un module donne.

## Role technique

Classe `FieldsMetaData` etendant `SugarBean`. Expose tous les champs de la table comme proprietes publiques. Desactive les champs personnalises recurssifs (`disable_custom_fields = true` implicite via `SugarBean`). La table est `fields_meta_data`.

---

## Dependances principales

| Import | Role |
|---|---|
| `SugarBean` | Classe parente |
| `modules/DynamicFields/vardefs.php` | Schema de la table |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `FieldsMetaData` | classe | Bean metadonnees de champs custom |
| `$table_name` | propriete | `fields_meta_data` |
| `$custom_module` | propriete | Nom du module proprietaire du champ |
| `$type` | propriete | Type de champ (varchar, enum, relate, etc.) |
| `$ext1`, `$ext2`, `$ext3` | proprietes | Extensions generiques (ex: `ext1` = liste d'options pour enum) |
| `$audited` | propriete | Si le champ est audite |
| `$duplicate_merge` | propriete | Comportement lors de fusion doublons |
| `$reportable` | propriete | Si le champ est reportable |

## Consommateurs identifies

- `modules/DynamicFields/UpgradeFields.php` — requete directe sur `fields_meta_data`
- `DynamicField.php` — lecture/ecriture via DBManager
- Studio (INCONNU exact)

---

## Relations cles

- **Etend :** `SugarBean`
- **Table :** `fields_meta_data`
- **Schema defini dans :** `modules/DynamicFields/vardefs.php`

---

## Points d'attention

- `$required_fields` est declare avec des cles incorrectes (`date_start`, `time_start`) pour un bean de metadonnees — heritage probable, a verifier si ces champs sont reellement valides.
- `$ext1` a `$ext3` sont des champs fourre-tout dont la semantique depend du type de champ (ex: `ext1` = dropdown key pour enum, `ext1` = taille max pour varchar).
