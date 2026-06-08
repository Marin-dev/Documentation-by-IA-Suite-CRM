# Fichier : Save.php

**Chemin :** `modules/DynamicFields/Save.php`
**Type :** PHP — Script d'action (sauvegarde champ dynamique legacy)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Sauvegarde un nouveau champ dynamique pour un module, puis injecte le champ dans la mise en page via `AddField`. Semble etre un script legacy utilise par une ancienne interface de creation de champs dynamiques.

## Role technique

Script procedural. Charge `DynamicField` pour le module cible, instancie le bean du module, appelle `setup()`, puis `addField()` avec les parametres de la requete. Recupere le HTML du champ et son label, instancie `AddField` pour injecter le champ dans la mise en page du formulaire appelant (via `window.opener`). Ferme la fenetre avec `window.close()`.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/DynamicFields/DynamicField.php` | Gestionnaire champs dynamiques |
| `modules/DynamicLayout/AddField.php` | Injection dans la mise en page |
| `$beanList` / `$beanFiles` (globaux) | Resolution classe du module |

## Exports / Symboles principaux

Aucun. Script d'action produisant JavaScript.

---

## Relations cles

- **Appele par :** INCONNU — ancienne interface popup de creation de champ (non identifiee)
- **Appelle :** `DynamicField::addField()`, `DynamicField::getFieldHTML()`, `AddField::add_field()`

---

## Points d'attention

- Gestion speciale pour le module `aCase` : le fichier PHP est cherche comme `Case.php` (ligne 52-54) — cas particulier du nommage PHP.
- Script legacy — l'interface actuelle de Studio utilise probablement un mecanisme different.
