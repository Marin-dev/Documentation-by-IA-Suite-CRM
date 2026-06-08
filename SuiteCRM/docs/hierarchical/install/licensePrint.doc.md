# Fichier : licensePrint.php

**Chemin :** `install/licensePrint.php`
**Type :** installer (vue — impression licence)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Genere une page HTML imprimable contenant le texte integral de la licence AGPL de SuiteCRM. Accessible via un lien "Imprimer la licence" dans les etapes d'acceptation du wizard.

## Role technique
Charge dynamiquement le pack de langue depuis `$_GET['language']`, recupere le contenu du fichier `LICENSE.txt` via `getLicenseContents()` avec `wordwrap()` a 100 caracteres. Affiche dans une balise `<pre>` avec boutons Imprimer et Fermer.

---

## Dependances cles
- **Imports principaux :**
  - `install/language/{language}.lang.php` — chaines de langue (ligne 51)
  - `install/install_utils.php` — `getLicenseContents()`, `get_language_header()`
  - `install/install.css` — styles
- **Parametres HTTP :** `$_GET['language']` — code langue (ex: `en_us`)
- **Fichiers lus :** `LICENSE.txt`

## Exports / Symboles principaux
- Aucun export — affichage HTML uniquement

## Interactions
- **Appele par :** `welcome.php` et `license.php` via `window.open("install.php?page=licensePrint&language=...")`
- **Appelle :**
  - `clean_incoming_data()` — nettoyage entrees (ligne 49)
  - `install/install_utils.php::getLicenseContents()`

---

## Notes
- Utilise `$_GET['language']` directement dans `require_once` (ligne 51) — risque potentiel d'injection de chemin si `clean_incoming_data()` ne sanitise pas suffisamment.
- La garde `sugarEntry` est presente (ligne 3).
- Page autonome destinee a la popup navigateur uniquement.
