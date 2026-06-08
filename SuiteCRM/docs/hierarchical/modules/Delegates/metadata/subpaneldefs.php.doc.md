# subpaneldefs.php (Delegates)

**Chemin :** `modules/Delegates/metadata/subpaneldefs.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Definit le sous-panneau par defaut du module Delegates. Ce sous-panneau affiche les participants (Contacts, Leads, Prospects) d'un evenement avec leur statut et statut d'acceptation.

**Type :** config (metadata sous-panneau)

---

## Dependances cles
- Aucune (fichier de configuration pur)

## Exports / Symboles principaux

Variable `$layout_defs['Delegates']` :

| Element | Detail | Role |
|---|---|---|
| `top_buttons` | `SubPanelTopArchiveEmailButton`, `SubPanelTopSummaryButton` | Boutons du sous-panneau |
| `list_fields.Contacts` | `name`, `account_name`, `phone_work`, `email1`, `event_status_name`, `event_accept_status` | Colonnes Contacts |
| `list_fields.Leads` | Idem + icone module Emails | Colonnes Leads |
| `list_fields.Prospects` | `name`, `account_name`, `phone_work`, `email1`, `event_status_name`, `event_accept_status` | Colonnes Prospects |

## Interactions
- **Appele par :** systeme de sous-panneaux SuiteCRM dans les modules parents affichant des delegues
- **Reference :** modules Contacts, Leads, Prospects, Accounts, Emails

## Notes
- Trois types de participants sont geres : Contacts, Leads, Prospects.
- Les colonnes `event_status_name` et `event_accept_status` sont specifiques aux evenements — non standard dans SuiteCRM de base.
- TODO (commentaire ligne 13) : merge avec le sous-panneau activities prevu mais non realise.
- `order_by` de Leads reference `date_modified` mais `order_by` de Contacts reference `date_entered.date_modified` — potentielle erreur de configuration.
