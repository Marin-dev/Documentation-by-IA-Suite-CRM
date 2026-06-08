# Fichier : gantt.php

**Chemin :** `modules/AM_ProjectTemplates/gantt.php`
**Type :** PHP - Helper de rendu (View Helper)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le diagramme de Gantt pour un modele de projet (`AM_ProjectTemplates`). Copie conforme de `modules/Project/gantt.php` adaptee aux templates — prend en compte les taches du template et non les dates reelles.

## Role technique

Classe `Gantt` (meme nom que dans `Project/gantt.php` — risque de conflit si les deux fichiers sont inclus simultanement). Constructeur appelle `draw()` uniquement si des taches existent. Differece avec `Project/gantt.php` : verifie `!empty($this->tasks)` avant de dessiner.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `AM_ProjectTemplatesController` | Appelant (via `include_once`) |

---

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `Gantt` | Classe | Rendu Gantt pour template de projet |

---

## Relations cles

- **Appele par :** Controleur AM_ProjectTemplates via `include_once`
- **Position dans le flux :** Vue GanttChart du template de projet

---

## Points d'attention

- Meme nom de classe que `modules/Project/gantt.php` — ne jamais inclure les deux fichiers dans la meme requete.
- La version template verifie `!empty($this->tasks)` (ligne 35-37) contrairement a la version Project — meilleure protection.
