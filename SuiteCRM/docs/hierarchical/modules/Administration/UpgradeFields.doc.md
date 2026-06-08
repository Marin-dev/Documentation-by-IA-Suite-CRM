# UpgradeFields.php

**Chemin :** `modules/Administration/UpgradeFields.php`
**Type :** PHP (action / migration BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Synchronise la structure des tables de champs personnalises (`*_cstm`) avec les definitions dans `fields_meta_data`. Assure que les colonnes existent et ont le bon type apres une importation de champs personnalises.

## Role technique
Requete sur `fields_meta_data WHERE deleted=0`, regroupe par module. Utilise `DynamicField` et `FieldCases` pour comparer les colonnes existantes et creer/modifier les colonnes manquantes.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/DynamicFields/DynamicField.php` | Gestion des champs personnalises |
| `modules/DynamicFields/FieldCases.php` | Types de champs |

## Interactions
- **Inclus par :** `ImportCustomFieldStructure.php` (apres import)
- **Lit depuis :** `fields_meta_data`
- **Modifie :** Tables `*_cstm`
