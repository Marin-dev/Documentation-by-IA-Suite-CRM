# EmailTemplate.php

**Chemin :** `modules/EmailTemplates/EmailTemplate.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle principal des gabarits email. Stocke le sujet, le corps HTML et texte, les pièces jointes et les métadonnées d'un template email réutilisable pour les campagnes et les emails manuels.

## Type

model

---

## Dépendances clés

- `SugarBean` (classe parente)
- `BeanFactory` — instanciation Contacts, Accounts, Leads, Prospects, Users, FP_events
- `LoggerManager`
- `$sugar_config['default_charset']`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `EmailTemplate` | classe | Entité gabarit email (table `email_templates`) |
| `generateFieldDefsJS()` | méthode | Génère le JavaScript des définitions de champs pour l'éditeur de macros (Contacts, Accounts, Users) |
| `generateFieldDefsJS2()` | méthode | Version étendue incluant les Events (FP_events) |
| `fill_in_additional_detail_fields()` | méthode | Nettoie et prépare le corps HTML pour l'affichage |
| `parse_tracker_urls()` | méthode | Remplace les URLs tracker dans le corps du template |
| `badFields` | propriété | Liste des champs exclus des macros de template |

## Interactions

- **Appelé par :** `EmailMan::sendEmail()`, `EmailTemplateParser`, `EmailMarketing`, vues EmailTemplates
- **Appelle :** BeanFactory (Contacts, Accounts, Leads, Prospects, Users, FP_events)

## Notes

- `badFields` exclut des champs sensibles (user_hash, is_admin, etc.) des macros disponibles dans les templates.
- `generateFieldDefsJS()` et `generateFieldDefsJS2()` construisent la liste des variables disponibles pour l'éditeur de template.
- Supporte le flag `text_only` pour les templates sans HTML.
