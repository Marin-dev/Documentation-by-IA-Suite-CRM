# Fichier : Account.php

**Chemin :** `modules/Accounts/Account.php`
**Type :** `PHP`
**Categorie :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente l'entite "Compte" (organisation cliente, partenaire ou prospect). C'est le bean central du module Accounts : il stocke les donnees d'une societe (adresses, telephones, secteur, site web) et maintient les liens vers les contacts, opportunites, cas de support, bugs et campagnes associes.

## Role technique

Etend la classe `Company` (template SugarObjects) et implemente `EmailInterface`. Definit les champs persistes en base (`table_name = "accounts"`), les relations ORM (`relationship_fields`), et surcharge plusieurs methodes du framework SugarBean pour la liste, le detail, l'export et la recherche generique. Locking optimiste active.

---

## Dependances cles

| Dependance | Chemin | Role |
|---|---|---|
| `Company` | `include/SugarObjects/templates/company/Company.php` | Classe parente (adresses, champs entreprise) |
| `EmailInterface` | `include/EmailInterface.php` | Contrat pour la gestion des emails |
| `BeanFactory` | framework | Creation/recuperation de beans lies |
| `DBManagerFactory` | framework | Acces base de donnees |
| `ACLController` | framework | Controle d'acces |
| `TrackerManager` | framework | Suivi d'activite utilisateur |
| `SugarEmailAddress` | helper | Gestion des adresses email |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Account` | classe | Bean principal du module Accounts |
| `get_contacts()` | methode | Retourne les contacts lies via `get_linked_beans` |
| `clear_account_case_relationship()` | methode | Supprime le lien account-case en base (UPDATE cases) |
| `fill_in_additional_detail_fields()` | methode | Enrichit le bean avec parent_name et campaign_name |
| `get_list_view_data()` | methode | Prepare le tableau de donnees pour la vue liste |
| `build_generic_where_clause()` | methode | Construit la clause WHERE pour la recherche globale |
| `create_export_query()` | methode | Requete SQL complete pour l'export CSV avec jointures |
| `set_notification_body()` | methode | Peuple le template XTemplate pour les notifications |
| `getProductsServicesPurchasedQuery()` | methode | Requete produits/services achetes (AOS_Quotes) |
| `bean_implements()` | methode | Declare le support ACL |

**Consommateurs identifies dans le repo :**

- `modules/Accounts/AccountFormBase.php`
- `modules/Accounts/ShowDuplicates.php`
- `modules/Accounts/AccountsJjwg_MapsLogicHook.php`
- `modules/Leads/Lead.php` (requete SQL sur accounts)
- `modules/Opportunities/Opportunity.php` (get_account_detail)
- `modules/Cases/Case.php` (getAccount)

## Relations cles

- **Table SQL :** `accounts`
- **Herite de :** `Company > SugarBean`
- **Relations ORM declarees :** `opportunities`, `contacts`, `cases`, `bugs`, `tasks`, `notes`, `meetings`, `calls`, `emails`, `leads`, `documents`, `campaigns`, `aos_quotes`, `aos_invoices`, `aos_contracts`, `project`, `members` (sous-comptes)
- **Hierarchie auto-referentielle :** `member_accounts` (one-to-many sur `parent_id`)
- **Position dans le flux :** bean central appele par les vues, formulaires, logic hooks et modules lies

---

## Points d'attention

- `remove_redundant_http()` est marquee `@deprecated` et son corps est commente (ligne 202-207).
- La recuperation de `parent_name` requete la base uniquement si le champ est vide ET `id` non vide (ligne 222-238) : risque de donnee manquante si `fill_in_additional_detail_fields` n'est pas appele.
- `getProductsServicesPurchasedQuery()` retourne une chaine SQL sans l'executer : c'est au consommateur de l'executer.
- Champ `campaign_id` : appel a `get_full_list` potentiellement couteux.
- Le constructeur efface `parent_name`/`parent_id` des requetes si le parent est le module `Emails` (ligne 161-165).
