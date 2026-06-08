# Fichier : AM_TaskTemplates.php

**Chemin :** `modules/AM_TaskTemplates/AM_TaskTemplates.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe metier du module AM_TaskTemplates (modeles de taches). Represente une tache type destinee a etre utilisee dans un modele de projet (`AM_ProjectTemplates`). Lors de la creation d'un projet a partir d'un template, chaque `AM_TaskTemplates` est convertie en `ProjectTask` avec ses caracteristiques (nom, duree, priorite, predecesseurs, etc.).

## Role technique

Herite de `AM_TaskTemplates_sugar` (classe generee auto). La classe elle-meme est vide — marquee "FOR DEVELOPERS TO MAKE CUSTOMIZATIONS IN". Toute la logique metier est dans la classe parente generee `AM_TaskTemplates_sugar`.

---

## Dependances principales

| Import / Classe | Role |
|---|---|
| `AM_TaskTemplates_sugar` (`modules/AM_TaskTemplates/AM_TaskTemplates_sugar.php`) | Classe parente avec vardefs et logique de base |
| `SugarBean` | Ancetre final via la chaine d'heritage |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `AM_TaskTemplates` | Classe | Modele de tache pour template de projet |

**Tables DB :** `am_tasktemplates`

**Champs clés (issus de la table, lus dans `Project::save()`) :** `name`, `status`, `priority`, `percent_complete`, `predecessors`, `milestone_flag`, `relationship_type`, `task_number`, `order_number`, `estimated_effort`, `utilization`, `assigned_user_id`, `description`, `duration`

---

## Relations cles

- **Appele par :** `Project::save()` (lecture via SQL direct, ligne 555-564) lors de l'application d'un template
- **Lie a :** `AM_ProjectTemplates` via `am_tasktemplates_am_projecttemplates_c`
- **Produit :** `ProjectTask` lors de l'instantiation d'un projet depuis un template

---

## Points d'attention

- La classe est vide — toute personnalisation doit se faire ici (philosophie SuiteCRM "customization layer").
- `AM_TaskTemplates` n'est pas instanciee via `BeanFactory` dans `Project::save()` — les donnees sont lues par requete SQL directe, ce qui contourne les hooks et validations du bean.
- Le champ `order_number` determine l'ordre de creation des taches dans le projet.
