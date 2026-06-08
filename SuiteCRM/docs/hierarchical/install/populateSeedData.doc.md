# Fichier : populateSeedData.php

**Chemin :** `install/populateSeedData.php`
**Type :** installer (insertion donnees de demonstration)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Peuple la base de donnees avec des donnees de demonstration (contacts, comptes, opportunites, etc.) si l'utilisateur a choisi cette option pendant l'installation. Charge les donnees depuis des fichiers de demo localises.

## Role technique
Inclut les fichiers de demo selon la langue courante (`demoData.{langue}.php` ou `demoData.en_us.php` en fallback). Utilise `UserDemoData` et `TeamDemoData` pour creer les utilisateurs et equipes de demo. Initialise le generateur aleatoire avec une graine fixe (93285903) pour reproductibilite inter-installations.

---

## Dependances cles
- **Imports principaux :**
  - `include/language/{current_language}.lang.php` ou `en_us.lang.php`
  - `install/UserDemoData.php` — classe `UserDemoData`
  - `install/TeamDemoData.php` — classe `TeamDemoData`
  - `install/demoData.{language}.php` — donnees demo localisees
  - `DBManagerFactory::getInstance()` — connexion DB
- **Variables de contexte :** `$current_language`, `$sugar_demodata`, `$app_list_strings`
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- Aucun export — execution directe

## Interactions
- **Appele par :** `install.php` (include, si `demoData=yes`)
- **Appelle :**
  - `UserDemoData` (instanciation et population)
  - `TeamDemoData` (instanciation et population)
  - `return_app_list_strings_language('en_us')` — chaines listes

---

## Notes
- La graine fixe `mt_srand(93285903)` (ligne 79) garantit que les UUID/donnees demo sont identiques sur toutes les installations du meme code base.
- Le tableau `$sugar_demodata` contient : `users[]`, `last_name_array`, `first_name_array`, `company_name_array`, `street_address_array`, `city_array` (lignes 64-68).
- `$_REQUEST['useEmailWidget'] = "true"` (ligne 71) — forçage du widget email pour la creation de demo data.
