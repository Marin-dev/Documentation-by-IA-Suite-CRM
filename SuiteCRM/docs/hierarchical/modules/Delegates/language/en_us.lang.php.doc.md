# en_us.lang.php (Delegates)

**Chemin :** `modules/Delegates/language/en_us.lang.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role
Fichier de langue anglaise du module Delegates (Delegues). Definit les chaines d'interface pour les evenements et leurs delegues (Contacts, Leads, Prospects).

**Type :** config (langue)

---

## Dependances cles
- Aucune (fichier de donnees pur)

## Exports / Symboles principaux

Tableau `$mod_strings` avec les cles notables :

| Cle | Valeur | Usage |
|---|---|---|
| `LBL_MODULE_NAME` | `'Event'` | Nom affiché : "Event" (evenement) |
| `LBL_DEFAULT_SUBPANEL_TITLE` | `'Delegates'` | Titre du sous-panneau delegues |
| `LBL_LOCATION` | `'Location'` | Champ lieu |
| `LBL_START_DATE` | `'start date'` | Champ date de debut |
| `LBL_END_DATE` | `'End Date/Time'` | Champ date de fin |
| `LBL_BUDGET` | `'Budget'` | Champ budget |
| `LBL_INVITE_PDF` | `'Send Invites'` | Action envoi invitations |
| `LBL_EMAIL_TEMPLATE` | `'Invite Email Template'` | Template email invitation |

## Interactions
- **Appele par :** systeme de traduction SuiteCRM, vues du module Delegates
- **Appelle :** rien

## Notes
- Le module Delegates est lie aux evenements (FP_events ou similaire — INCONNU sans investigation supplementaire du module parent).
- Le libelle `LBL_MODULE_NAME = 'Event'` indique que ce module est present dans le contexte d'un module Evenements.
- Contient `LBL_ACCEPT_STATUS` et `LBL_STATUS_EVENT` impliquant un workflow de statut d'invitation.
