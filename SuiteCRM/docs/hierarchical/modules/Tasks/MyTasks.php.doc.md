# Fichier : MyTasks.php

**Chemin :** `modules/Tasks/MyTasks.php`
**Type :** PHP - Vue (liste "Mes Taches")
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la liste des taches assignees a l'utilisateur courant qui ne sont ni completees ni differees et dont la date de debut est aujourd'hui ou dans le passe. Utilise le composant `ListView` standard de SuiteCRM.

## Role technique

Script PHP de rendu direct (pas de classe). Construit une clause SQL `WHERE` filtrant sur `assigned_user_id = current_user.id`, statut different de `Completed` et `Deferred`, et `date_start <= demain`. Utilise `$db->convert()` pour la compatibilite multi-SGBD (formatage date/heure). Instancie `ListView` et affiche la liste.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `ListView` | Composant de rendu de liste SuiteCRM |
| `BeanFactory::newBean('Tasks')` | Seed bean pour la requete |
| `$timedate` (global) | Calcul de "demain" en format DB |
| `$current_user` (global) | Filtrage par utilisateur courant |

---

## Exports / Symboles principaux

Aucun. Script de rendu direct.

---

## Relations cles

- **Appele par :** INCONNU (probablement accessible via `index.php?module=Tasks&action=MyTasks`)
- **Appelle :** `ListView::display()` avec filtre SQL

---

## Points d'attention

- Le filtre inclut les taches sans `date_start` (NULL) — elles apparaissent toujours dans la liste.
- Utilise `$db->convert()` pour `date_format` et `time_format` — requete sensible aux variations de SGBD.
