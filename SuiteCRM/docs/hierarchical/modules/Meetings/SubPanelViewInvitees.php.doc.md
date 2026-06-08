# Fichier : SubPanelViewInvitees.php

**Chemin :** `modules/Meetings/SubPanelViewInvitees.php`
**Type :** vue (sous-panneau)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Affiche le sous-panneau des invites (users et contacts) d'une reunion dans la vue detail. Presente deux tableaux : un pour les utilisateurs, un pour les contacts, avec leurs coordonnees.

## Role technique
Script PHP qui utilise `XTemplate` (`modules/Meetings/SubPanelViewInvitees.html`) pour le rendu. Parcourt `$focus_users_list` et `$focus_contacts_list` (variables globales alimentees en amont). Genere des boutons HTML pour selectionner des contacts ou des utilisateurs via popup.

---

## Dependances cles
- `XTemplate` — moteur de template HTML
- `$focus_users_list`, `$focus_contacts_list` — listes d'objets passees en globales
- `$locale->getLocaleFormattedName()` — formatage nom localise

## Exports / Symboles principaux
Aucun. Rendu direct via `XTemplate::out()`.

---

## Relations cles
- **Appele par :** framework de sous-panneaux SuiteCRM sur la DetailView Meeting
- **Appelle :** `XTemplate`

---

## Points d'attention
- Depend de variables globales `$focus_users_list` et `$focus_contacts_list` injectees par le framework — leur alimentation est INCONNU dans ce fichier.
