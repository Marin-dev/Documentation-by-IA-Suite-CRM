# Fichier AOW_Processed.php

**Chemin :** `modules/AOW_Processed/AOW_Processed.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle du journal d'exécution des workflows. Chaque enregistrement trace l'exécution d'un workflow sur un bean spécifique. Utilisé pour éviter la double exécution (quand `multiple_runs = false`) et pour afficher l'historique des traitements.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOW_Processed` | classe | Bean journal d'exécution workflow |

### Champs importants
| Champ | Rôle |
|---|---|
| `aow_workflow_id` | Lien vers le workflow |
| `parent_id` | ID du bean traité |
| `parent_type` | Module du bean traité |
| `status` | Running / Complete / Failed |

## Interactions
- **Appelé par :** `AOW_WorkFlow::run_actions()` (création/mise à jour), `AOW_WorkFlow::check_valid_bean()` (lecture), `AOW_WorkFlow::mark_deleted()` (suppression en cascade)
- **Table BD :** `aow_processed`, relation `aow_processed_aow_actions` (table pivot avec statut par action)

## Notes
- La relation `aow_actions` sur `aow_processed` utilise une table pivot `aow_processed_aow_actions` avec un champ `status` (Complete/Failed) par action.
- Quand `multiple_runs = false` et `status = 'Complete'`, le workflow ne se réexécute pas sur ce bean.
- Un seul bean AOW_Processed par (workflow, bean) quand `multiple_runs = false`.
