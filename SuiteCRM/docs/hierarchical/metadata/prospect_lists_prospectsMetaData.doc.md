# prospect_lists_prospectsMetaData.php

**Chemin :** `metadata/prospect_lists_prospectsMetaData.php`
**Type :** config (métadonnées de table de jointure polymorphe campagnes)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `prospect_lists_prospects` qui matérialise la relation polymorphe entre les listes de prospects (`ProspectLists`) et plusieurs types d'entités (Contacts, Prospects, Leads, Users, Accounts). Une seule table couvre 5 types de destinataires potentiels d'une campagne.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['prospect_lists_prospects']` | variable globale PHP | Définition de la table de jointure polymorphe |

### Structure de la table `prospect_lists_prospects`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `prospect_list_id` | varchar(36) | FK vers `prospect_lists.id` |
| `related_id` | varchar(36) | UUID de l'entité liée (polymorphe) |
| `related_type` | varchar(25) | Type de l'entité : Prospect, Contact, Lead, User (commentaire source ligne 68) |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relations définies (discriminant = `related_type`)

| Relation | Module RHS | Valeur `related_type` |
|---|---|---|
| `prospect_list_contacts` | `Contacts` | `Contacts` |
| `prospect_list_prospects` | `Prospects` | `Prospects` |
| `prospect_list_leads` | `Leads` | `Leads` |
| `prospect_list_users` | `Users` | `Users` |
| `prospect_list_accounts` | `Accounts` | `Accounts` |

## Interactions

- **Appelé par :** module Campaigns, module ProspectLists
- **Appelle :** rien

## Notes

- Table polymorphe clé du système de campagnes : une liste de prospects peut contenir des contacts, prospects, leads, utilisateurs ou comptes.
- Commentaire source ligne 68 : "valid values are Prospect, Contact, Lead, User" — `Accounts` n'est pas listé mais est bien défini dans les relations.
