# Fichier : SystemEmailTemplates.php

**Chemin :** `install/suite_install/SystemEmailTemplates.php`
**Type :** installer (installation templates email systeme)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Installe les templates d'email systeme par defaut de SuiteCRM lors de l'installation initiale (notifications, alertes automatiques, etc.).

## Role technique
Expose deux fonctions : `installSystemEmailTemplates()` charge les templates depuis `getSystemEmailTemplates()` et les persiste via la classe `EmailTemplate`. `setSystemEmailTemplatesDefaultConfig()` configure les parametres par defaut associes.

---

## Dependances cles
- **Imports principaux :**
  - `modules/EmailTemplates/EmailTemplate.php` — classe `EmailTemplate`
  - `$sugar_config` (global)
  - `getSystemEmailTemplates()` — INCONNU : origine de cette fonction

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `installSystemEmailTemplates()` | Installe les templates d'email systeme |
| `setSystemEmailTemplatesDefaultConfig()` | Configure les parametres par defaut des templates |

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (lignes 60-61)
- **Appelle :**
  - `getSystemEmailTemplates()` — recupere la liste des templates
  - `EmailTemplate` — persistence des templates

---

## Notes
- `getSystemEmailTemplates()` est appelee mais son origine n'est pas visible dans les 50 lignes lues — INCONNU : fichier ou module source de cette fonction.
- Les templates systeme incluent probablement : confirmation inscription, reset password, notifications d'affectation, etc.
