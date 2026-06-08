# Fichier : Opportunity.php

**Chemin :** `modules/Opportunities/Opportunity.php`
**Type :** `PHP`
**Categorie :** model
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Represente l'entite "Opportunite" du CRM : une transaction commerciale potentielle avec une organisation cliente. Stocke le montant, la date de cloture prevue, l'etape de vente et la probabilite. Pivot entre les comptes, contacts et activites commerciales.

## Role technique

Classe `Opportunity` etendant `SugarBean`. Table SQL `opportunities`, table de relation `accounts_opportunities` (M:M). Gere la conversion des montants en USD (via `SaveOverload.php`), le lien compte via `accounts_opportunities`, la gestion de la devise, et le lien contact avec role.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `SugarBean` | framework | Classe parente |
| `BeanFactory` | framework | Creation/recuperation de beans |
| `DBManagerFactory` | framework | Acces base de donnees |
| `SecurityGroup` | `modules/SecurityGroups/SecurityGroup.php` | Securite par groupe |
| `SaveOverload.php` | `modules/Opportunities/SaveOverload.php` | Calcul conversion montant en USD |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `Opportunity` | classe | Bean principal du module Opportunities |
| `get_contacts()` | methode | Retourne les contacts lies avec leur role |
| `get_account_detail($opp_id)` | methode statique | Recupere le compte lie (via accounts_opportunities) |
| `update_currency_id($fromid, $toid)` | methode | Met a jour la devise pour opportunites non closes |
| `fill_in_additional_detail_fields()` | methode | Enrichit avec account_name, campaign_name, devise |
| `build_generic_where_clause()` | methode | Clause WHERE pour la recherche globale |
| `save($check_notify)` | methode | Force devise, calcule probabilite, convertit montant |
| `save_relationship_changes($is_update, $exclude)` | methode | Gere le changement de compte lie et role contact |
| `set_opportunity_contact_relationship($contact_id)` | methode | Cree le lien contact avec role par defaut |
| `set_notification_body($xtpl, $oppty)` | methode | Peuple le template de notification |
| `getCurrencyType()` | fonction globale | Fonction vide (vestige de code) |

**Consommateurs identifies dans le repo :**

- `modules/Opportunities/Save.php`
- `modules/Opportunities/OpportunityFormBase.php`
- `modules/Accounts/AccountsJjwg_MapsLogicHook.php`
- `modules/Leads/Lead.php` (get_opportunity)

## Relations cles

- **Table SQL :** `opportunities`
- **Tables de relation :** `accounts_opportunities` (M:M), `opportunities_contacts` (M:M)
- **Herite de :** `SugarBean`
- **Champs cles :** `amount`, `amount_usdollar`, `currency_id`, `date_closed`, `sales_stage`, `probability`

---

## Points d'attention

- `save()` appelle `perform_save()` de `SaveOverload.php` AVANT `parent::save()` pour calculer `amount_usdollar`.
- La probabilite est calculee automatiquement depuis `sales_probability_dom` si non deja definie.
- `save_relationship_changes()` exclut `currency_id` (corrections bugs 38529 et 40938).
- `update_currency_id()` n'affecte que les opportunites avec `sales_stage` different de `Closed Won`/`Closed Lost`.
- `getCurrencyType()` est une fonction vide hors classe (ligne 480) : vestige non supprime.
- Si `$sugar_config['require_accounts']` est false, `account_name` n'est pas requis.
