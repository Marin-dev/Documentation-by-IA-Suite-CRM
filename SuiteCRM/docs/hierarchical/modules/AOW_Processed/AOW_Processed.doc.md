# AOW_Processed.php

**Chemin :** `modules/AOW_Processed/AOW_Processed.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele de traçabilite des executions de workflow AOW. Enregistre chaque execution d'un workflow sur un enregistrement, avec le statut (Running, Complete, Failed). Permet d'eviter les doubles executions quand `multiple_runs = false`.

## Role technique
Etend `Basic`. Classe simple sans logique metier specifique. Les instances sont creees et mises a jour par `AOW_WorkFlow->run_actions()`. Le statut evolue de `Running` vers `Complete` ou `Failed` selon le resultat des actions.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aow_workflow_id` | FK vers le workflow execute |
| `parent_id` | ID du bean sur lequel le workflow a tourne |
| `parent_type` | Module du bean (`module_dir`) |
| `status` | Statut (Running, Complete, Failed) |
| `aow_action_id` | INCONNU — semble non utilise directement |
| `aow_action` | INCONNU — semble non utilise directement |

## Relations cles
- **Cree/mis a jour par :** `AOW_WorkFlow->run_actions()`
- **Lu par :** `AOW_WorkFlow->check_valid_bean()` et `build_flow_query_where()` pour filtrer les records deja traites
- **Table DB :** `aow_processed`
- **Relations :** vers `aow_actions` via la table `aow_processed_aow_actions` (statut par action)

---

## Points d'attention
- La relation `aow_actions` (table de jonction `aow_processed_aow_actions`) stocke le statut par action individuelle (`Complete` ou `Failed`).
- Quand `multiple_runs = true`, les entrees precedentes ne sont pas supprimees — multiplication des enregistrements.
- Supprime en cascade lors de la suppression du workflow parent (via `AOW_WorkFlow->mark_deleted()`).
