# Fichier : MyContactsDashlet.data.php

**Chemin :** `modules/Contacts/Dashlets/MyContactsDashlet/MyContactsDashlet.data.php`
**Type :** PHP - Configuration (donnees dashlet)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit les donnees de configuration par defaut du dashlet `MyContactsDashlet` : colonnes affichees, requete de base, options de tri.

## Role technique

Script procedural. Peuple `$dashletData['MyContactsDashlet']` avec les colonnes et parametres de la liste.

---

## Dependances cles

- Aucune

## Exports / Symboles principaux

- `$dashletData['MyContactsDashlet']` — configuration des donnees du dashlet

## Consommateurs identifies

- `MyContactsDashlet.php` (via `$dashletData` global)

---

## Points d'attention

- Fichier de donnees statiques complementaire a `MyContactsDashlet.meta.php`.
