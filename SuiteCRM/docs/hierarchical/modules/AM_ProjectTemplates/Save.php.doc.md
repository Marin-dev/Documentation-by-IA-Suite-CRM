# Fichier : Save.php

**Chemin :** `modules/AM_ProjectTemplates/Save.php`
**Type :** PHP - Controleur (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'action `Save` du module AM_ProjectTemplates. Sauvegarde un modele de projet et redirige vers la vue GanttChart du template.

## Role technique

Script de ~15 lignes utiles. Instancie `AM_ProjectTemplates` via `BeanFactory`, appelle `populateFromPost()`, sauvegarde avec `save(null)`, puis redirige vers `index.php?module=AM_ProjectTemplates&action=view_GanttChart&record={id}` via `handleRedirect()`.

---

## Dependances principales

| Import / Fichier | Role |
| --- | --- |
| `include/formbase.php` | `populateFromPost()`, `handleRedirect()` |
| `BeanFactory` | Instanciation de `AM_ProjectTemplates` |

---

## Exports / Symboles principaux

Aucun symbole exporte. Script d'execution directe.

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=AM_ProjectTemplates&action=Save`)
- **Appelle :** `AM_ProjectTemplates::save()`, `handleRedirect()`

---

## Points d'attention

- La redirection post-sauvegarde cible toujours `view_GanttChart` — pas de retour vers une liste ou une vue detail standard.
