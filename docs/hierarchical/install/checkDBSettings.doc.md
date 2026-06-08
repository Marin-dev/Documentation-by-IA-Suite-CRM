# checkDBSettings.php

**Chemin :** `install/checkDBSettings.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-28

## Role

Valide la configuration de base de donnees saisie par l'utilisateur lors de l'installation de SuiteCRM. Verifie la connectivite, l'existence de la base, les droits de l'utilisateur DB et la compatibilite du moteur de base de donnees.

## Responsabilites

- Fonction `checkDBSettings($silent)` : orchestre l'ensemble des verifications DB.
  - Copie les parametres POST/SESSION via `copyInputsIntoSession()`.
  - Valide que le nom de la base n'est pas vide et est syntaxiquement correct (regles differentes selon MySQL/MSSQL).
  - Tente une connexion avec le compte d'application ou le compte admin.
  - Verifie si la base existe deja et si des tables SuiteCRM y sont presentes.
  - Verifie que l'utilisateur DB demande n'existe pas deja.
  - Appelle `$db->canInstall()` pour les verifications specifiques au moteur.
- Fonction `printErrors($errors)` : genere le HTML d'erreur ou retourne `dbCheckPassed` / `preexeest`.
- Fonction `copyInputsIntoSession()` : synchronise `$_REQUEST` vers `$_SESSION` pour tous les parametres DB et FTS ; gere les trois modes de creation d'utilisateur (`auto`, `create`, `provide`, `same`).

## Dependances internes

- `install_utils.php` : fonctions `installLog()`, `getInstallDbInstance()`, `create_db_user_creds()`.
- `DBManagerFactory` (core SuiteCRM) : creation de l'instance DB.
- `$_SESSION` / `$_REQUEST` : source des parametres de formulaire.
- Globale `$mod_strings` : chaines de traduction des erreurs.

## Exports / Points d'entree

- `checkDBSettings($silent = false)` — appelee par `install.php` lors de la soumission AJAX du formulaire de configuration DB.
- `printErrors($errors)` — echoes HTML d'erreur ou codes sentinelles (`dbCheckPassed`, `preexeest`).
- `copyInputsIntoSession()` — preparatoire, appelee par `checkDBSettings()`.

## Notes techniques

- En mode `$silent = true`, retourne un tableau d'erreurs sans echo (utilise pour la validation silencieuse via `install_utils.php::validate_dbConfig()`).
- Le sentinel `preexeest` indique que la base existe deja et que l'utilisateur doit confirmer l'ecrasement.
- La detection du type de DB se fait via `$db->dbType` ; la liste de types supportes est MySQL et MSSQL (cas par defaut).
- La creation automatique d'utilisateur (`auto`) genere des identifiants aleatoires prefixes `sugar`.
