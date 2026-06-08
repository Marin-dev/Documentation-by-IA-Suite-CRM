# AdvancedOpenPortal.php

**Chemin :** `install/suite_install/AdvancedOpenPortal.php`
**Type :** `PHP (installeur — initialisation module AOP)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module Advanced Open Portal (AOP — portail client SuiteCRM) lors de l'installation. Configure les paramètres par défaut (portail désactivé, distribution round-robin) et crée les templates d'email système du portail.

**Type :** installer

---

## Dépendances clés
- `modules/EmailTemplates/EmailTemplate.php`
- `BeanFactory::newBean('EmailTemplates')`
- `$sugar_config` — tableau de configuration global
- `write_array_to_file()` — écriture de `config.php`

## Exports / Symboles principaux
- `install_aop()` — configure `$sugar_config['aop']` (portail désactivé, distribution round-robin), appelle `getTemplates()` et crée les templates email
- `getTemplates()` — INCONNU (function non lue dans les 60 premières lignes)

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 29)
- **Appelle :** `BeanFactory::newBean('EmailTemplates')`, `$template->save()`, `write_array_to_file()`
- **Position dans le flux global :** configuration du portail client lors de l'installation

---

## Notes
- Portail AOP désactivé par défaut (`enable_portal = false`).
- Méthode de distribution par défaut : `'roundRobin'`.
- Les champs `joomla_url`, `distribution_user_id`, `support_from_address`, `support_from_name` sont vides par défaut.
