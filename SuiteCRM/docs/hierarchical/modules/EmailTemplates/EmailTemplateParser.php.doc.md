# EmailTemplateParser.php

**Chemin :** `modules/EmailTemplates/EmailTemplateParser.php`
**Type :** helper

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Parseur de gabarits email. Substitue les variables `$module_field` dans le sujet et le corps du template par les valeurs réelles du bean destinataire (contact, lead, compte…) au moment de l'envoi d'une campagne.

## Type

helper

---

## Dépendances clés

- `EmailTemplate` — template à parser
- `Campaign` — contexte de la campagne
- Objet module destinataire (Contact, Lead, Prospect, Account) — implémentant `EmailInterface`
- `$sugar_config['site_url']` — URL du site pour les liens
- `SuiteValidator` (`SuiteCRM\Utility\SuiteValidator`)

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailTemplateParser` | classe | Parseur de variables dans les templates email |
| `PATTERN` | constante | Regex de détection des variables `$module_field` |
| `parseVariables()` | méthode | Retourne un tableau `[subject, body_html, body]` avec variables remplacées |
| `$allowedAttributes` | statique | Attributs traités : `subject`, `body_html`, `body` |
| `$allowedVariables` | statique | Variables non-DB autorisées : `survey_url_display` |

## Interactions

- **Appelé par :** `EmailMan::sendEmail()` (ligne 1060)
- **Appelle :** bean destinataire (lecture des champs)

## Notes

- Pattern de variables : `$module_field` (ex. `$contact_first_name`, `$account_name`).
- Les variables non reconnues sont laissées telles quelles ou supprimées selon la configuration.
- `survey_url_display` est une variable spéciale non-DB autorisée explicitement.
