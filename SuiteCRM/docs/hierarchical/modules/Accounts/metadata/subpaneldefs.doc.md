# Fichier : subpaneldefs.php

**Chemin :** `modules/Accounts/metadata/subpaneldefs.php`
**Type :** `PHP`
**Categorie :** configuration (sous-panneaux)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les sous-panneaux affiches dans la vue detail du module Accounts via `$layout_defs['Accounts']['subpanel_setup']`. Chaque sous-panneau represente une relation (contacts, opportunites, cases, bugs, activites, etc.).

---

## Parametres cles

| Sous-panneau | Module lie | Type de relation |
| --- | --- | --- |
| contacts | Contacts | accounts_contacts |
| opportunities | Opportunities | accounts_opportunities |
| cases | Cases | account_cases |
| bugs | Bugs | accounts_bugs |
| leads | Leads | account_leads |
| history | Emails/Notes/Calls/Meetings | activites liees |
| aos_quotes | AOS_Quotes | account_aos_quotes |
| aos_invoices | AOS_Invoices | account_aos_invoices |
| aos_contracts | AOS_Contracts | account_aos_contracts |
| members | Accounts | member_accounts (sous-comptes) |

## Impacte par / impacte

- Consomme par le framework lors du rendu de la DetailView
- Peut etre surcharge dans `custom/Extension/modules/Accounts/Ext/Layoutdefs/`
- Les layouts des sous-panneaux individuels sont dans `metadata/subpanels/`

## Points d'attention

- L'ordre des sous-panneaux dans ce fichier determine leur ordre d'affichage par defaut.
- Chaque entree peut specifier un `subpanel_name` pointant vers un fichier layout dans `metadata/subpanels/`.
