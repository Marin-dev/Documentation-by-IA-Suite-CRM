# Fichier : demoData.en_us.php

**Chemin :** `install/demoData.en_us.php`
**Type :** configuration (donnees de demonstration)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Fournit les donnees de demonstration en anglais (US) pour l'installation de SuiteCRM : tableaux de noms, entreprises, adresses, villes utilises pour generer des enregistrements fictifs.

## Role technique
Peuple le tableau global `$sugar_demodata` avec des tableaux d'echantillons : utilisateurs, noms de famille, prenoms, noms d'entreprises, adresses, villes. Ces donnees sont utilisees par `populateSeedData.php` pour creer des enregistrements CRM realistes.

---

## Dependances cles
- **Imports principaux :** aucun
- **Globaux :** `$sugar_demodata`
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- `$sugar_demodata` (global) — tableau — donnees de demo en_us avec sous-cles :
  - `users[]` — configurations utilisateurs de demo
  - `last_name_array` — noms de famille
  - `first_name_array` — prenoms
  - `company_name_array` — noms d'entreprises
  - `street_address_array` — adresses
  - `city_array` — villes

## Interactions
- **Appele par :** `install/populateSeedData.php` (ligne 60)
- **Appelle :** rien

---

## Notes
- Fichier de donnees statiques — uniquement des tableaux PHP.
- Le fallback vers ce fichier est systematique si `demoData.{langue}.php` n'existe pas.
- La graine aleatoire fixe dans `populateSeedData.php` garantit la reproductibilite de la generation.
