# AOR_Scheduled_Reports.php

**Chemin :** `modules/AOR_Scheduled_Reports/AOR_Scheduled_Reports.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele de planification d'envoi automatique de rapports AOR par email. Permet de configurer un calendrier cron et une liste de destinataires pour envoyer periodiquement les resultats d'un rapport par email.

## Role technique
Etend `Basic`. Utilise la bibliotheque `Cron\CronExpression` (bundlee dans `lib/Cron/`) pour parser et evaluer les expressions cron. La methode `shouldRun` determine si le rapport doit etre execute a la date courante en comparant la date de dernier run avec la prochaine occurrence cron.

---

## Attributs principaux
| Attribut | Role |
|---|---|
| `aor_report_id` | FK vers le rapport AOR associe |
| `schedule` | Expression cron (ex: `0 8 * * 1` = lundi 8h) |
| `email_recipients` | Destinataires serialises en base64 (types: Email Address, Specify User, Users) |
| `status` | Statut du planificateur (Active/Inactive) |
| `last_run` | Date du dernier envoi |

## Methodes principales
| Methode | Role |
|---|---|
| `shouldRun(DateTime $date)` | Verifie si le rapport doit etre execute a la date donnee |
| `get_email_recipients()` | Retourne la liste des emails des destinataires (resout groupes securite, roles, tous) |
| `parseRecipients()` | Parse les destinataires depuis le POST et stocke en base64 |
| `handleTimeZone(DateTime $date)` | Ajuste la date selon le fuseau horaire de la config |

## Relations cles
- **Appele par :** Scheduler SuiteCRM (INCONNU — le job cron appelant n'est pas dans ce module)
- **Appelle :** `Cron\CronExpression`, `SecurityGroup`, `ACLRole`, `BeanFactory`
- **Table DB :** `aor_scheduled_reports`
- **Relation parent :** `aor_report_id` vers `aor_reports`

---

## Points d'attention
- Les destinataires de type `Users` peuvent etre filtres par groupe securite ET role simultanement (intersection).
- La gestion de timezone dans `handleTimeZone` utilise l'offset en secondes applique via `modify()` — attention aux transitions DST.
- Si `last_run` est vide, la date de creation (`date_entered`) est utilisee comme reference.
- `email_recipients` est stocke en `base64(serialize(array))` — doit etre deserialise avec `['allowed_classes' => false]`.
