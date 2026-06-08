# AOPAdmin.php

**Chemin :** `modules/Administration/AOPAdmin.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration du module AOP (Advanced OpenCases / portail de support). Configure : activation AOP, portail Joomla (URL, cle d'acces), methode de distribution des tickets, templates email (creation de compte, creation/fermeture de ticket, notifications utilisateur/contact), adresse d'expediteur du support, et regles de changement automatique de statut de ticket.

## Role technique
Script procedral. En POST (`do=save`) : normalise l'URL Joomla (ajoute http:// si absent), serialise les regles de statut en JSON, et persiste via `Configurator::saveConfig()`. En GET : charge les valeurs depuis `$cfg->config['aop']`, construit les dropdowns de templates email et de methode de distribution, et affiche le template `AOPAdmin.tpl`.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/AOP_Case_Updates/util.php` | `getAOPAssignField()`, `getStatusRowTemplate()` |
| `modules/Configurator/Configurator.php` | Persistance config |
| `BeanFactory` | Acces Cases, Users, EmailTemplates |
| `$app_list_strings['dom_email_distribution_for_auto_create']` | Options de distribution |
| `Sugar_Smarty` | Template |

## Symboles principaux

| Fonction | Role |
|---|---|
| `getStatusRowTemplate($mod_strings, $ifDropdown, $thenDropdown)` | Genere une ligne HTML pour les regles if/then de statut |

## Interactions
- **Appele par :** `index.php?module=Administration&action=AOPAdmin`
- **Appelle :** `Configurator::saveConfig()`, `BeanFactory::getBean('Cases')`, `BeanFactory::getBean('Users')`
- **Template :** `modules/Administration/AOPAdmin.tpl`

---

## Notes
- Les regles de changement de statut (`case_status_changes`) sont stockees en JSON dans `config_override.php` (ligne 127) — complexe a debugger.
- `distribution_method = 'singleUser'` requiert une validation JS (`addToValidate`) pour le champ `distribution_user_id`.
- Supprime l'option `AOPDefault` de la liste de distribution (ligne 133) — valeur reservee.
