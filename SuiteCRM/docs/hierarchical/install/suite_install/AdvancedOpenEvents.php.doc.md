# AdvancedOpenEvents.php

**Chemin :** `install/suite_install/AdvancedOpenEvents.php`
**Type :** `PHP (installeur — initialisation module AOE)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Initialise le module Advanced Open Events (AOE — événements SuiteCRM) lors de l'installation. Crée le template d'email d'invitation aux événements par défaut.

**Type :** installer

---

## Dépendances clés
- `modules/Administration/Administration.php`
- `modules/EmailTemplates/EmailTemplate.php`
- `BeanFactory::newBean('EmailTemplates')`

## Exports / Symboles principaux
- `install_aoe()` — crée un `EmailTemplate` de type `'system'` intitulé "Event Invite Template" avec corps HTML et texte contenant les variables de substitution `$fp_events_name`, `$contact_name`, etc.

## Interactions
- **Appelé par :** `install/suite_install/suite_install.php` (ligne 35)
- **Appelle :** `BeanFactory::newBean('EmailTemplates')`, `$emailTemp->save()`
- **Position dans le flux global :** création des templates email système lors de l'installation

---

## Notes
- Le template utilise des variables de substitution SuiteCRM (`$fp_events_name`, `$fp_events_date_start`, `$fp_events_link`, etc.).
- Type `'system'` : template non modifiable par les utilisateurs standard.
- L'ID était commenté — le template n'a pas d'ID fixe, il est généré à la création.
