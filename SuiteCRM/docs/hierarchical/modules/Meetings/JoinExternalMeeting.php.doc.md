# Fichier : JoinExternalMeeting.php

**Chemin :** `modules/Meetings/JoinExternalMeeting.php`
**Type :** controller (point d'entree action)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Gere l'acces a une reunion externe (WebEx ou autre). Verifie si l'utilisateur courant est invite ou hote avant de le rediriger vers l'URL de rejoindre (`join_url`) ou de demarrer (`host_url`) la reunion. Affiche un message d'erreur via Smarty si l'acces est refuse.

## Role technique
Script de 50 lignes. Lit `$_REQUEST['meeting_id']` et `$_REQUEST['host_meeting']`. Interroge `meetings_users` pour verifier l'invitation. Si hote : verifie `assigned_user_id == current_user`. Redirige via `SugarApplication::redirect()`. Si refus : affiche un template Smarty (`tpls/extMeetingNoStart.tpl` ou `extMeetingNotInvited.tpl`, surchargeable dans `custom/`).

---

## Dependances cles
- `DBManagerFactory` — requete SQL directe sur `meetings_users`
- `loadBean('Meetings')` — recuperation de la reunion
- `Sugar_Smarty` — rendu template d'erreur
- Templates : `modules/Meetings/tpls/extMeetingNoStart.tpl`, `extMeetingNotInvited.tpl`

## Exports / Symboles principaux
Aucun. Script d'execution directe.

---

## Relations cles
- **Appele par :** lien "Rejoindre la reunion" dans les vues Meetings (URL `?module=Meetings&action=JoinExternalMeeting`)
- **Appelle :** `SugarApplication::redirect()`, `Sugar_Smarty`

---

## Points d'attention
- Les templates Smarty sont surchargeable dans `custom/modules/Meetings/tpls/`.
- Seuls l'assignee ou un admin peuvent demarrer (`host_meeting=1`) ; tout invite peut rejoindre.
