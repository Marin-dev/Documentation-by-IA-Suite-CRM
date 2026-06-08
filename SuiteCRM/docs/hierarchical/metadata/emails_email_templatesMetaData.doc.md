# emails_email_templatesMetaData.php

**Chemin :** `metadata/emails_email_templatesMetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `emails_email_templates` qui matérialise la relation entre les emails (`Emails`) et les modèles d'email (`EmailTemplates`). Permet de lier un email à un modèle depuis lequel il a été généré.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['emails_email_templates']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `emails_email_templates`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `emails_email_templates_ida` | varchar(36) | FK vers `emails.id` |
| `emails_email_templates_idb` | varchar(36) | FK vers `email_templates.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `emails_email_templatesspk` | primary | `id` |
| `emails_email_templates_ida1` | index | `emails_email_templates_ida` |
| `emails_email_templates_idb2` | index | `emails_email_templates_idb` |

### Relation

- **Type déclaré :** `true_relationship_type = one-to-one` (implémenté en many-to-many via table de jointure)
- **LHS :** module `Emails`, table `emails`, clé `id`
- **RHS :** module `EmailTemplates`, table `email_templates`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Emails
- **Appelle :** rien

## Notes

- `true_relationship_type = 'one-to-one'` mais implémenté en many-to-many : un email a été généré depuis un unique template, mais la table de jointure le permet many-to-many techniquement.
- Généré par Studio (`'from_studio' => true`).
