# Fichier : AdvancedOpenEvents.php

**Chemin :** `install/suite_install/AdvancedOpenEvents.php`
**Type :** installer (configuration module AOE)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Configure le module Advanced Open Events (AOE — gestion d'evenements) en creant le template email d'invitation a un evenement par defaut.

## Role technique
Fonction `install_aoe()` qui cree un `EmailTemplate` de type `system` via `BeanFactory::newBean('EmailTemplates')` avec les variables de fusion SuiteCRM (`$contact_name`, `$fp_events_name`, etc.).

---

## Dependances cles
- **Imports principaux :**
  - `modules/Administration/Administration.php`
  - `modules/EmailTemplates/EmailTemplate.php`
  - `BeanFactory`

## Exports / Symboles principaux
| Symbole | Role |
|---|---|
| `install_aoe()` | Cree le template email "Event Invite Template" |

**Template cree :**
- Nom : `'Event Invite Template'`
- Sujet : `'You have been invited to $fp_events_name'`
- Type : `'system'`
- Corps HTML avec variables : `$contact_name`, `$fp_events_name`, `$fp_events_date_start`, `$fp_events_date_end`, `$fp_events_description`, `$fp_events_link`, `$fp_events_link_declined`

## Interactions
- **Appele par :** `install/suite_install/suite_install.php` (ligne 35)
- **Appelle :** `BeanFactory::newBean('EmailTemplates')`, `$emailTemp->save()`

---

## Notes
- Le template est publie en `'off'` par defaut — l'admin doit le publier manuellement.
- Le commentaire de GUID (ligne 9) suggere un GUID fixe prevu mais non applique.
