# Fichier : register.php

**Chemin :** `install/register.php`
**Type :** installer (vue — enregistrement)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Gere l'etape d'enregistrement optionnel de SuiteCRM aupres de SalesAgility pendant l'installation. Permet a l'utilisateur de confirmer ou ignorer l'enregistrement.

## Role technique
Verifie la presence de `$_POST['confirm']` pour determiner si le formulaire a ete soumis. Si non soumis, inclut `sugar_version.php` pour obtenir `$sugar_flavor`. Protege contre les acces directs avec une logique `$suicide` (ligne 45-55).

---

## Dependances cles
- **Imports principaux :**
  - `sugar_version.php` — version et edition SuiteCRM
- **Variables de contexte :** `$mod_strings`, `$install_script`, `$sugar_config`
- **Garde :** `sugarEntry` + `$install_script` (via logique $suicide)

## Exports / Symboles principaux
- Aucun export — affichage/traitement HTML

## Interactions
- **Appele par :** `install.php` (include, etape enregistrement)
- **Appelle :**
  - `sugar_version.php` — informations version

---

## Notes
- Logique de protection originale avec variable `$suicide` (ligne 45) — alternative a la garde `$install_script`.
- Le detail du formulaire d'enregistrement (suite du fichier non lue) est INCONNU — probablement un formulaire HTML avec informations entreprise.
- SuiteCRM etant open source (AGPL), l'enregistrement est optionnel et non bloquant.
