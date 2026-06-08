# Fichier : vardefs.php (configuration)

**Chemin :** `modules/AM_ProjectTemplates/vardefs.php`
**Configure :** Schema du bean `AM_ProjectTemplates` / table SQL `am_projecttemplates`
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definition du schema `$dictionary['AM_ProjectTemplates']` pour la table `am_projecttemplates`. Genere par Module Builder. Declare les champs du modele de projet, ses relations avec les utilisateurs, contacts et taches modeles.

---

## Parametres cles

| Parametre | Valeur / Type | Effet |
| --- | --- | --- |
| `table` | `am_projecttemplates` | Table SQL principale |
| `audited` | `true` | Audit des modifications actif |
| `name` | varchar(255), required | Nom du template |
| `status` | enum, default `Draft` | Statut du template (Draft, Active, Inactive) |
| `override_business_hours` | bool | Si true, ignore les heures ouvrables AOBH pour le calcul des dates |
| `description` | text | Description du template |

---

## Relations declarees

| Relation | Type | Description |
| --- | --- | --- |
| `am_projecttemplates_users_1` | many-to-many (custom) | Ressources utilisateurs du template |
| `am_projecttemplates_contacts_1` | many-to-many (custom) | Ressources contacts du template |
| `am_tasktemplates_am_projecttemplates` | many-to-many | Taches modeles liees au template |
| `am_projecttemplates_project_1` | many-to-many | Projets issus de ce template |

---

## Impacte par / impacte

- Lu par `Project::save()` lors de l'application d'un template (champ `override_business_hours`, ligne 491)
- Relations utilisees dans `AM_ProjectTemplates::save()` pour la synchronisation des ressources

---

## Points d'attention

- Fichier genere par Module Builder — ne pas modifier directement (les surcharges vont dans `custom/Extension/modules/`).
- `override_business_hours` est un champ cle pour le calcul des dates — sa valeur impacte directement `Project::save()`.
