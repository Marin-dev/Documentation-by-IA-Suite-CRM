# sugar_version.php

**Chemin :** `sugar_version.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle fonctionnel

Déclare les variables de version de la base SugarCRM CE sur laquelle SuiteCRM est construit. Ces informations sont utilisées pour les compatibilités, mises à jour et affichages de version.

**Type :** config

## Rôle technique

Assigne des variables PHP globales de version après vérification que `sugarEntry` est défini. Ces variables sont chargées tôt dans le bootstrap applicatif.

---

## Dépendances clés

- **Aucune dépendance**
- **Sécurité :** bloque si `sugarEntry` non défini (ligne 41)

## Exports / Variables définies

| Variable | Valeur | Rôle |
|---|---|---|
| `$sugar_version` | `'6.5.25'` | Version SugarCRM CE de base |
| `$sugar_db_version` | `'6.5.25'` | Version du schéma DB correspondant |
| `$sugar_flavor` | `'CE'` | Édition (Community Edition) |
| `$sugar_build` | `'344'` | Numéro de build |
| `$sugar_timestamp` | `'2017-02-06 12:07PM'` | Timestamp du build |

## Relations clés

- **Appelé par :** `install.php` (ligne 84), `include/entryPoint.php` (INCONNU à confirmer)
- **Consommé par :** logique de mise à jour, vérifications de compatibilité DB, affichages admin

---

## Points d'attention

- La version `6.5.25` correspond à la base SugarCRM CE — **ne reflète pas la version SuiteCRM** (voir `suitecrm_version.php` pour `7.15.1`).
- Le timestamp `2017-02-06` est figé depuis le fork initial — ne pas le confondre avec la date de mise à jour SuiteCRM.
- Ces variables sont accessibles en global — attention aux collisions de noms.
