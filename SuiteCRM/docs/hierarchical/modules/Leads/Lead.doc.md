# Fichier : Lead.php

**Chemin :** `modules/Leads/Lead.php`
**Type :** `PHP`
**Categorie :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente l'entite "Prospect" (Lead) du CRM : une personne d'interet en debut de cycle de vente, pas encore convertie en contact/compte. Gere le cycle de vie du lead de la creation a la conversion, avec les liens vers le compte, l'opportunite et le contact d'origine.

## Role technique

Classe `Lead` etendant `Person` (template SugarObjects) et implementant `EmailInterface`. Table SQL `leads`. Fournit des methodes de requete pour les entites liees, la construction de listes, la gestion de la conversion, et la verification ACL enrichie (securite par groupe).

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `Person` | `include/SugarObjects/templates/person/Person.php` | Classe parente (champs personne) |
| `EmailInterface` | `include/EmailInterface.php` | Contrat emails |
| `BeanFactory` | framework | Creation/recuperation de beans |
| `DBManagerFactory` | framework | Acces base de donnees |
| `SecurityGroup` | `modules/SecurityGroups/SecurityGroup.php` | Securite par groupe (charge dynamiquement) |
| `LoggerManager` | framework | Journalisation |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `Lead` | classe | Bean principal du module Leads |
| `get_account()` | methode | Hydrate `account_name` depuis la BDD via `account_id` |
| `get_opportunity()` | methode | Hydrate `opportunity_name` |
| `get_contact()` | methode | Hydrate `contact_name` (apres conversion) |
| `converted_lead()` | methode | Marque le lead converti (UPDATE SQL + status='Converted') |
| `fill_in_additional_detail_fields()` | methode | Enrichit avec account, contact, opportunity, campaign |
| `get_list_view_data()` | methode | Prepare les donnees pour la vue liste |
| `build_generic_where_clause()` | methode | Clause WHERE pour la recherche globale |
| `convertCustomFieldsForm()` | methode | Propage les champs custom lors de la conversion |
| `listviewACLHelper()` | methode | Gere les liens ACL pour account/opportunity/contact en liste |
| `getActivitiesOptions()` | methode statique | Retourne les options de conversion d'activites |
| `save()` | methode | Force `status = 'New'` si non defini |

**Consommateurs identifies dans le repo :**

- `modules/Leads/LeadFormBase.php`
- `modules/Leads/views/view.convertlead.php`
- `modules/Leads/Save.php` (via LeadFormBase)

## Relations cles

- **Table SQL :** `leads`
- **Herite de :** `Person > SugarBean`
- **Champs de relation :** `contact_id`, `account_id`, `opportunity_id`, `task_id`, `note_id`, `meeting_id`, `call_id`, `email_id`
- **Lien post-conversion :** `contact_id`, `account_id`, `opportunity_id` (remplis par `converted_lead()`)
- **Position dans le flux :** entite en debut de pipeline commercial, convertie en Contact+Account+Opportunity via ConvertLead

---

## Points d'attention

- `converted_lead()` execute un UPDATE SQL direct puis recharge le bean pour setter `status='Converted'` et declencher les workflows (ligne 277-287).
- `get_linked_fields()` exclut `oldmeetings` et `oldcalls` (correction bug 27339, legacy pre-5.1).
- `listviewACLHelper()` a un fallback : si `account_name_owner` absent, charge le bean Account entier pour obtenir `assigned_user_id`.
- Double `require_once` de `Person.php` dans le fichier (lignes 46 et 55) : redondance inoffensive.
- `save()` garantit le statut minimum `'New'` : important pour les imports en masse.
