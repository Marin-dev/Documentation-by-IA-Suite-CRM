# performSetup.php

**Chemin :** `install/performSetup.php`
**Type :** `PHP (installeur — exécution de l'installation)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Orchestre l'exécution complète de l'installation SuiteCRM : écriture de la configuration, création de la BDD, installation des tables, création de l'utilisateur admin, peuplement des données initiales et de démo. Gère la progression en temps réel via `install/status.json`.

**Type :** installer

---

## Dépendances clés
- `sugarEntry` + `$install_script` — protections
- `install/install_utils.php` — utilitaires d'installation
- `modules/TableDictionary.php` — dictionnaire des tables
- `TrackerManager` — mis en pause pendant l'installation
- `$mod_strings` — messages localisés
- `$GLOBALS['installing'] = true` — flag global d'installation
- `ini_set("output_buffering", "0")` + `ob_implicit_flush()` — sortie en temps réel
- `set_time_limit(3600)` — timeout étendu à 1h

## Exports / Symboles principaux
- `installStatus(string $msg, $cmd = null, bool $overwrite = false, string $before = '[ok]<br>')` — écrit dans `install/status.json` le message de progression courant (et éventuellement une commande de redirection)

## Interactions
- **Appelé par :** `install.php` (soumission du formulaire de configuration via `installConfig.php`)
- **Lit :** `install/status.json` est lu par le client JS toutes les 1200ms
- **Appelle :** de nombreuses fonctions d'installation (INCONNU : reste du fichier non lu)
- **Position dans le flux global :** étape finale d'exécution — transforme la configuration en instance SuiteCRM fonctionnelle

---

## Notes
- `TrackerManager::getInstance()->pause()` : désactive le tracking pendant l'installation pour performance.
- `installStatus()` cumule les messages précédents dans `status.json` (ajout avec `$before`), sauf si `$overwrite = true`.
- `ob_implicit_flush()` permet d'afficher la progression ligne par ligne sans buffer (utile pour le suivi de la barre de progression).
- Timeout 3600s nécessaire car l'installation peut prendre plusieurs minutes sur des serveurs lents.
