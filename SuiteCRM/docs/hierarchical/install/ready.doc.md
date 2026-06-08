# Fichier : ready.php

**Chemin :** `install/ready.php`
**Type :** installer (vue wizard — verification systeme)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Affiche la page de verification de l'environnement systeme dans le wizard d'installation. Indique a l'utilisateur si le serveur repond aux prerequis de SuiteCRM (version PHP, extensions, permissions, etc.).

## Role technique
Template PHP qui construit une chaine HTML (`$envString`) avec les resultats de verification : version PHP, extensions PHP activees, permissions de fichiers/repertoires. Inclut `ImapHandlerFactory` pour la verification IMAP.

---

## Dependances cles
- **Imports principaux :**
  - `include/Imap/ImapHandlerFactory.php` — verification IMAP (ligne 46)
  - `$mod_strings` — chaines de langue
- **Variables de contexte :** `$mod_strings`, `$install_script`
- **Garde :** `sugarEntry` requise + `$install_script`

## Exports / Symboles principaux
- `$envString` — chaine HTML — resultats des verifications systeme (consomme par la page appelante)

## Interactions
- **Appele par :** `install.php` (include, etape verification)
- **Appelle :**
  - `ImapHandlerFactory` — detection support IMAP
  - Fonctions systeme PHP (`phpversion()`, `extension_loaded()`, etc.)

---

## Notes
- La variable `$envString` est construite puis renvoyee au contexte appelant pour inclusion dans la page HTML complete.
- L'include d'`ImapHandlerFactory` (ligne 46) suggere que la disponibilite de IMAP est verifiee dans cette etape.
- Le detail complet des verifications n'est pas lisible ici (lecture limitee a 60 lignes) — INCONNU : liste exhaustive des checks.
