# Fichier : MyEmailsDashlet.php

**Chemin :** `modules/Emails/Dashlets/MyEmailsDashlet/MyEmailsDashlet.php`
**Type :** PHP — Dashlet
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Dashlet "Mes Emails" affichable sur le tableau de bord SuiteCRM. Affiche la liste des emails de l'utilisateur courant dans un widget redimensionnable.

## Role technique

Herite de `DashletGeneric`. Charge les donnees depuis `MyEmailsDashlet.data.php` au constructeur.

---

## Dependances

- **Herite de :** `DashletGeneric` (`include/Dashlets/DashletGeneric.php`)
- **Inclut :** `modules/Emails/Dashlets/MyEmailsDashlet/MyEmailsDashlet.data.php`
- **Globales :** `$current_user`, `$app_strings`, `$dashletData`

## Exports / Symboles principaux

- `MyEmailsDashlet` — classe dashlet
  - Constructeur prend `$id` et `$def` optionnel

## Relations cles

- **Appele par :** framework Dashlet SuiteCRM

---

## Points d'attention

- Corps complet INCONNU (seulement 60 lignes lues).
