# field_arrays.php

**Chemin :** `modules/Contacts/field_arrays.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Fichier de définition des tableaux de champs du module Contacts. Déclare les champs de colonne (`column_fields`), les champs de liste (`list_fields`) et les champs requis (`required_fields`) utilisés par le framework SuiteCRM pour le cache et la résolution des requêtes.

**Type :** configuration

---

## Dépendances clés

Aucune — fichier de données pur.

---

## Exports / Symboles principaux

| Variable | Contenu | Rôle |
|---|---|---|
| `$fields_array['Contact']['column_fields']` | Liste de 35+ champs DB | Champs persistés en base pour un contact |
| `$fields_array['Contact']['list_fields']` | 15 champs | Champs affichés dans la vue liste |
| `$fields_array['Contact']['required_fields']` | `["last_name" => 1]` | Seul `last_name` est obligatoire |

**Champs notables dans `column_fields` :**
`portal_name`, `portal_app`, `portal_active`, `portal_password`, `campaign_id`, `invalid_email`, adresses primaire et alternative complètes.

---

## Interactions

**Appelée par :** Framework SuiteCRM lors du chargement du bean `Contact` — utilisé pour la construction des requêtes SQL et la validation des formulaires.

**Position dans le flux global :** Configuration statique chargée une fois au démarrage, mise en cache par le framework.

---

## Notes

- Le seul champ requis est `last_name` — cohérent avec la logique de `ContactFormBase::getDuplicateQuery()`.
- `invalid_email` est présent dans `column_fields` et `list_fields` — permet de filtrer les contacts avec email invalide.
