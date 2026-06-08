# Fichier : MyLeads.php

**Chemin :** `modules/Leads/MyLeads.php`
**Type :** `PHP`
**Categorie :** view (liste legacy)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la liste des leads assignes a l'utilisateur courant, en excluant les leads avec les statuts Converted, Dead ou recycled. Utilisable comme page ou depuis le dashboard.

## Role technique

Script procedural legacy utilisant `ListView` (ancienne API XTemplate). Filtre sur `assigned_user_id = current_user->id` et les statuts exclus. Affiche un lien "Edit Layout" pour les admins en mode editinplace.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ListView` | Rendu liste legacy (XTemplate) |
| `BeanFactory::newBean('Leads')` | Bean seed |
| `$current_user` | Filtre sur l'utilisateur courant |

## Points d'attention

- Fichier legacy (XTemplate + `ListView`). Probablement remplace par les vues MVC modernes mais maintenu pour compatibilite.
- Le filtre WHERE est assemble directement en string PHP, sans parameterisation ORM.
