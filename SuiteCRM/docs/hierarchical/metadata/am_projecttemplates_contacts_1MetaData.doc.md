# am_projecttemplates_contacts_1MetaData.php

**Chemin :** `metadata/am_projecttemplates_contacts_1MetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `am_projecttemplates_contacts_1_c` (suffixe `_c` = table custom) qui matérialise la relation many-to-many entre les modèles de projet (`AM_ProjectTemplates`) et les contacts (`Contacts`). Créé via le Studio SuiteCRM.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Généré par Studio (`'from_studio' => true`, date : 2014-06-24).

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['am_projecttemplates_contacts_1']` | variable globale PHP | Définition de la table de jointure custom |

### Structure de la table `am_projecttemplates_contacts_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `am_projecttemplates_ida` | varchar(36) | FK vers `am_projecttemplates.id` |
| `contacts_idb` | varchar(36) | FK vers `contacts.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `am_projecttemplates_contacts_1spk` | primary | `id` |
| `am_projecttemplates_contacts_1_alt` | alternate_key | `am_projecttemplates_ida`, `contacts_idb` |

### Relation

- **Type :** many-to-many
- **LHS :** module `AM_ProjectTemplates`, table `am_projecttemplates`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- Fichier généré automatiquement par le Studio SuiteCRM le 2014-06-24.
- Le suffixe `_c` sur le nom de la table indique une table custom (non core).
- Convention de nommage des colonnes de jointure : `{module_lhs}_ida` et `{module_rhs}_idb`.
