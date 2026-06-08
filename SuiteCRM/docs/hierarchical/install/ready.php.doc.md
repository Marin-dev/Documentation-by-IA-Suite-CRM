# ready.php

**Chemin :** `install/ready.php`
**Type :** `PHP (installeur — vue HTML récapitulatif système)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche le récapitulatif de l'environnement système (version PHP, extensions, serveur) avant l'étape de configuration. Équivalent d'une vue "ready check" finale permettant à l'utilisateur de vérifier l'environnement avant de lancer l'installation.

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `include/Imap/ImapHandlerFactory.php` — vérification IMAP
- `$mod_strings` — messages localisés
- `PHP_VERSION`, `$_SERVER` — informations système

## Exports / Symboles principaux
Aucun. Vue HTML procédurale (variable `$envString` construite progressivement).

## Interactions
- **Appelé par :** `install.php` (INCONNU : étape exacte dans le flux)
- **Position dans le flux global :** vue récapitulative système, probablement après `installSystemCheck.php`

---

## Notes
- Vérifie la disponibilité d'IMAP via `ImapHandlerFactory` (ligne 46).
- Construit une chaîne HTML `$envString` avec les informations système, version PHP, etc.
