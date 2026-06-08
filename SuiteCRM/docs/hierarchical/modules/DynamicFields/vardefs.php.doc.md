# Fichier : vardefs.php

**Chemin :** `modules/DynamicFields/vardefs.php`
**Type :** PHP — Configuration (schema de la table fields_meta_data)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit le schema de la table `fields_meta_data` dans `$dictionary['FieldsMetaData']`. Cette table stocke les metadonnees de tous les champs dynamiques personnalises de l'application.

## Role technique

Fichier de configuration peuplant `$dictionary['FieldsMetaData']`. Declare les colonnes avec types, longueurs, labels et validations.

---

## Schema de la table fields_meta_data

| Colonne | Type | Notes |
|---|---|---|
| `id` | varchar 255 | Cle primaire |
| `name` | varchar 255 | Nom technique du champ |
| `vname` | varchar 255 | Label du champ |
| `comments` | varchar 255 | Commentaire |
| `help` | varchar 255 | Texte d'aide |
| `custom_module` | varchar 255 | Module proprietaire |
| `type` | varchar 255 | Type de champ |
| `len` | int 11 | Longueur max (validation: 1-255) |
| `required` | bool | Champ obligatoire |
| `default_value` | varchar 255 | Valeur par defaut |
| `date_modified` | datetime | Date modification |
| `deleted` | bool | Soft delete |
| `audited` | bool | Audit active |
| `ext1`, `ext2`, `ext3`, `ext4` | varchar | Extensions generiques |
| `duplicate_merge` | bool | Fusion doublons |
| `reportable` | bool | Reportable |
| `inline_edit` | bool | Edition inline |
| `unified_search` | bool | Recherche unifiee |

---

## Impacte par / impacte

- Utilise par `FieldsMetaData.php` (bean)
- Charge par le framework SugarCRM au demarrage du module DynamicFields
- Surcharge possible dans `custom/Extension/modules/DynamicFields/Ext/Vardefs/`
