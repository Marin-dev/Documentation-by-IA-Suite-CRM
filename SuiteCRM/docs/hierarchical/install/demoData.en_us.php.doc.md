# demoData.en_us.php

**Chemin :** `install/demoData.en_us.php`
**Type :** `PHP (installeur — données de démo anglais)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le jeu de données de démonstration pour la langue anglaise (en_us). Peuple le tableau global `$sugar_demodata` avec les utilisateurs, équipes, contacts, comptes, opportunités et autres entités de démo qui seront créées lors d'une installation avec données de démo activées.

**Type :** installer / config

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `$sugar_demodata` — tableau global qui reçoit les données

## Exports / Symboles principaux
- `$sugar_demodata['users']` — tableau des 6 utilisateurs seed (Jim Brennan VP Sales, Sarah Smith, Sally Bronsen, Max, Will, Chris)
- `$sugar_demodata['teams']` — INCONNU (non lu en totalité, structure similaire)
- Autres clés probables : contacts, accounts, opportunities (INCONNU : fichier tronqué à 80 lignes)

## Interactions
- **Appelé par :** `install/populateSeedData.php` (ligne 58 : `require_once("install/demoData.{$current_language}.php")`)
- **Appelle :** rien
- **Position dans le flux global :** chargement des données de démo avant la création des entités

---

## Notes
- Fallback vers `en_us` si le fichier de la langue courante n'existe pas (géré dans `populateSeedData.php`).
- Les IDs utilisateurs sont des chaînes nommées (`seed_jim_id`, etc.) et non des UUIDs standard — TODO en attente de correction.
- Jim Brennan est le VP Sales en haut de la hiérarchie (`reports_to = null`).
