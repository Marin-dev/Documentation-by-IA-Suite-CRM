# Fichier : subpaneldefs.php

**Chemin :** `modules/CalendarAccount/metadata/subpaneldefs.php`
**Type :** PHP — configuration (sous-panneaux)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit les sous-panneaux disponibles dans la vue detail de CalendarAccount :
- **Meetings** (ordre 10) : reunions liees via `calendar_account_meetings`, triees par `date_start` desc
- **SecurityGroups** (ordre 900) : groupes de securite associes

## Parametres cles
| Sous-panneau | Module | Relation | Ordre |
|---|---|---|---|
| meetings | Meetings | `calendar_account_meetings` | 10 |
| securitygroups | SecurityGroups | `SecurityGroups` | 900 |

## Impacte par / impacte
- Consomme par le framework SugarCRM pour la vue detail CalendarAccount
- La relation `calendar_account_meetings` doit etre definie dans les vardefs

## Points d'attention
- Le sous-panneau Meetings n'a pas de boutons d'action (`top_buttons: []`) — lecture seule.
