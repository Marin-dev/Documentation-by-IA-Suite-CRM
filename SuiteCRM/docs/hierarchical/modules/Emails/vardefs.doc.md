# Fichier : vardefs.php (configuration)

**Chemin :** `modules/Emails/vardefs.php`
**Configure :** Schema de la table `emails` et relations CRM
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le dictionnaire `$dictionary['Email']` : champs de la table `emails`, relations many-to-many et one-to-many avec les modules CRM, et index de base de donnees. C'est la source d'autorite pour le mapping ORM du bean Email.

## Parametres cles

| Parametre | Valeur | Effet |
|---|---|---|
| `table` | `emails` | Table principale |
| `acl_fields` | `false` | ACL non applique champ par champ |
| `fields.type` | enum `dom_email_types` | archived / draft / out / forward |
| `fields.status` | enum `dom_email_status` | unread / read / sent / send_error / draft / archived |
| `fields.mailbox_id` | id | Lie a InboundEmail |
| `fields.parent_type` / `parent_id` | varchar / id | Lien polymorphique (deprecated v4.2) |
| `fields.category_id` | enum `email_category_dom` | Categorie de l'email |
| `fields.orphaned` | bool | Email present dans SuiteCRM mais supprime du serveur IMAP |
| `fields.intent` | varchar (defaut 'pick') | Cible d'action pour assignation InboundEmail |
| Relations many-to-many | `emails_beans` (join table) | Contacts, Accounts, Leads, Opportunities, Cases, Bugs, Projects, Tasks, Users, Meetings, AOS_Contracts, Prospects |
| Relation one-to-many | `emails_notes_rel` | Notes (pieces jointes) liees a l'email via `parent_id` |
| `indices` | idx_email_name, idx_message_id, idx_email_parent_id, idx_email_assigned, idx_email_cat, idx_email_uid | Optimisation requetes |

## Impacte par / impacte

- Consomme par `VardefManager::createVardef()` avec les mixins `default`, `basic`, `assignable`, `security_groups`
- Champs `description` et `description_html` : `source=non-db` — stockes dans la table `emails_text` (INCONNU : a confirmer)
- Plusieurs champs virtualises (`indicator`, `subject`, `attachment`, `has_attachment`, `opt_in`) utilisent des fonctions d'affichage incluses depuis `modules/Emails/include/display*.php`

## Points d'attention

- La table de jointure `emails_beans` est partagee entre toutes les relations many-to-many ; le discriminant est la colonne `bean_module`.
- Le champ `parent_type`/`parent_id` est marque "deprecated as of 4.2" mais reste present.
- `description_html` est de type `emailbody` (non-db) : son stockage reel est a verifier (probablement `emails_text`).
