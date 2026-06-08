# Fichier : vardefs.php

**Chemin :** `modules/FP_events/vardefs.php`
**Type :** PHP — configuration (vardefs SugarCRM)
**Derniere mise a jour doc :** 2026-06-02

---

## Ce que ce fichier configure
Definit le schema de la table `fp_events` pour le framework SugarCRM. Champs specifiques : `duration_hours`, `duration_minutes`, `date_start`, `date_end`, `location`, `budget`, `currency_id`, `invite_templates`, `accept_redirect`, `decline_redirect`. Definit aussi les relations avec Contacts, Leads et FP_Event_Locations.

## Parametres cles
| Champ | Type | Effet |
|---|---|---|
| `duration_hours` | int, required | Duree en heures |
| `duration_minutes` | int | Duree en minutes |
| `date_start` / `date_end` | datetime | Plage de l'evenement |
| `location` | varchar | Lieu textuel |
| `budget` | currency | Budget alloue |
| `invite_templates` | relate | Template d'email d'invitation |
| `accept_redirect` / `decline_redirect` | varchar | URL de redirection apres reponse |

## Impacte par / impacte
- Consomme par `FP_events.php`, BeanFactory
- Relations definies vers Contacts, Leads, FP_Event_Locations (via `fp_event_locations_fp_events_1`)

## Points d'attention
- Table auditee (`audited: true`).
- La relation avec FP_Event_Locations est de type `link` (relation N-N via table de liaison).
