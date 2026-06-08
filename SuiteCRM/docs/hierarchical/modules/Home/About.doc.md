# About.php

**Chemin :** `modules/Home/About.php`
**Type :** PHP - Vue HTML
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Affiche la page "À propos" de SuiteCRM : version, contributeurs, partenaires, informations sur les packs de langue. Inclut `suitecrm_version.php` pour la version courante et optionnellement `custom_version.php`.

## Type
view

## Dépendances clés
- `suitecrm_version.php` — variable `$suitecrm_version`
- `custom_version.php` (optionnel) — variable `$custom_version`
- `$mod_strings` (global) — libellés localisés

## Exports / Symboles principaux
Aucun (script HTML pur).

## Interactions
- **Appelé par :** action `About` du module Home
- **Appelle :** `suitecrm_version.php`

## Notes
- Page statique d'informations, sans logique métier.
