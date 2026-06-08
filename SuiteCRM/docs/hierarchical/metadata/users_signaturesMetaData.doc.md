# users_signaturesMetaData.php

**Chemin :** `metadata/users_signaturesMetaData.php`
**Type :** config (metadonnees de table)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table `users_signatures` qui stocke les signatures email des utilisateurs. Chaque utilisateur peut avoir plusieurs signatures (texte brut et HTML) utilisees lors de la redaction d'emails depuis SuiteCRM.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['UserSignature']` | variable globale PHP | Definition de la table des signatures utilisateur |

### Structure de la table `users_signatures`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | id (requis) | Cle primaire UUID |
| `date_entered` | datetime | Date de creation (requis) |
| `date_modified` | datetime | Date de modification (requis) |
| `deleted` | bool | Soft delete (nullable) |
| `user_id` | varchar(36) | FK vers `users.id` |
| `name` | varchar(255) | Nom/label de la signature |
| `signature` | text | Corps de la signature en texte brut |
| `signature_html` | text | Corps de la signature en HTML |

### Index

| Nom | Type | Champs |
|---|---|---|
| `users_signaturespk` | primary | `id` |
| `idx_usersig_uid` | index | `user_id` |

### Relation

- Pas de bloc `relationships` explicite dans ce fichier.
- Relation implicite one-to-many : un utilisateur peut avoir plusieurs signatures.

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema), module Users, module Emails
- **Appelle :** rien

## Notes

- Protege par la constante `sugarEntry`.
- Le champ `signature_html` permet des signatures riches (images, mise en forme). La valeur non-reportable indique que ces champs n'apparaissent pas dans les rapports.
- Le commentaire en tete du fichier indique explicitement : "TABLE DEFINITION FOR EMAIL STUFF".
