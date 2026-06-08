# Bug.php

**Chemin :** `modules/Bugs/Bug.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal du module Bugs (signalements de defauts). Represente un bug/defaut remonte par un client ou une equipe interne, avec suivi de statut, priorite, type, version concernee et version de correction.

## Type
model

## Dependances cles
- `SugarBean` (heritage) — classe de base ORM SuiteCRM
- `BeanFactory` — instanciation des beans lies (Releases, Bugs)
- `VardefManager::createVardef` (dans vardefs.php) — injection des champs standards
- Table DB : `bugs`, relations : `accounts_bugs`, `contacts_bugs`, `cases_bugs`
- `releases` (table) — pour `found_in_release` et `fixed_in_release`

## Exports / Symboles principaux
- `class Bug extends SugarBean` — modele principal
- `getReleaseDropDown()` — fonction globale, retourne la liste des releases actives pour les dropdowns
- Methodes : `get_summary_text()`, `create_list_query()`, `create_export_query()`, `fill_in_additional_detail_fields()`, `set_release()`, `set_fixed_in_release()`, `get_list_view_data()`, `build_generic_where_clause()`, `set_notification_body()`, `bean_implements()`, `save()`

## Interactions
- **Appelle :** `BeanFactory::newBean('Releases')`, `parent::save()`, `$this->db->query()`, `return_app_list_strings_language()`, `return_module_language()`
- **Appele par :** framework SuiteCRM (BeanFactory, vues detail/edit/list), `BugsQuickCreate`, `MyBugsDashlet`
- **Implements ACL :** `bean_implements('ACL')` retourne true

## Notes
- Champ `bug_number` indexe separement (autoincrement gere par SugarBean).
- `set_release()` et `set_fixed_in_release()` utilisent un cache statique `$releases` pour eviter les requetes repetees.
- `importable = true` : le module supporte l'import CSV.
- Supporte `security_groups` via VardefManager (ligne 358).
