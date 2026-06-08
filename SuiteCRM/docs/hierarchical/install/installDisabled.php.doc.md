# installDisabled.php

**Chemin :** `install/installDisabled.php`
**Type :** `PHP (installeur — vue HTML désactivée)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Affiche une page HTML indiquant que l'installation est désactivée. Utilisé lorsque l'installeur est bloqué (SuiteCRM déjà installé ou verrou présent).

**Type :** installer (vue HTML)

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections d'accès
- `$disabled_title`, `$disabled_title_2`, `$disabled_text` — variables de message injectées par le contexte appelant
- `$sugar_md` — chemin du logo SuiteCRM
- `get_language_header()` — entête HTML lang

## Exports / Symboles principaux
Aucun. Vue HTML pure via `echo $out`.

## Interactions
- **Appelé par :** `install.php` (INCONNU : condition exacte de déclenchement)
- **Position dans le flux global :** page de blocage préventif du wizard

---

## Notes
- Les variables `$disabled_title`, `$disabled_title_2`, `$disabled_text` doivent être définies avant l'inclusion.
- Lien footer vers `suitecrm.com`, forums et guide d'installation.
