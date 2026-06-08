# Administration.php

**Chemin :** `modules/Administration/Administration.php`
**Type :** PHP (Model / SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe centrale du module Administration : represente le modele de configuration systeme de SuiteCRM. Elle permet de lire, ecrire et mettre en cache tous les parametres applicatifs stockes dans la table `config` (SMTP, notifications, portail, proxy, LDAP, captcha, etc.). C'est le point d'entree pour toute lecture/ecriture de configuration persistante.

## Role technique
Etend `SugarBean` avec `$table_name = "config"`. Gere un cache en memoire (via `sugar_cache_retrieve`/`sugar_cache_put`) des parametres pour eviter les requetes repetees. Dechiffre les mots de passe sensibles (ldap_admin_password, proxy_password) a la lecture et les chiffre a l'ecriture. Fusionne les parametres email sortant depuis `OutboundEmail` si absents.

---

## Dependances cles
| Import | Role |
|---|---|
| `data/SugarBean.php` | Classe parente ORM |
| `include/OutboundEmail/OutboundEmail.php` | Lecture/ecriture parametres email sortant |
| `DBManagerFactory` (global) | Acces base de donnees |
| `sugar_cache_*` (fonctions globales) | Cache applicatif |

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `Administration` | Classe | Modele de configuration systeme |
| `retrieveSettings($category, $clean)` | Methode | Charge les parametres en BDD, avec cache |
| `saveConfig()` | Methode | Persiste les donnees $_POST dans config |
| `saveSetting($category, $key, $value)` | Methode | INSERT ou UPDATE d'un parametre individuel |
| `checkSmtpError($displayWarning)` | Methode | Verifie si le serveur SMTP est configure |
| `get_config_prefix($str)` | Methode | Decoupe `category_key` en `[category, key]` |
| `$settings` | Propriete | Tableau associatif de tous les parametres charges |
| `$config_categories` | Propriete | Categories acceptees : disclosure, notify, system, portal, proxy, massemailer, ldap, captcha, sugarpdf |

## Interactions
- **Appele par :** `Save.php`, `PasswordManager.php`, `DisplayWarnings.php`, `BeanFactory::newBean('Administration')` partout dans l'application
- **Appelle :** `OutboundEmail::getSystemMailerSettings()`, `OutboundEmail::saveSystem()`, fonctions de chiffrement SugarBean
- **Table BDD :** `config` (category, name, value)

---

## Notes
- Les mots de passe LDAP et proxy sont chiffres/dechiffres automatiquement : lignes 143-145 (lecture) et 224-226 (ecriture).
- Le cache `admin_settings_cache` est invalide apres chaque `saveSetting()` (ligne 233).
- `$disable_custom_fields = true` : pas de champs personnalises possibles sur ce bean.
- La categorie `mail` est commentee (ligne 57) : la gestion des emails sortants est deplacee vers `OutboundEmail`.
