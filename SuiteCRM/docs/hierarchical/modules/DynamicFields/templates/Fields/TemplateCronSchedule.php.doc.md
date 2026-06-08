# Fichier : TemplateCronSchedule.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateCronSchedule.php`
**Type :** PHP — Template de champ (planification cron)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente un champ de planification de type cron (expression cron) personnalise. Utilise comme champ custom pour les modules necessitant une planification temporelle.

## Role technique

Classe `TemplateCronSchedule` etendant `TemplateText`. Type `CronSchedule`. Probablement tres peu de surcharge par rapport a `TemplateText`.

---

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateCronSchedule` | classe | Champ expression cron |
| `$type` | propriete | `'CronSchedule'` |

---

## Relations cles

- **Etend :** `TemplateText`
