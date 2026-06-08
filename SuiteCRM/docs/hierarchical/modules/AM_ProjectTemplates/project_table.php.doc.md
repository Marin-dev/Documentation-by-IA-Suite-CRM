# Fichier : project_table.php

**Chemin :** `modules/AM_ProjectTemplates/project_table.php`
**Type :** PHP - Helper de rendu (View Helper)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le tableau HTML des taches modeles dans la vue Gantt d'un template de projet (`AM_ProjectTemplates`). Affiche les memes colonnes que `Project/project_table.php` mais pour les `AM_TaskTemplates`.

## Role technique

Classe `AM_ProjectTemplatesTable` avec constructeur appelant `draw()`. Prend en parametre `$project_template_id` et la liste des taches. Rendu HTML direct par echo. Utilise `TimeDate` pour le formatage.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `TimeDate` | Formatage des dates |
| `$mod_strings` (global) | Labels traduits |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AM_ProjectTemplatesTable` | Classe | Tableau des taches dans la vue Gantt template |
| `AM_ProjectTemplatesTable::draw()` | Methode | Genere le HTML du tableau |

---

## Relations cles

- **Appele par :** Controleur AM_ProjectTemplates via `include_once`
- **Position dans le flux :** Complement de `AM_ProjectTemplates/gantt.php`

---

## Points d'attention

- Nom de classe different de `ProjectTable` — pas de conflit si les deux sont inclus simultanement.
- `$project_template_id` est passe au constructeur mais l'usage dans `draw()` est a verifier (ajout de liens d'edition des taches template).
