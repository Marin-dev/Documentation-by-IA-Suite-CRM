# Fichier : vardefs.php

**Chemin :** `modules/Tasks/vardefs.php`
**Type :** config (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure
Definition du schema `$dictionary['Task']` pour la table `tasks`. Champs specifiques aux taches : `date_due`, `date_due_flag`, `date_start`, `date_start_flag`, `priority`, `status`.

## Parametres cles (distincts des autres modules d'activites)
| Parametre | Valeur | Effet |
|---|---|---|
| `status` | enum `task_status_dom` | Not Started / In Progress / Completed / Pending Input / Deferred |
| `priority` | enum `task_priority_dom` | High / Medium / Low |
| `date_due` | datetime | date d'echeance |
| `date_due_flag` | bool | indicateur date echeance definie |
| `date_start` | datetime | date de debut (optionnelle) |

## Points d'attention
Pas de champs d'invites (pas de `meetings_users` equivalent) — tache individuelle.
