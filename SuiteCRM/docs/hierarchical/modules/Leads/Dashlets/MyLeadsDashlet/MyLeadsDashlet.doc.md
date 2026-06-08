# Fichier : MyLeadsDashlet.php

**Chemin :** `modules/Leads/Dashlets/MyLeadsDashlet/MyLeadsDashlet.php`
**Type :** `PHP`
**Categorie :** dashlet
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Dashlet "Mes Leads" affichable sur le tableau de bord SuiteCRM. Presente une liste filtrable et configurable des leads de l'utilisateur courant, excluant par defaut les leads convertis.

## Role technique

Classe `MyLeadsDashlet` heritant de `DashletGeneric`. Charge les colonnes depuis `MyLeadsDashlet.data.php`. Peut surcharger `process()` pour injecter des jointures supplementaires (email).

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `DashletGeneric` | `include/Dashlets/DashletGeneric.php` | Classe parente |
| `MyLeadsDashlet.data.php` | meme dossier | Definition des colonnes et filtres |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `MyLeadsDashlet` | classe | Dashlet "Mes Leads" |
| `process()` | methode | Eventuellement surcharge pour jointures email |

## Points d'attention

- Le fichier `.meta.php` associe declare les metadonnees du dashlet.
- Le fichier `.data.php` definit les colonnes disponibles et les filtres de recherche.
