# Fichier : Reschedule_popup.php

**Chemin :** `modules/Calls_Reschedule/Reschedule_popup.php`
**Type :** PHP - Vue (popup de replanification)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la fenetre popup de replanification d'un appel. Presente un formulaire avec les champs date, heure et raison de la replanification. Adapte l'affichage au format date/heure de l'utilisateur courant.

## Role technique

Script PHP qui lit `$_GET['call_id']`, recupere le bean `Call`, extrait et reformate la date/heure de debut selon le format `timef` de l'utilisateur (H:i, H.i, h:ia, h.ia, h:i via un `switch`). Construit le formulaire HTML soumettant vers `modules/Calls/Reschedule.php`. Le champ raison est alimente par `$app_list_strings['call_reschedule_dom']`.

---

## Dependances principales

| Import / Classe | Role |
| --- | --- |
| `Calls_Reschedule` | Inclus pour l'historique |
| `Call` | Bean appel recupere par ID |
| `$locale` (global) | Formatage du nom utilisateur |
| `$app_list_strings` (global) | Dropdown des raisons (`call_reschedule_dom`) |

---

## Exports / Symboles principaux

Aucun. Script de rendu HTML direct (echo implicite).

---

## Relations cles

- **Appele par :** Lien "Replanifier" dans la vue liste des Calls (via popup JavaScript)
- **Soumet vers :** `modules/Calls/Reschedule.php` (POST)
- **Position dans le flux :** Vue intermediaire entre le clic utilisateur et l'action `Reschedule`

---

## Points d'attention

- Gere 5 formats d'heure distincts via un `switch` — fragile si nouveau format ajoute.
- Utilise `$_GET['call_id']` directement — protection IDOR a verifier au niveau du routeur.
- La liste des raisons `call_reschedule_dom` est configurable via l'admin Dropdowns Editor.
