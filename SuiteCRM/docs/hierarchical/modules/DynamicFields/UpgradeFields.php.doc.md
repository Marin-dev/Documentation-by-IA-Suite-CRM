# Fichier : UpgradeFields.php

**Chemin :** `modules/DynamicFields/UpgradeFields.php`
**Type :** PHP — Script de maintenance (synchronisation champs custom)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Script de maintenance qui verifie et synchronise les champs dynamiques enregistres dans `fields_meta_data` avec la structure reelle des tables de la base de donnees. Utilise apres une mise a jour ou en cas de desynchronisation. Supporte un mode simulation (sans modifications) et un mode execution reelle.

## Role technique

Script procedural. Requete tous les enregistrements de `fields_meta_data` (non supprimes), groupe par module. Pour chaque module, verifie si la table `{module}_cstm` existe, la cree si absente. Pour chaque champ, verifie s'il existe physiquement en DB ; s'il est manquant et que le mode `run` est actif, tente de l'ajouter. Le mode simulation (`!isset($_REQUEST['run'])`) n'effectue que des lectures et vide le cache.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/DynamicFields/FieldCases.php` | Fabrique de widgets par type |
| `modules/DynamicFields/DynamicField.php` | Gestionnaire champs dynamiques |
| `DBManagerFactory` | Acces base de donnees |
| `$beanList` / `$beanFiles` (globaux) | Resolution classes modules |

## Exports / Symboles principaux

Aucun. Script d'action produisant du HTML de rapport.

---

## Relations cles

- **Appele par :** administrateur via URL (INCONNU exact — probablement `index.php?module=DynamicFields&action=UpgradeFields`)
- **Appelle :** `DynamicField::createCustomTable()`, `DynamicField::setup()`, `get_widget()`
- **Lit :** `fields_meta_data` (DB)

---

## Points d'attention

- Par defaut en mode simulation — ajouter `&run=1` a l'URL pour executer reellement les modifications.
- Si un module n'existe plus dans `$beanList`, il est silencieusement ignore.
- Affiche la progression directement en HTML (echo) — pas de log structuré.
