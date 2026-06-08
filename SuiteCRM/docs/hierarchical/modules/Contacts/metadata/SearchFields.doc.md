# SearchFields.php

**Chemin :** `modules/Contacts/metadata/SearchFields.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les champs de recherche disponibles pour le module Contacts dans les vues liste et recherche. Configure les opérateurs SQL, les champs DB cibles et les requêtes spéciales (sous-requêtes email, favoris).

**Type :** configuration / metadata

---

## Configure

Moteur de recherche SuiteCRM pour le module Contacts (`$searchFields['Contacts']`)

## Paramètres clés

| Champ | Opérateur | Champs DB ciblés | Notes |
|---|---|---|---|
| `first_name` / `last_name` | default | directs | Recherche standard |
| `search_name` | default | `first_name`, `last_name` | Recherche unifiée |
| `account_name` | default | `accounts.name` | JOIN accounts requis |
| `phone` | default | 6 champs téléphone | Recherche multi-champs |
| `email` | subquery | `id` via `email_addr_bean_rel` | Sous-requête JOIN email_addresses |
| `optinprimary` | subquery | `id` via `email_addr_bean_rel` | Filtre opt-in email principal |
| `favorites_only` | subquery | `id` via `favorites` | Filtre favoris de l'utilisateur courant |
| `address_*` | default | adresse primaire + alternative | Recherche sur les deux adresses |
| `current_user_only` | default | `assigned_user_id` | Filtre "mes contacts" |
| `range_date_*` | default | date_entered / date_modified | Recherche par plage de dates |

---

## Impacté par / impacte

- Framework de recherche SuiteCRM — lit ce fichier pour construire les clauses WHERE
- `metafiles.php` (`searchfields`) — référence ce fichier

---

## Notes

- La recherche email via sous-requête (ligne 68-74) peut être lente sur grandes bases — pas d'index direct sur le contenu de l'email.
- `favorites_only` utilise un placeholder `{1}` pour l'ID utilisateur courant (substitué par le framework).
