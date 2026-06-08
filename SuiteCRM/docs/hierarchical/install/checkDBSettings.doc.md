# Fichier : checkDBSettings.php

**Chemin :** `install/checkDBSettings.php`
**Type :** installer (validation base de donnees)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Valide les parametres de connexion a la base de donnees saisis par l'utilisateur lors de l'installation. Verifie la validite du nom de base, tente la connexion, verifie l'existence de la base et des utilisateurs, et controle les capacites du driver DB.

## Role technique
Expose deux fonctions principales : `checkDBSettings()` et `printErrors()`. `checkDBSettings()` copie les parametres depuis `$_REQUEST` vers `$_SESSION` via `copyInputsIntoSession()`, puis effectue les verifications en cascade. La reponse est textuelle (`'dbCheckPassed'`, `'preexeest'` ou HTML d'erreurs) pour consommation AJAX.

---

## Dependances cles
- **Imports principaux :**
  - `DBManagerFactory` (global) — instanciation driver DB
  - `getInstallDbInstance()` — depuis `install_utils.php`
  - `installLog()` — journalisation installation
- **Session utilisee :** `setup_db_type`, `setup_db_host_name`, `setup_db_database_name`, `setup_db_admin_user_name`, `setup_db_admin_password`, `setup_db_sugarsales_user/password`, `setup_db_create_database`, `dbUSRData`

## Exports / Symboles principaux

| Fonction | Role |
|---|---|
| `checkDBSettings($silent)` | Valide tous les parametres DB ; en mode silent retourne un tableau d'erreurs |
| `printErrors($errors)` | Affiche/retourne les erreurs HTML ou `'dbCheckPassed'` si aucune |
| `copyInputsIntoSession()` | Copie `$_REQUEST` vers `$_SESSION` et gere les modes utilisateur DB |

## Interactions
- **Appele par :** `install.php` (via AJAX POST avec `checkDBSettings=true`)
- **Appelle :**
  - `getInstallDbInstance()` — driver DB
  - `$db->connect()`, `$db->disconnect()`, `$db->dbExists()`, `$db->tableExists()`, `$db->userExists()`, `$db->canInstall()`, `$db->supports()`
  - `DBManagerFactory::getManagerByType()`
  - `create_db_user_creds()` — generation credentials automatiques

---

## Notes
- Trois modes utilisateur DB : `'same'` (meme que admin), `'provide'` (fourni), `'create'` (creer), `'auto'` (genere).
- Support MySQL et MSSQL avec validations de nom de base differentes (ligne 116-132).
- Si la base existe deja avec des tables `config`, une erreur specifique est levee (ligne 182).
- En mode `silent`, les erreurs sont retournees (pas echoes) pour l'installation silencieuse.
