# audit_templateMetaData.php

**Chemin :** `metadata/audit_templateMetaData.php`
**Type :** config (métadonnées de table modèle d'audit)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure du **modèle de table d'audit** (`audit`) de SuiteCRM. Ce fichier ne crée pas de table réelle ; il sert de template pour générer les tables d'audit spécifiques à chaque module (ex. `accounts_audit`, `contacts_audit`, etc.). Commentaire explicite ligne 44 : "This table should never get created, it should only be used as a template".

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['audit']` | variable globale PHP | Template de structure des tables d'audit |

### Colonnes du template `audit`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id/varchar(36) | Clé primaire UUID (requis) |
| `parent_id` | id/varchar(36) | UUID du bean parent audité (requis) |
| `date_created` | datetime | Date de création de l'entrée d'audit |
| `created_by` | varchar(36) | UUID de l'utilisateur ayant effectué la modification |
| `field_name` | varchar(100) | Nom du champ modifié |
| `data_type` | varchar(100) | Type de données du champ |
| `before_value_string` | varchar | Valeur avant modification (champs courts) |
| `after_value_string` | varchar | Valeur après modification (champs courts) |
| `before_value_text` | text | Valeur avant modification (champs longs) |
| `after_value_text` | text | Valeur après modification (champs longs) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `pk` | primary | `id` |
| `parent_id` | index | `parent_id` |

## Interactions

- **Appelé par :** framework SugarCRM (outil Repair/Rebuild, création des tables d'audit par module)
- **Appelle :** rien

## Notes

- Ce template est instancié par le framework pour chaque module auditables : le nom de la table réelle sera `{module}_audit` (ex. `accounts_audit`).
- Commentaire ligne 44 avertit explicitement que cette table ne doit jamais être créée directement.
- Le préfixe de l'index sera recalculé lors de la création réelle : `idx_` + nom de table.
- Deux paires de colonnes pour les valeurs (string vs text) permettent de gérer les champs courts et les champs longs (text) efficacement.
