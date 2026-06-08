# Fichier : installDisabled.php

**Chemin :** `install/installDisabled.php`
**Type :** installer (vue — installation desactivee)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche une page informant l'utilisateur que l'installation a ete desactivee sur ce serveur. Typiquement affichee quand SuiteCRM detecte que `install.php` ne doit pas etre accessible (post-installation ou configuration admin).

## Role technique
Template PHP generant une page HTML simple avec un titre desactivation (`$disabled_title`) et un message d'information. Utilise le layout HTML 4.01 Transitional (ancien format).

---

## Dependances cles
- **Imports principaux :** aucun
- **Variables de contexte :** `$mod_strings`, `$disabled_title`, `$install_script`
- **Garde :** `sugarEntry` requise + `$install_script`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `install.php` (include, quand installation desactivee)
- **Appelle :** rien

---

## Notes
- Page de garde de securite — empeche l'acces au wizard post-installation.
- La variable `$disabled_title` est fournie par `install.php` (non visible ici).
