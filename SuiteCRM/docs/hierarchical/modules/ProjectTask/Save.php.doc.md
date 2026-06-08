# Fichier : Save.php

**Chemin :** `modules/ProjectTask/Save.php`
**Type :** PHP - Controleur (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'action `Save` du module ProjectTask. Sauvegarde une tache projet apres l'avoir populee depuis le POST, puis redirige.

## Role technique

Script PHP. Instancie `ProjectTask` via `BeanFactory`, recupere l'enregistrement existant si `record` est fourni, applique le champ `email_id` si present, appelle `populateFromPost()` puis `save()`. Inclut `include/formbase.php` pour `populateFromPost()` et `handleRedirect()`.

---

## Dependances principales

| Import / Fichier | Role |
| --- | --- |
| `include/formbase.php` | `populateFromPost()`, `handleRedirect()` |
| `BeanFactory` | Instanciation de `ProjectTask` |

---

## Exports / Symboles principaux

Aucun symbole exporte. Script d'execution directe.

---

## Relations cles

- **Appele par :** Routeur SuiteCRM (`index.php?module=ProjectTask&action=Save`)
- **Appelle :** `ProjectTask::save()`, `handleRedirect()`

---

## Points d'attention

- `email_id` est traite manuellement avant `populateFromPost()` (ligne 56-58) — probablement pour eviter qu'il soit ecrase.
