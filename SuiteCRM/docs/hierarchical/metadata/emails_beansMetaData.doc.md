# emails_beansMetaData.php

**Chemin :** `metadata/emails_beansMetaData.php`
**Type :** config (métadonnées de tables email — fichier multi-tables)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de **deux tables** liées aux emails :
1. `emails_beans` — table de jointure polymorphe reliant les emails à n'importe quel bean SugarCRM (Accounts, Bugs, Cases, Contacts, Leads, Opportunities, Tasks, Users, ProjectTask, Project, Prospects, Quotes)
2. `emails_text` — table de stockage des champs texte longs des emails (corps HTML/texte, raw source) séparée pour des raisons de performance

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

### Table `emails_beans`

Table de jointure polymorphe email ↔ beans.

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `email_id` | varchar(36) | FK vers `emails.id` |
| `bean_id` | varchar(36) | UUID du bean lié (polymorphe) |
| `bean_module` | varchar(100) | Module du bean (discriminant polymorphe) |
| `campaign_data` | text | Données de campagne associées |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |

**Relations définies via `relationship_role_column`** (discriminant = `bean_module`) :

| Relation | Module RHS |
|---|---|
| `emails_accounts_rel` | Accounts |
| `emails_bugs_rel` | Bugs |
| `emails_cases_rel` | Cases |
| `emails_contacts_rel` | Contacts |
| `emails_leads_rel` | Leads |
| `emails_opportunities_rel` | Opportunities |
| `emails_tasks_rel` | Tasks |
| `emails_users_rel` | Users |
| `emails_project_task_rel` | ProjectTask |
| `emails_projects_rel` | Project |
| `emails_prospects_rel` | Prospects |
| `emails_quotes` | Quotes |

### Table `emails_text`

Stockage séparé des champs longs d'un email (relation 1:1 avec `emails`).

| Colonne | Type | Rôle |
|---|---|---|
| `email_id` | id | Clé primaire + FK vers `emails.id` |
| `from_addr` | varchar(255) | Adresse expéditeur |
| `reply_to_addr` | varchar(255) | Adresse de réponse |
| `to_addrs` | text | Destinataires |
| `cc_addrs` | text | Copies carbone |
| `bcc_addrs` | text | Copies cachées |
| `description` | longtext | Corps texte brut |
| `description_html` | longhtml | Corps HTML |
| `raw_source` | longtext | Source brute complète de l'email |
| `deleted` | bool | Soft delete |

## Interactions

- **Appelé par :** framework SugarCRM, module Emails, modules de campagne
- **Appelle :** rien

## Notes

- Pattern polymorphe : une seule table `emails_beans` avec `bean_module` comme discriminant remplace 12 tables de jointure distinctes — optimisation majeure du schéma.
- `emails_text` séparée de `emails` pour des raisons de performance (champs `longtext`/`longhtml` évités lors des requêtes de liste).
- `campaign_data` dans `emails_beans` : INCONNU — probablement données de tracking des campagnes.
- Commentaire ligne 289 : `emails_text` utilise InnoDB par défaut (code MyISAM commenté pour la recherche fulltext — fonctionnalité non activée).
