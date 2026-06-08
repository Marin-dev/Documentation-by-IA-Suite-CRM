# Fichier : MyContactsDashlet.php

**Chemin :** `modules/Contacts/Dashlets/MyContactsDashlet/MyContactsDashlet.php`
**Type :** PHP - Composant Dashlet
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Dashlet affichant la liste des contacts assignes a l'utilisateur courant sur la page d'accueil SuiteCRM. Permet un acces rapide aux contacts recents ou importants sans naviguer dans le module.

## Role technique

Etend `DashletGeneric` (`include/Dashlets/DashletGeneric.php`). Filtre automatiquement par `assigned_user_id = current_user->id`. Utilise le systeme de configuration standard des dashlets.

---

## Dependances cles

- `include/Dashlets/DashletGeneric.php` — classe parente
- Globales : `$current_user`, `$app_strings`, `$dashletData`

## Exports / Symboles principaux

- `MyContactsDashlet` — classe
  - `__construct($id, $def)` — initialisation avec filtrage par utilisateur courant (l.54)

## Consommateurs identifies

- Framework Dashlet SuiteCRM (page d'accueil / Home)
- Metadata dans `MyContactsDashlet.meta.php`

## Relations cles

- **Filtre sur :** `contacts.assigned_user_id = current_user`

---

## Points d'attention

- Dashlet generique — la personnalisation des colonnes passe par les parametres de configuration du dashlet.
