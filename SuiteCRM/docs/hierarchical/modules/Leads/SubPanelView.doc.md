# Fichier : SubPanelView.php

**Chemin :** `modules/Leads/SubPanelView.php`
**Type :** `PHP`
**Categorie :** view (sous-panneau legacy)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Rendu legacy du sous-panneau Leads (liste de leads dans un contexte parent). Affiche la liste des leads passes en `$focus_list` avec le template XTemplate.

## Role technique

Script procedural legacy. Utilise `ListView::processListView()` sur `$focus_list` (variable globale injectee par le framework parent lors du rendu du sous-panneau). Ajoute un lien "Edit Layout" pour les admins.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ListView` | Rendu legacy (XTemplate) |
| `$focus_list` | Variable globale injectee par le framework parent |

## Points d'attention

- Fichier legacy XTemplate. Probablement utilise uniquement dans des contextes ou le framework MVC sous-panneaux n'est pas encore actif.
- Les sous-panneaux modernes utilisent `metadata/subpaneldefs.php` et `metadata/subpanels/default.php`.
