# Fichier : vardefs.php (configuration)

**Chemin :** `modules/Project/vardefs.php`
**Configure :** Schema du bean `Project` / table SQL `project`
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definition complete du schema `$dictionary['Project']` pour la table `project`. Declare tous les champs, relations et index. Sert de source de verite pour l'ORM SuiteCRM, les vues (Studio), les exports, les formulaires et les recherches.

---

## Parametres cles

| Parametre | Valeur / Type | Effet |
| --- | --- | --- |
| `table` | `project` | Table SQL principale |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `full_text_search` | `true` | Indexation texte integral |
| `unified_search_default_enabled` | `false` | Non actif par defaut en recherche globale |
| `name` | varchar(50), required | Nom du projet |
| `status` | enum `project_status_dom` | Statut du projet |
| `estimated_start_date` | date, required | Validation `isbefore(estimated_end_date)` |
| `estimated_end_date` | date, required | Date de fin du projet |
| `is_template` | bool, default `0` | Si true, le projet est un template reutilisable |
| `assigned_user_id` | id FK users | Responsable du projet |

---

## Relations declarees

| Relation | Type | Description |
| --- | --- | --- |
| `project_users_1` | many-to-many (custom) | Ressources utilisateurs du projet |
| `project_contacts_1` | many-to-many (custom) | Ressources contacts du projet |
| `am_projecttemplates_project_1` | many-to-many | Template de projet associe |
| `project_tasks` (via `ProjectTask.project_id`) | one-to-many | Taches du projet |

---

## Impacte par / impacte

- Charge par `SugarBean` via `VardefManager` au demarrage
- Lu par `Project::save()` pour la detection de changement de template
- Utilise par Studio pour la configuration des champs personnalises

---

## Points d'attention

- La validation `isbefore` sur `estimated_start_date` est cote client — non enforced en PHP.
- `is_template` n'est pas dans `VardefManager::createVardef` standard — declare manuellement.
