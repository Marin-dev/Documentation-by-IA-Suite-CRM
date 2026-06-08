# MyContactsDashlet.data.php

**Chemin :** `modules/Contacts/Dashlets/MyContactsDashlet/MyContactsDashlet.data.php`
**Type :** PHP — configuration / dashlet data
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Définit les données de configuration du dashlet "Mes Contacts" : champs de recherche disponibles et colonnes affichables. Alimente le tableau `$dashletData['MyContactsDashlet']`.

**Type :** configuration

**Configure :** Colonnes et filtres du dashlet MyContactsDashlet.

## Paramètres clés

**Champs de recherche :**

| Champ | Défaut |
|---|---|
| `date_entered` | vide |
| `title` | vide |
| `primary_address_country` | vide |
| `assigned_user_id` | utilisateur courant |

**Colonnes disponibles (actives par défaut : `*`) :**

`name*`, `account_name`, `title*`, `email1`, `phone_work*`, `phone_home`, `phone_mobile`, `phone_other`, `date_entered*`, `date_modified`, `created_by`, `assigned_user_name*`

---

## Notes

- `assigned_user_id` est pré-filtré sur l'utilisateur courant (`$current_user->name`).
- Le champ `email1` utilise `customCode = '{$EMAIL1_LINK}'` pour le rendu du lien email cliquable.
