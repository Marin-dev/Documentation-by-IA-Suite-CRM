# Fichier : vardefs.php (configuration)

**Chemin :** `modules/AM_TaskTemplates/vardefs.php`
**Configure :** Schema du bean `AM_TaskTemplates` / table SQL `am_tasktemplates`
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definition du schema `$dictionary['AM_TaskTemplates']` pour la table `am_tasktemplates`. Genere par Module Builder. Declare les champs d'une tache modele utilisee dans les templates de projets.

---

## Parametres cles

| Parametre | Valeur / Type | Effet |
| --- | --- | --- |
| `table` | `am_tasktemplates` | Table SQL principale |
| `audited` | `true` | Audit des modifications actif |
| `name` | varchar(255), required | Nom de la tache modele |
| `status` | enum, default `Not Started` | Statut initial de la tache lors de la creation |
| `order_number` | int | Ordre de creation des taches dans le projet |
| `task_number` | int | Numero de tache interne |
| `duration` | int | Duree en jours ouvrables |
| `percent_complete` | int | % d'avancement initial |
| `predecessors` | text | IDs des taches predecesseurs |
| `milestone_flag` | bool | Indique si c'est un jalon |
| `relationship_type` | enum | Type de dependance (FS/SS/FF/SF) |
| `priority` | enum | Priorite de la tache |
| `estimated_effort` | int | Effort estime en heures |
| `utilization` | int | Taux d'utilisation ressource (%) |
| `assigned_user_id` | id FK users | Responsable par defaut de la tache |

---

## Relations declarees

| Relation | Type | Description |
| --- | --- | --- |
| `am_tasktemplates_am_projecttemplates` | many-to-many | Templates de projets auxquels cette tache appartient |

---

## Impacte par / impacte

- Lu par `Project::save()` via requete SQL directe (non via BeanFactory) pour creer les `ProjectTask`
- Champs copies tels quels vers `ProjectTask` lors de l'instantiation d'un projet

---

## Points d'attention

- Genere par Module Builder — ne pas modifier directement.
- `order_number` determine l'ordre de creation des `ProjectTask` — tri croissant dans `Project::save()` (ligne 564).
- Les champs de ce schema sont lus en SQL brut dans `Project::save()` : toute modification du schema doit etre reflectee dans ce code.
