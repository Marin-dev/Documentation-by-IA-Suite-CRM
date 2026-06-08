# install_defaults.php

**Chemin :** `install/install_defaults.php`
**Type :** `PHP (installeur — valeurs par défaut)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le tableau `$installer_defaults` contenant toutes les valeurs par défaut des paramètres de session du wizard d'installation. Utilisé pour initialiser les variables de session avant le début du processus d'installation.

**Type :** installer / config

---

## Dépendances clés
Aucune dépendance externe.

## Exports / Symboles principaux
- `$installer_defaults` — tableau associatif des valeurs par défaut

| Paramètre | Valeur par défaut |
|---|---|
| `language` | `'en_us'` |
| `install_type` | `'typical'` |
| `setup_db_type` | `'mysql'` |
| `setup_db_database_name` | `'suitecrm'` |
| `setup_db_host_instance` | `'SQLEXPRESS'` |
| `setup_db_create_database` | `true` |
| `setup_db_drop_tables` | `false` |
| `setup_license_accept` | `false` |
| ... | (voir fichier complet) |

## Interactions
- **Appelé par :** `install.php` ou `install_utils.php` (INCONNU : point exact d'inclusion)
- **Appelle :** rien
- **Position dans le flux global :** initialisation en début de session d'installation

---

## Notes
- Fichier de données pur, sans protection `sugarEntry` (pas nécessaire car pas d'accès direct attendu).
- La valeur par défaut `setup_db_host_instance = 'SQLEXPRESS'` est spécifique à MSSQL.
