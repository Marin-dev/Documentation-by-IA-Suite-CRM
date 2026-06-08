# Fichier : field_arrays.php

**Chemin :** `modules/Accounts/field_arrays.php`
**Type :** `PHP`
**Categorie :** configuration (tableau de champs cache)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit `$fields_array['Account']` : les tableaux de champs utilises pour le cache du module Accounts. Contient `column_fields` (champs persistes en base), `list_fields` (champs affiches dans la vue liste) et `required_fields` (champs obligatoires).

---

## Parametres cles

| Parametre | Contenu |
| --- | --- |
| `column_fields` | 33 champs : annual_revenue, billing_address_*, description, email1/2, employees, id, industry, name, ownership, parent_id, phone_*, rating, shipping_address_*, sic_code, ticker_symbol, account_type, website, created_by |
| `list_fields` | id, name, website, phone_office, assigned_user_name/id, billing_address_*, shipping_address_* |
| `required_fields` | `name => 1` (seul champ requis) |

## Impacte par / impacte

- Consomme par le framework SugarBean pour le cache des champs lors de la lecture/ecriture en base
- Les `vardefs.php` restent la source de verite pour le schema

## Points d'attention

- Fichier vestige de l'ancien systeme de cache pre-Vardefs. Avec `new_schema = true`, les vardefs font autorite. Ce fichier reste charge pour compatibilite descendante.
- Ne pas editer manuellement : toute modification du schema doit se faire dans `vardefs.php`.
