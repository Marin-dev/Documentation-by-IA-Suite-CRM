# licensePrint.php

**Chemin :** `install/licensePrint.php`
**Type :** `PHP (installeur — vue HTML impression licence)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Génère une version imprimable de la licence AGPL pour SuiteCRM. Accessible depuis un lien "Print License" sur la page de licence du wizard d'installation. Lit `LICENSE.txt` et le formatte avec `wordwrap` (100 caractères).

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` — protection d'accès direct
- `install/language/{language}.lang.php` — fichier de langue via `$_GET['language']`
- `install/install_utils.php` — `getLicenseContents()`
- `clean_incoming_data()` — sanitisation des données en entrée

## Exports / Symboles principaux
Aucun. Vue HTML pure.

## Interactions
- **Appelé par :** lien "Print" depuis `license.php` (INCONNU : URL exacte)
- **Position dans le flux global :** page auxiliaire d'impression de la licence

---

## Notes
- `$_GET['language']` est utilisé directement dans le `require_once` — `clean_incoming_data()` doit prévenir les traversées de chemin.
- `wordwrap($text, 100)` pour un affichage propre en texte brut.
