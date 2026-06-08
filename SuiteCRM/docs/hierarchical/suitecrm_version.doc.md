# suitecrm_version.php

**Chemin :** `suitecrm_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Déclare la version officielle de SuiteCRM. Source de vérité pour la version applicative affichée dans l'interface, utilisée dans les mises à jour et les rapports de diagnostic.

**Type :** config

## Rôle technique

Assigne deux variables PHP globales après vérification que `sugarEntry` est défini.

---

## Dépendances clés

- **Aucune dépendance**
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 2)

## Exports / Variables définies

| Variable | Valeur | Rôle |
|---|---|---|
| `$suitecrm_version` | `'7.15.1'` | Version actuelle de SuiteCRM |
| `$suitecrm_timestamp` | `'2026-03-19 12:00:00'` | Date de release |

## Relations clés

- **Appelé par :** `install.php` (ligne 85), INCONNU pour les autres points de chargement
- **Consommé par :** affichage de version dans l'interface admin, logique de mise à jour, `$setup_sugar_version` dans `install.php`

---

## Points d'attention

- Ce fichier est le point de mise à jour lors de chaque release SuiteCRM — à modifier en priorité lors d'une montée de version.
- Distinct de `sugar_version.php` qui porte la version SugarCRM CE de base (`6.5.25`).
- `$suitecrm_version` est utilisé comme `$setup_sugar_version` dans `install.php` ligne 114.
