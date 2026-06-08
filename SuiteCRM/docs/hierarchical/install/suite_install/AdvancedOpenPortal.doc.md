# Fichier : AdvancedOpenPortal.php

**Chemin :** `install/suite_install/AdvancedOpenPortal.php`
**Type :** installer (configuration module AOP)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le module Advanced Open Portal (AOP) de SuiteCRM lors de l'installation : parametres du portail client, URL Joomla, methode de distribution des cases, et templates email AOP.

## Role technique
Fonction `install_aop()` qui initialise `$sugar_config['aop']` avec les valeurs par defaut, puis installe les templates email du portail via `BeanFactory::newBean('EmailTemplates')` et `getTemplates()`.

---

## Dependances cles
- **Imports principaux :**
  - `modules/EmailTemplates/EmailTemplate.php`
  - `BeanFactory` — creation beans
  - `getTemplates()` — INCONNU : origine de la fonction
  - `$sugar_config` (global)

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_aop()` | Configure AOP et installe les templates email du portail |

**Parametres configures :**
- `aop.enable_portal = false` — portail desactive par defaut
- `aop.joomla_url = ''` — URL Joomla vide
- `aop.distribution_user_id = ''`
- `aop.support_from_address/name = ''`
- `aop.distribution_method = 'roundRobin'`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 29)
- **Appelle :**
  - `BeanFactory::newBean('EmailTemplates')` — creation templates
  - `getTemplates()` — recuperation templates AOP

---

## Notes
- Le portail est desactive par defaut (`enable_portal = false`) — l'admin doit l'activer manuellement.
- `getTemplates()` n'est pas visible dans les premiers imports — INCONNU : source de cette fonction.
