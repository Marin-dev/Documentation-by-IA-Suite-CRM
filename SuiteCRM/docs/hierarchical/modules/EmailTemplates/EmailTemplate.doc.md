# EmailTemplate.php

**Chemin :** `modules/EmailTemplates/EmailTemplate.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean principal des templates email (table `email_templates`). Stocke le sujet, le corps HTML, le corps texte, les pieces jointes et les macros de variables. Expose des methodes pour generer les definitions JS de champs (selecteur de variables dans l'editeur), parser les templates et remplacer les URLs de tracking.

**Type :** model

---

## Dependances cles
- `SugarBean` (classe parente)
- `BeanFactory` (Contacts, Accounts, Leads, Prospects, Users, Notes)
- `LoggerManager`
- Table `email_templates`

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailTemplate` | classe | Bean template email |
| `generateFieldDefsJS()` | methode | Genere les definitions JS des variables de template (contact_, account_, contact_user_) |
| `parse_tracker_urls()` | methode | Remplace les tokens de tracking par des URLs trackees |
| `parse_email_template()` | methode | Substitution des variables dans le corps du template (methode historique) |
| `$badFields` | propriete | Liste de champs exclus de la selection de variables |

---

## Interactions
- **Appele par :** `EmailMan::sendEmail()`, `EmailTemplateParser`, vues EditView/DetailView, wizard Campagnes
- **Appelle :** Contacts, Accounts, Leads, Prospects, Users, Notes

---

## Notes
- Variables de template : pattern `$module_attribute` (ex: `$contact_first_name`). Prefixes : `contact_` pour Contact/Lead/Prospect, `account_` pour Account, `contact_user_` pour User.
- `$badFields` (ligne 75-105) exclut explicitement des champs sensibles (id, hash, preferences utilisateur).
- `imageLinkReplaced` evite les doubles remplacements de liens d'images inline.
