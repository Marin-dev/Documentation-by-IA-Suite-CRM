# MyContactsDashlet.php

**Chemin :** `modules/Contacts/Dashlets/MyContactsDashlet/MyContactsDashlet.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Dashlet "Mes Contacts" pour la page d'accueil SuiteCRM. Affiche la liste des contacts assignés à l'utilisateur courant dans un widget dashlet configurable. Hérite de `DashletGeneric` pour la gestion standard des dashlets.

**Type :** helper / dashlet

---

## Dépendances clés

- `include/Dashlets/DashletGeneric.php` (classe parente)
- `$dashletData` global — données de configuration du dashlet
- `$current_user` — filtrage par utilisateur assigné
- `$app_strings` — libellés

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `MyContactsDashlet` | classe | Dashlet liste des contacts de l'utilisateur courant |
| `__construct($id, $def)` | méthode | Initialisation avec chargement de la configuration dashlet |

---

## Interactions

**Appelée par :** Framework de dashlets SuiteCRM lors du rendu de la page d'accueil ou des tableaux de bord.

**Position dans le flux global :** Widget d'accès rapide aux contacts assignés à l'utilisateur.

---

## Notes

- La configuration et les colonnes affichées sont définies dans les fichiers associés `MyContactsDashlet.meta.php` et `MyContactsDashlet.data.php`.
