# Fichier : vardefs.php

**Chemin :** `modules/Leads/vardefs.php`
**Type :** `PHP`
**Categorie :** configuration (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le schema du bean `Lead` via `$dictionary['Lead']`. Declare les champs specifiques aux leads (converted, refered_by, lead_source, status, account_name, etc.), les liens ORM, et invoque `VardefManager::createVardef()`.

---

## Parametres cles

| Parametre | Valeur | Effet |
| --- | --- | --- |
| `table` | `leads` | Nom de la table SQL |
| `audited` | `true` | Audit des modifications active |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `full_text_search` | `true` | Indexation full-text |
| `duplicate_merge` | `true` | Fusion de doublons activee |
| `converted` | bool, default `0` | Indicateur de conversion en Contact/Account/Opp |
| `lead_source` | enum (`lead_source_dom`) | Source du lead (Web, email, etc.) |
| `status` | enum (`lead_status_dom`) | Statut : New, Assigned, In Process, Converted... |
| `refered_by` | varchar(100) | Nom du referent |

## Impacte par / impacte

- Consomme par `VardefManager` au demarrage
- Utilise par `Lead.php` via `$this->field_defs`
- Surcharge possible dans `custom/Extension/modules/Leads/Ext/Vardefs/`

## Points d'attention

- Le champ `converted` est central : il conditionne l'exclusion des leads de la recherche de doublons et le filtrage dans les vues.
- Les relations `calls`, `meetings` anciens (pre-5.1) sont gerees separement via `get_old_related_calls()` / `get_old_related_meetings()` dans `Lead.php`.
