# vardefs.php

**Chemin :** `modules/Administration/vardefs.php`
**Type :** PHP (configuration / schema BDD)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit les schemas de deux tables systeme : `config` (parametres applicatifs) et `upgrade_history` (historique des mises a jour et modules installes). Ces definitions sont utilisees par le framework ORM pour creer/reparer les tables et valider les donnees.

## Role technique
Renseigne la variable globale `$dictionary` avec deux entrees. Utilise la syntaxe standard SugarCRM `$dictionary['NomBean'] = array('table' => ..., 'fields' => ..., 'indices' => ...)`.

---

## Schemas definis

### Table `config`
| Colonne | Type | Longueur | Description |
|---|---|---|---|
| `category` | varchar | 32 | Groupe du parametre (ex: system, ldap, notify) |
| `name` | varchar | 32 | Nom du parametre |
| `value` | text | - | Valeur du parametre |

Index : `idx_config_cat` sur `category`

### Table `upgrade_history`
| Colonne | Type | Description |
|---|---|---|
| `id` | id | Identifiant unique |
| `filename` | varchar(255) | Fichier de mise a jour en cache |
| `md5sum` | varchar(32) | Checksum MD5 du fichier |
| `type` | varchar(30) | Type : module, patch, theme, langpack |
| `status` | varchar(50) | Statut : installed, etc. |
| `version` | varchar(64) | Version du manifest |
| `name` | varchar(255) | Nom du paquet |
| `description` | text | Description |
| `id_name` | varchar(255) | Identifiant unique du module |
| `manifest` | longtext | Copie serialisee du manifest |
| `date_entered` | datetime | Date d'installation |
| `enabled` | bool | Paquet actif (defaut: 1) |

Index : cle primaire `id`, contrainte unique sur `md5sum`

## Interactions
- **Consomme par :** `Administration.php` (classe), `UpgradeHistory.php` (classe), outils de reparation DB (`repairDatabase.php`)
- **Lu par :** `VardefManager`, `DBManager::repairTable()`

## Notes
- La table `upgrade_history` n'a pas de colonne `deleted` — les suppressions sont physiques (cf. `UpgradeHistory::retrieve()` ligne 307 qui ignore le filtre `deleted`).
- `upgrade_history_md5_uk` garantit l'unicite par fichier installe.
