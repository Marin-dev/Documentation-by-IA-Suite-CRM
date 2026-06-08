# 📁 AOR_Scheduled_Reports

**Chemin :** `modules/AOR_Scheduled_Reports/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOR_Scheduled_Reports gère l'envoi automatique de rapports AOR par email selon un planning cron. Il permet de configurer des destinataires (adresses directes, utilisateurs, rôles, groupes de sécurité) et une fréquence d'envoi pour recevoir les résultats de rapports sans intervention manuelle.

## ⚙️ Responsabilité technique
Bean `AOR_Scheduled_Reports` (hérite de `Basic`). Utilise la librairie tierce `Cron\CronExpression` (bundlée dans `lib/Cron/`) pour évaluer les expressions cron. `shouldRun()` compare la dernière exécution avec la prochaine occurrence. Les destinataires sont stockés en `base64(serialize(...))`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |
| `lib/` | Librairie Cron pour parsing d'expressions cron | [→ CONTEXT](lib/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOR_Scheduled_Reports.php` | Bean planificateur d'envoi de rapports | [→ fiche](AOR_Scheduled_Reports.doc.md) |
| `emailRecipients.php` | Helper pour la sélection des destinataires | [→ fiche](emailRecipients.doc.md) |
| `vardefs.php` | Schéma de la table `aor_scheduled_reports` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOR_Report` (exécution du rapport), `Cron\CronExpression`, `SecurityGroup`, `ACLRole`, `BeanFactory`
- **Consommé par :** Scheduler SuiteCRM (job cron - chemin exact INCONNU)
- **Flux typique :** Scheduler → `shouldRun(now)` → oui → `get_email_recipients()` → `AOR_Report::build_report_*()` → envoi email

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique de planification | [`AOR_Scheduled_Reports.php`](AOR_Scheduled_Reports.doc.md) |
| Voir la gestion des destinataires | [`emailRecipients.php`](emailRecipients.doc.md) |
| Explorer la librairie cron | [`lib/Cron/CronExpression.php`](lib/Cron/CronExpression.php.doc.md) |

---

## ⚠️ Zones INCONNU
- Job cron appelant ce module non identifié (dans `Schedulers/`)
- Gestion des transitions DST dans `handleTimeZone()` — risque à l'heure du changement
