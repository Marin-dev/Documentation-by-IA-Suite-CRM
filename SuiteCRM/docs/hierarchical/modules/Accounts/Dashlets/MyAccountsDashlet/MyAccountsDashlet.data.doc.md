# Fichier : MyAccountsDashlet.data.php

**Chemin :** `modules/Accounts/Dashlets/MyAccountsDashlet/MyAccountsDashlet.data.php`
**Type :** `PHP`
**Categorie :** configuration (donnees dashlet)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Peuple `$dashletData['MyAccountsDashlet']` avec les definitions des champs de recherche et des colonnes affichables dans le dashlet "Mes Comptes".

---

## Parametres cles

### Champs de recherche (`searchFields`)

| Champ | Valeur par defaut |
| --- | --- |
| `date_entered` | vide |
| `account_type` | vide |
| `industry` | vide |
| `billing_address_country` | vide |
| `assigned_user_id` | utilisateur courant |

### Colonnes (`columns`)

| Colonne | Affichee par defaut | Largeur |
| --- | --- | --- |
| `name` | oui | 40% |
| `account_type` | oui | 10% |
| `website` | oui | 8% |
| `phone_office` | oui | 15% |
| `billing_address_country` | oui | 8% |
| `email1` | non | 8% |
| `parent_name` | non | 15% |
| `date_entered` | non | 15% |

## Impacte par / impacte

- Consomme par `MyAccountsDashlet.php` pour construire la requete et le rendu
- Charge via `require()` (pas `require_once`) pour permettre le rechargement de `$dashletData`

## Points d'attention

- Les colonnes `email1` et `parent_name` necessitent des jointures supplementaires geries dans `MyAccountsDashlet.php`.
