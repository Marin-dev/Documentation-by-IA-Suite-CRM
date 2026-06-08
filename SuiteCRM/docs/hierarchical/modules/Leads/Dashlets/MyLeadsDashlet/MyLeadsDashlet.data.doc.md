# Fichier : MyLeadsDashlet.data.php

**Chemin :** `modules/Leads/Dashlets/MyLeadsDashlet/MyLeadsDashlet.data.php`
**Type :** `PHP`
**Categorie :** configuration (donnees dashlet)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit les colonnes disponibles et les champs de recherche du dashlet `MyLeadsDashlet` via `$dashletData['MyLeadsDashlet']`.

---

## Parametres cles

| Parametre | Contenu |
| --- | --- |
| Colonnes par defaut | name, status, phone_work, email1, account_name |
| Filtres | status, lead_source, assigned_user_id |

## Points d'attention

- Fichier de configuration pur. Charge via `require()` par `MyLeadsDashlet.php`.
