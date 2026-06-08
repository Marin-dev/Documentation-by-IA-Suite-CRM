# Fichier aow_utils.php

**Chemin :** `modules/AOW_WorkFlow/aow_utils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Bibliothèque utilitaire partagée pour les modules AOW et AOR. Fournit des fonctions de récupération des champs de module, des relations, des données d'arbre, et de formatage pour les interfaces dynamiques (AJAX) des éditeurs de workflow et de rapport.

## Type
helper

## Dépendances clés
- `BeanFactory`, `$beanList`
- `ACLController`
- `$app_list_strings`

## Exports / Symboles principaux (INCONNU partiels — basé sur les usages)

| Symbole | Rôle |
|---|---|
| `getModuleFields()` | Retourne les options HTML des champs d'un module pour les sélecteurs |
| `getModuleField()` | Retourne le widget HTML d'un champ spécifique |
| `getModuleTreeData()` | Retourne les données de l'arbre modules/relations pour jqtree |
| `getModuleRelationships()` | Retourne les relations disponibles d'un module |
| `getRelatedModule()` | Résout le nom du module lié via une relation |
| `fixUpFormatting()` | Normalise une valeur de formulaire selon le type de champ du module |
| `getDateField()` | Génère le widget de saisie de date relative |
| `getAssignField()` | Génère le widget d'assignation (Round Robin, Least Busy, Random) |
| `getDropdownList()` | Génère une liste déroulante depuis app_list_strings |

## Interactions
- **Appelé par :** `AOR_Report.php`, `AOR_ReportsController`, `AOR_Condition.php`, `AOR_Field.php`, `AOW_WorkFlow.php`, `AOW_Condition.php`, `AOW_Action.php`, vues AOW/AOR
- **Appelle :** `BeanFactory`, `ACLController`

## Notes
Fichier partagé entre les deux familles de modules AOR et AOW — toute modification impacte les deux.
