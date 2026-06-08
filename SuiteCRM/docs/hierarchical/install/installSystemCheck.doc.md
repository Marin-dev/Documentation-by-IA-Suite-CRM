# Fichier : installSystemCheck.php

**Chemin :** `install/installSystemCheck.php`
**Type :** installer (verification systeme)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Effectue la verification de l'environnement systeme avant installation (extensions PHP, permissions de fichiers, configuration serveur). Peut etre appele en mode AJAX pour valider le systeme sans rechargement de page.

## Role technique
Expose la fonction `runCheck($install_script, $mod_strings)` qui execute les verifications et retourne les resultats. Fixe `$_SESSION['setup_license_accept'] = true` avant de lancer le check. Journalise chaque etape via `installLog()`.

---

## Dependances cles
- **Imports principaux :**
  - `installLog()` — journalisation
  - `$mod_strings` — chaines d'erreur/succes
- **Session :** `$_SESSION['setup_license_accept']` fixe a `true`
- **Garde :** `sugarEntry` requise

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `runCheck($install_script, $mod_strings)` | Verifie l'environnement systeme et retourne les resultats |

## Interactions
- **Appele par :** `install.php` (via AJAX POST avec `checkInstallSystem=true` ou include direct)
- **Appelle :**
  - `installLog()` — depuis `install_utils.php`
  - Fonctions systeme PHP pour les verifications

---

## Notes
- Le detail complet des verifications (liste des checks PHP, extensions, permissions) n'est pas lisible dans les 60 premieres lignes — INCONNU : liste exhaustive.
- Cette fonction est appelee via AJAX depuis `welcome.php` et `license.php` (`callSysCheck()`) avant de permettre le passage a l'etape suivante.
- La reponse attendue par le client AJAX est la chaine `'passed'` en cas de succes.
