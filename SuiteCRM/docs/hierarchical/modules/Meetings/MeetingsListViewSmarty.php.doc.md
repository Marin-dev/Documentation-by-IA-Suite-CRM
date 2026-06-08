# Fichier : MeetingsListViewSmarty.php

**Chemin :** `modules/Meetings/MeetingsListViewSmarty.php`
**Type :** vue (list view)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Specialisation de la vue liste pour le module Meetings. Ajoute dans le menu d'actions de la liste un lien "Carte" (jjwg_Maps) en plus du lien "Export" standard.

## Role technique
Etend `ListViewSmarty` (`include/ListView/ListViewSmarty.php`). Surcharge `buildExportLink()` pour injecter un second element `<li>` dans le dropdown des actions, pointant vers l'entryPoint `jjwg_Maps`.

---

## Dependances cles
- `ListViewSmarty` (`include/ListView/ListViewSmarty.php`) — classe parente

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `MeetingsListViewSmarty` | classe | vue liste avec lien carte |
| `buildExportLink()` | methode | HTML du lien export + lien carte |

---

## Relations cles
- **Appele par :** `MeetingsViewList::preDisplay()` (qui instancie cette classe)
- **Appelle :** `ListViewSmarty`

---

## Points d'attention
- L'injection du second `<li>` est un "hack" explicitement documente dans le code (commentaire "List item hack").
