# Fichier AOR_Scheduled_Reports.php

**Chemin :** `modules/AOR_Scheduled_Reports/AOR_Scheduled_Reports.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle des rapports planifiés. Permet d'associer un rapport AOR à une expression cron et une liste de destinataires email. Le scheduler SuiteCRM appelle ce bean pour déterminer si un rapport doit être envoyé et résoudre la liste des destinataires (adresses directes, utilisateurs spécifiques, groupes de sécurité, rôles, tous les utilisateurs actifs).

## Type
model

---

## Dépendances clés
- `basic` (classe parente)
- `modules/AOR_Scheduled_Reports/lib/Cron/includeCron.php` — bibliothèque Cron\CronExpression
- `BeanFactory` — récupération Users, SecurityGroups, ACLRoles
- `modules/SecurityGroups/SecurityGroup.php` — groupes de sécurité (optionnel)
- `modules/ACLRoles/ACLRole.php` — rôles ACL
- `$sugar_config['default_timezone']` — fuseau horaire pour le calcul de planification

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_Scheduled_Reports` | classe | Bean rapport planifié |
| `save()` | méthode | Sauvegarde après parsing des destinataires |
| `get_email_recipients()` | méthode | Résout la liste des adresses email selon les règles de ciblage |
| `shouldRun()` | méthode | Teste si le rapport doit s'exécuter à la date donnée (expression cron) |
| `handleTimeZone()` | méthode (protected) | Ajuste une DateTime selon le fuseau horaire configuré |
| `parseRecipients()` | méthode (protected) | Extrait et sérialise les destinataires depuis POST |

### Champs importants
| Champ | Rôle |
|---|---|
| `schedule` | Expression cron (ex: `0 8 * * 1`) |
| `email_recipients` | Destinataires sérialisés en base64 |
| `status` | Statut du rapport planifié |
| `last_run` | Date de dernière exécution |
| `aor_report_id` | Lien vers le rapport AOR associé |

## Interactions
- **Appelé par :** Scheduler SuiteCRM (cron.php), module AOR_Reports (sous-panel)
- **Appelle :** `Cron\CronExpression`, `BeanFactory::newBean('Users')`, `SecurityGroups`, `ACLRoles`
- **Table BD :** `aor_scheduled_reports`

## Notes
- `email_recipients` est stocké comme `base64_encode(serialize($array))` contenant les clés `email_target_type` et `email`.
- `shouldRun()` compare `getNextRunDate($lastRun)` avec la date courante — si `last_run` est vide, vérifie `isDue()`.
- La résolution des destinataires de type "Users" supporte : `security_group` (avec filtre rôle optionnel), `role`, `all`.
- Le parsing POST dans `parseRecipients()` supprime `$_POST['email_recipients']` pour éviter la double sauvegarde par le framework.
