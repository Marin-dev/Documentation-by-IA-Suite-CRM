# checkDBSettings.php

**Chemin :** `install/checkDBSettings.php`
**Type :** `PHP (installeur — validation DB)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Fournit la fonction de validation des paramètres de connexion à la base de données lors de l'installation. Vérifie le nom de la BDD, le hostname, les mots de passe, tente une connexion réelle et détecte les conflits (BDD existante, utilisateur existant, etc.).

**Type :** installer

---

## Dépendances clés
- `$mod_strings` — messages d'erreur localisés
- `getInstallDbInstance()` — instance du driver DB (depuis `install_utils.php`)
- `installLog()` — journalisation de l'installation
- `$_SESSION` — paramètres de configuration DB (setup_db_*)
- `DBManagerFactory` — pour récupérer le manager selon le type

## Exports / Symboles principaux
- `checkDBSettings(bool $silent = false)` — valide les paramètres DB ; retourne les erreurs si `$silent = true`, sinon les affiche via `printErrors()`
- `printErrors(array $errors)` — affiche les erreurs de validation ; émet `'dbCheckPassed'` si aucune erreur, `'preexeest'` si la BDD existe déjà
- `copyInputsIntoSession()` — synchronise `$_REQUEST` vers `$_SESSION` et gère les 4 modes d'utilisateur DB (`auto`, `provide`, `create`, `same`)

## Interactions
- **Appelé par :** `install.php` (via `checkDBSettings=true` en POST AJAX depuis `dbConfig_a.php`)
- **Appelle :** `getInstallDbInstance()`, `$db->connect()`, `$db->dbExists()`, `$db->tableExists()`, `$db->userExists()`, `$db->canInstall()`, `DBManagerFactory::getManagerByType()`
- **Position dans le flux global :** étape 5 du wizard d'installation (configuration DB), appelée en AJAX avant la progression

---

## Notes
- La réponse AJAX est textuelle : `'dbCheckPassed'`, `'preexeest'` ou HTML d'erreurs.
- Le mode `'auto'` génère un utilisateur DB aléatoire (`sugar` + 5 chars aléatoires).
- `copyInputsIntoSession()` est appelée systematiquement au début de `checkDBSettings()` (ligne 54).
- Support MySQL et MSSQL avec validations spécifiques du nom de BDD (caractères interdits).
- Détection de BDD existante avec config (`config` table + version) pour éviter les réinstallations accidentelles.
