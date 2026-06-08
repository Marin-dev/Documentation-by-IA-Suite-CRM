# Case.php

**Chemin :** `modules/Cases/Case.php`
**Type :** Modele (model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit l'entite "Cas de support" du CRM. Un cas represente une demande d'assistance client avec un numero unique, une priorite, un statut et une resolution. Il est lie a un compte et peut avoir des contacts, des bugs, des taches et des activites associes.

## Role technique
Classe `aCase` (note : prefixe `a` car `Case` est un mot reserve PHP) heritant de `Basic`. Table BDD : `cases`, avec tables de relation `accounts_cases` et `contacts_cases`. Supporte le macro de sujet email `[CASE:%1]` pour l'email entrant.

---

## Dependances / Imports
| Dependance | Role |
|---|---|
| `Basic` | Classe parente (template SugarObjects) |
| `BeanFactory` | Creation de beans lies |
| `SecurityGroup` | Controle ACL par groupe (charge dynamiquement) |
| `ACLController` | Verification des droits |

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `aCase` | Classe | Bean principal du module Cases |
| `get_summary_text()` | Methode | Retourne `$this->name` |
| `listviewACLHelper()` | Methode | ACL pour le lien Account en liste |
| `save_relationship_changes()` | Methode | Lie automatiquement un contact a la creation |
| `set_case_contact_relationship()` | Methode | Ajoute un contact avec son role par defaut |
| `fill_in_additional_detail_fields()` | Methode | Enrichit avec account_name/id, assigned users |
| `get_contacts()` | Methode | Liste des contacts avec role et id de relation |
| `get_list_view_data()` | Methode | Formate priority/status/case_number en liste |
| `build_generic_where_clause()` | Methode | WHERE pour recherche par nom, compte, case_number |
| `set_notification_body()` | Methode | Remplit le template email de notification |
| `bean_implements()` | Methode | Retourne `true` pour l'interface `ACL` |
| `getEmailSubjectMacro()` | Methode | Retourne le macro `[CASE:%1]` (ou config) |
| `getAccount()` | Methode | Retourne nom et id du compte lie par SQL |

## Consommateurs identifies
- `modules/Accounts/AccountsJjwg_MapsLogicHook.php` (propagation geocodage)

---

## Relations cles
- **Table BDD :** `cases`
- **Tables de relation :** `accounts_cases`, `contacts_cases`
- **Champs cles :** `case_number` (auto-increment), `status`, `priority`, `state`, `emailSubjectMacro`
- **Option config :** `$sugar_config['require_accounts']` — si false, `account_name` n'est plus obligatoire
- **Option config :** `$sugar_config['inbound_email_case_subject_macro']` — surcharge le macro email

---

## Points d'attention
- Le nom de la classe est `aCase` et non `Case` pour eviter le conflit avec le mot-cle PHP `case`.
- `getEmailSubjectMacro()` permet a l'email entrant de parser automatiquement le numero de cas depuis le sujet.
- `getAccount()` effectue une jointure directe `cases.account_id -> accounts.id` (pas via la table de relation `accounts_cases`) — potentielle incoherence si la relation est gere uniquement via la table de jonction.
- `set_case_contact_relationship()` utilise `case_relationship_type_default_key` depuis `$app_list_strings`.
