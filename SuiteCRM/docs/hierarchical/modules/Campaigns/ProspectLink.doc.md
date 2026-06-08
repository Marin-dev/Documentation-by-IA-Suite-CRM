# ProspectLink.php

**Chemin :** `modules/Campaigns/ProspectLink.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Extension de la classe Link2 pour les relations Campaign → cibles (Contacts, Leads, Accounts). Surcharge `getJoin()` pour produire une jointure via `prospect_list_campaigns` et `prospect_lists_prospects`, permettant de lier correctement les cibles d'une campagne à travers les listes de prospects.

## Type

`helper` (classe lien custom)

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `data/Link2.php` | Classe de lien ORM de base |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ProspectLink` | classe | Lien ORM custom pour les relations Campaign → cibles |
| `getJoin()` | méthode | Génère le JOIN en 3 tables pour accéder aux cibles via les listes |

---

## Interactions

- **Référencé dans :** `vardefs.php` champs `leads`, `contacts`, `accounts` (attributs `link_class` et `link_file`)
- **Utilisé par :** Framework ORM lors des requêtes de sous-panneaux Campaign
- **Position dans le flux global :** Couche de jointure SQL pour afficher les cibles dans la vue détail Campaign

---

## Points d'attention

- Correctif pour bug #40166 : sans ce lien custom, les noms Contact/Account ne s'affichaient pas dans les rapports campaign_log.
- Le JOIN en 3 étapes (prospect_list_campaigns → prospect_lists_prospects → table cible) peut être lourd sur de grandes campagnes.
