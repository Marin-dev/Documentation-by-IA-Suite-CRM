# EmailTemplateParser.php

**Chemin :** `modules/EmailTemplates/EmailTemplateParser.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe de parsing des variables dans les templates email de campagne. Remplace les tokens `$module_attribut` dans le sujet, le corps HTML et le corps texte d'un template en lisant les proprietes du bean cible (Contact, Lead, Prospect, Account, User).

**Type :** helper / service

---

## Dependances cles
- `EmailTemplate` (template a parser)
- `Campaign` (campagne courante)
- `EmailInterface` (bean destinataire : Contact, Lead, Prospect...)
- `BeanFactory::getBean('Surveys')` (pour la variable `survey_url_display`)
- `$app_list_strings` (traduction des champs enum)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `EmailTemplateParser` | classe | Parseur de variables de template |
| `PATTERN` | constante | Regex de detection des variables (`/\$([a-zA-Z_\x7f-\xff]+_[a-zA-Z0-9_\x7f-\xff]*)/`) |
| `parseVariables()` | methode publique | Retourne `['subject', 'body_html', 'body']` avec variables remplacees |
| `getSurvey()` | methode | Lazy-load de l'objet Survey lie a la campagne |

---

## Interactions
- **Appele par :** `EmailMan::sendEmail()` (ligne 1060)
- **Appelle :** `EmailTemplate`, `Campaign`, bean destinataire, `BeanFactory::getBean('Surveys')`

---

## Notes
- Variables non reconnues (attribut inexistant sur le bean) sont remplacees par `''` avec warning dans les logs (ligne 207-213).
- Schema de nommage special : `$contact_*` pointe vers Lead/Prospect si le bean est un Lead/Prospect ; `$contact_user_*` pour User.
- `$allowedVariables` = `['survey_url_display']` : seule variable non-DB autorisee.
