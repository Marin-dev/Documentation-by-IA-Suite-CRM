# subpaneldefs.php (History)

**Chemin :** `modules/History/metadata/subpaneldefs.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit le sous-panneau par defaut du module History. Ce sous-panneau affiche l'historique des activites terminees (reunions terminees/annulees, emails envoyes, notes, taches terminees/differees, appels tenus/non tenus) dans les modules CRM.

**Type :** config (metadata sous-panneau)

---

## Dependances cles
- Aucune (fichier de configuration pur)

## Exports / Symboles principaux

Variable `$layout_defs['History']` — sous-panneau par defaut avec 5 types d'activites :

| Type | Filtre WHERE | Colonnes principales |
|---|---|---|
| `Meetings` | `status='Held' OR status='Not Held'` | subject, status, contact, related_to, date_modified |
| `Emails` | `status='sent'` | subject, status, category, contact, related_to, date_modified |
| `Notes` | (aucun filtre) | subject, status, contact, related_to, date_modified |
| `Tasks` | `status='Completed' OR status='Deferred'` | subject, status, contact, related_to, date_modified |
| `Calls` | `status='Held' OR status='Not Held'` | subject, status, contact, related_to, date_modified |

Boutons en haut : `SubPanelTopCreateNoteButton`, `SubPanelTopArchiveEmailButton`, `SubPanelTopSummaryButton`

## Interactions
- **Appele par :** tous les modules SuiteCRM qui incluent un sous-panneau History (Accounts, Contacts, Leads, Opportunities, etc.)
- **Reference :** modules Meetings, Emails, Notes, Tasks, Calls, Contacts

## Notes
- TODO (commentaire ligne 57) : fusion avec le sous-panneau Activities prevue mais non realisee.
- Chaque type d'activite a son propre `order_by` : principalement `date_modified` sauf Tasks qui utilise `date_start`.
- Les colonnes `edit_button` et `remove_button` sont presentes pour chaque type d'activite.
- Ce fichier est fondamental : il est consume par pratiquement tous les modules relationnels de SuiteCRM.
