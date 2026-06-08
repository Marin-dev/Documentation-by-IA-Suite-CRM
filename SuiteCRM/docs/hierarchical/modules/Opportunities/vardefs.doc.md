# Fichier : vardefs.php

**Chemin :** `modules/Opportunities/vardefs.php`
**Type :** `PHP`
**Categorie :** configuration (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le schema du bean `Opportunity` via `$dictionary['Opportunity']`. Declare les champs (amount, currency_id, date_closed, sales_stage, probability, lead_source, etc.), les liens ORM et les relations.

---

## Parametres cles

| Parametre | Valeur | Effet |
| --- | --- | --- |
| `table` | `opportunities` | Table SQL principale |
| `audited` | `true` | Audit des modifications |
| `amount` | currency | Montant de l'opportunite |
| `amount_usdollar` | currency | Equivalent en USD (calcule par SaveOverload) |
| `currency_id` | id | Devise selectionnee |
| `date_closed` | date | Date de cloture prevue |
| `sales_stage` | enum (`sales_stage_dom`) | Etape de vente |
| `probability` | decimal | Probabilite de closing (%) |
| `lead_source` | enum (`lead_source_dom`) | Source du lead |

## Relations declarees

| Relation | Type | Modules lies |
| --- | --- | --- |
| `accounts_opportunities` | M:M | Accounts |
| `opportunities_contacts` | M:M | Contacts |
| `opportunities_tasks` | one-to-many | Tasks |
| `opportunities_notes` | one-to-many | Notes |
| `opportunities_meetings` | one-to-many | Meetings |
| `opportunities_calls` | one-to-many | Calls |

## Points d'attention

- `amount_usdollar` est calcule automatiquement, ne pas modifier manuellement.
- `sales_probability_dom` definit la probabilite par defaut pour chaque etape de vente.
