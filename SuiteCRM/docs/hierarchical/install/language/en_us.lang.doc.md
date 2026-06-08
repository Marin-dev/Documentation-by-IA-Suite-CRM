# Fichier : en_us.lang.php

**Chemin :** `install/language/en_us.lang.php`
**Type :** configuration (chaines de traduction installeur)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Fournit toutes les chaines de texte en anglais (US) utilisees par le wizard d'installation de SuiteCRM. Ce fichier definit les labels, messages d'erreur, titres et instructions affiches dans chaque etape du wizard.

## Role technique
Peuple le tableau global `$mod_strings` avec des centaines de cles/valeurs. Les cles suivent la convention `LBL_*` pour les labels, `ERR_*` pour les erreurs. Ce tableau est charge dynamiquement selon la langue selectionnee par l'utilisateur.

---

## Dependances cles
- **Imports principaux :** aucun
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
- `$mod_strings` — tableau — toutes les chaines de l'installeur en anglais US

**Exemples de cles :**
- `LBL_SYSOPTS_2` — description choix type DB
- `LBL_DBCONF_TITLE` — titre configuration DB
- `ERR_ADMIN_EMAIL`, `ERR_SITE_URL` — messages d'erreur validation

## Interactions
- **Appele par :**
  - `install.php` — chargement de la langue courante
  - `install/licensePrint.php` (ligne 51) — pour les chaines d'impression
- **Appelle :** rien

---

## Notes
- C'est la langue par defaut et de fallback : si une cle manque dans une autre langue, il faut la chercher ici.
- Autres langues supportees placees dans le meme repertoire `install/language/`.
- INCONNU : liste exhaustive de toutes les cles (fichier long non lu en entier).
