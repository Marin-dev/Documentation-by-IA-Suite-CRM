# Fichier : TemplateField.php

**Chemin :** `modules/DynamicFields/templates/Fields/TemplateField.php`
**Type :** PHP — Classe de base abstraite (template de champ dynamique)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Classe de base pour tous les types de champs dynamiques. Definit la structure commune : proprietes (nom, type, longueur, valeur par defaut, audit, etc.), la map de correspondance vardef/proprietes, et les methodes de rendu HTML pour les vues edit, detail, list et search.

## Role technique

Classe `TemplateField` definissant le contrat de tous les types de champs. Contient `$vardef_map` qui fait correspondre les noms des colonnes `fields_meta_data` aux proprietes de la classe. Les methodes `get_html()`, `get_html_edit()`, `get_html_detail()`, `get_html_search()`, `get_html_list()` retournent le HTML de rendu. Les methodes `get_xtpl_*()` retournent les valeurs pour injection dans XTemplate. La methode `set($values)` hydrate la classe depuis un tableau. La methode `populateFromPost()` lit les valeurs depuis `$_REQUEST`.

---

## Proprietes principales

| Propriete | Type defaut | Role |
|---|---|---|
| `$view` | `'edit'` | Contexte de rendu : edit, list, detail, search |
| `$name` | `''` | Nom technique du champ |
| `$vname` | `''` | Label (cle de traduction) |
| `$type` | `'varchar'` | Type de champ |
| `$len` | `'255'` | Longueur |
| `$required` | `false` | Obligatoire |
| `$default_value` | `null` | Valeur par defaut |
| `$audited` | `0` | Audit |
| `$inline_edit` | `1` | Edition inline |
| `$massupdate` | `0` | Mise a jour en masse |
| `$reportable` | `true` | Reportable |
| `$unified_search` | `0` | Recherche unifiee |
| `$supports_unified_search` | `false` | Support recherche unifiee (a surcharger) |
| `$ext1`-`$ext4` | `''` | Extensions generiques |
| `$vardef_map` | tableau | Correspondance colonnes DB / proprietes |
| `$decode_from_request_fields_map` | `['formula', 'dependency']` | Champs a decoder depuis POST |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `TemplateField` | classe | Classe de base tous types de champs |
| `get_html()` | methode | Dispatche vers la methode de rendu selon `$this->view` |
| `get_html_edit()` | methode | Rendu champ edition (retourne 'not implemented') |
| `get_html_detail()` | methode | Rendu champ detail (retourne 'not implemented') |
| `set($values)` | methode | Hydratation depuis tableau |
| `populateFromPost()` | methode | Hydratation depuis `$_REQUEST` |
| `save($df)` | methode | Sauvegarde via DynamicField |
| `delete($df)` | methode | Suppression via DynamicField |

---

## Relations cles

- **Etendue par :** `TemplateText`, `TemplateEnum`, `TemplateCurrency`, `TemplateRelatedTextField`, et toutes les autres classes Template*
- **Variable globale** : `$GLOBALS['studioReadOnlyFields']` = `['date_entered', 'date_modified', 'created_by', 'id', 'modified_user_id']` — ces champs sont forces en vue detail meme en mode edit (ligne 44)

---

## Points d'attention

- `get_html_edit()` et `get_html_detail()` retournent `'not implemented'` — toutes les sous-classes doivent surcharger ces methodes.
- `get_html_list()` delegue par defaut a `get_html_detail()`.
- `get_html_search()` delegue par defaut a `get_html_edit()`.
- `$vardef_map` maintient une double entree `default_value`/`default` pour des raisons de coherence historique (bug 15801).
