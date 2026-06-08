# Fichier : SubPanelView.php

**Chemin :** `modules/ProjectTask/SubPanelView.php`
**Type :** PHP - Vue (sous-panneau)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche le sous-panneau des taches projet dans d'autres modules (ex: sur la fiche d'un Projet). Construit et affiche la liste des `ProjectTask` liees a l'enregistrement parent.

## Role technique

Script PHP de rendu direct. Utilise les variables globales SuiteCRM standard pour les sous-panneaux (`$app_strings`, `$currentModule`). Rendu via le framework de sous-panneaux.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `$app_strings` (global) | Labels generaux |
| `$currentModule` (global) | Module courant |

---

## Exports / Symboles principaux

Aucun. Script de rendu direct.

---

## Relations cles

- **Appele par :** Framework de sous-panneaux SuiteCRM, notamment depuis la DetailView `Project`
- **Affiche :** Liste des `ProjectTask` liees au projet

---

## Points d'attention

- Contenu partiellement lu — details complets du rendu INCONNUS.
