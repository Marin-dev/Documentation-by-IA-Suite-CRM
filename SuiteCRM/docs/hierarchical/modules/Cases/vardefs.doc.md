# vardefs.php

**Chemin :** `modules/Cases/vardefs.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Definit le schema du bean Case : champs, relations, index et options de la table `cases`. Fichier de reference structurelle pour l'ORM SuiteCRM.

## Type
config / schema

## Dependances cles
- `VardefManager::createVardef()` — injection des groupes : `default`, `assignable`, `security_groups`, `issue`
- Table DB : `cases`
- Modules lies : `Accounts`, `Contacts`, `Users`, `Bugs`, `Tasks`, `Notes`, `Meetings`, `Calls`, `Emails`, `Documents`

## Exports / Symboles principaux
- `$dictionary['Case']` — definition complete du bean
- `audited = true`, `unified_search = true`, `full_text_search = true`, `duplicate_merge = true`
- Champs specifiques : `account_name` (relate), `suggestion_box`, `description` (html editor), `case_number`, `status`, `priority`, `resolution`

## Interactions
- **Appelle :** `VardefManager::createVardef('Cases', 'Case', [...])`
- **Appele par :** framework SuiteCRM au chargement du module

## Notes
- `full_text_search = true` : ce module supporte la recherche plein texte.
- `unified_search_default_enabled = true` : actif par defaut dans la recherche globale.
- Supporte les groupes de securite via `security_groups`.
