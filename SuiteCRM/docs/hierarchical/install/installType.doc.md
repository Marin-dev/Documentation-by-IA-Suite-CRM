# Fichier : installType.php

**Chemin :** `install/installType.php`
**Type :** installer (vue wizard — choix type d'installation)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche la page de choix du type d'installation dans le wizard (typique vs. personnalisee) et gere la cle de licence SuiteCRM. Cette etape permet egalement de saisir/valider une cle de licence.

## Role technique
Template PHP avec gestion de session pour les donnees de licence (`setup_license_key`, `setup_license_key_users`, `setup_license_key_expire_date`, `setup_num_lic_oc`). Affiche un dropdown de selection de langue. Les 60 premieres lignes montrent l'initialisation des variables de session si la page n'a pas encore ete soumise.

---

## Dependances cles
- **Imports principaux :**
  - `get_select_options_with_id()` — generation dropdown langue
  - `get_boolean_from_request()` — lecture booleen requete
- **Variables de contexte :** `$mod_strings`, `$supportedLanguages`, `$current_language`, `$next_step`
- **Session :** `licenseKey_submitted`, `setup_license_key_users`, `setup_license_key_expire_date`, `setup_license_key`, `setup_num_lic_oc`
- **Gardes :** `sugarEntry` + `$install_script`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, etape type installation)
- **Appelle :** `install.php` (submit formulaire)

---

## Notes
- La suite du fichier (non lue) contient probablement le formulaire HTML avec les options Typical/Custom.
- La gestion de licence dans SuiteCRM est essentiellement cosmétique (SuiteCRM est AGPL open source) — INCONNU : role exact de `setup_license_key` dans le flux.
