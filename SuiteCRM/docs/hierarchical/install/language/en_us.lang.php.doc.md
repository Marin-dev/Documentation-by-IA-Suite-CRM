# en_us.lang.php

**Chemin :** `install/language/en_us.lang.php`
**Type :** `PHP (installeur — fichier de langue anglais)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit toutes les chaînes de traduction anglaises (`$mod_strings`) utilisées par le wizard d'installation de SuiteCRM. C'est le fichier de langue de référence pour l'installeur.

**Type :** installer / config

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct

## Exports / Symboles principaux
- `$mod_strings` — tableau associatif des libellés, messages d'erreur, titres et boutons de l'installeur (plusieurs centaines de clés)

Exemples de clés notables :
- `LBL_WIZARD_TITLE` — titre de la fenêtre
- `LBL_DBCONF_TITLE` — titre configuration DB
- `ERR_DB_NAME`, `ERR_DB_HOSTNAME`, `ERR_DB_LOGIN_FAILURE` — messages d'erreur DB
- `LBL_NEXT`, `LBL_BACK` — boutons de navigation
- `LBL_SYSOPTS_2`, `LBL_SITECFG_TITLE` — libellés étapes
- `LBL_STEP3`, `LBL_STEP5` — indicateurs de progression

## Interactions
- **Appelé par :** `install.php` (chargement au démarrage du wizard), `install/licensePrint.php` (ligne 51)
- **Appelle :** rien
- **Position dans le flux global :** source de toutes les chaînes affichées dans l'installeur

---

## Notes
- Seule langue nativement disponible dans l'installeur — les autres langues nécessitent l'upload d'un pack.
- Les valeurs `LBL_NEXT` et `LBL_BACK` sont utilisées comme valeurs de boutons PHP et comparées dans `install.php` pour la navigation du wizard — ne pas modifier sans vérifier les conditions de routage.
