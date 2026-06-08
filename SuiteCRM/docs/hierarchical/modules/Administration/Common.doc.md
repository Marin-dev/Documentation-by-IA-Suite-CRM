# Common.php

**Chemin :** `modules/Administration/Common.php`
**Type :** PHP (helper / utilitaires)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bibliotheque de fonctions utilitaires pour la gestion des packs de langue et des listes deroulantes personnalisees. Permet de creer, modifier, supprimer, deplacer et sauvegarder des entrees dans les fichiers de langue PHP (`app_list_strings`, `mod_strings`) du repertoire `custom/`.

## Role technique
Ensemble de fonctions procedurales. Lit/ecrit les fichiers `custom/include/language/{lang}.lang.php` et `custom/modules/{module}/language/{lang}.lang.php`. Utilise des regex pour remplacer ou inserer les entrees dans le contenu PHP existant. Invalide le cache `app_list_strings.{lang}` apres chaque modification.

---

## Dependances cles
| Import | Role |
|---|---|
| `include/utils/array_utils.php` | `override_value_to_string()` pour serialisation PHP |
| `return_module_language()` | Chargement pack langue module |
| `return_app_list_strings_language()` | Chargement listes deroulantes |
| `sugar_cache_clear()` | Invalidation cache apres ecriture |
| `LoggerManager::getLogger()` | Journalisation |

## Symboles principaux

| Fonction | Role |
|---|---|
| `create_include_lang_dir()` | Cree `custom/include/language/` si absent |
| `create_module_lang_dir($module)` | Cree `custom/modules/$module/language/` si absent |
| `create_field_label($module, $language, $key, $value)` | Ajoute/remplace un label dans le pack module |
| `create_field_label_all_lang($module, $key, $value)` | Meme chose pour toutes les langues |
| `save_custom_app_list_strings(&$app_list_strings, $language)` | Sauvegarde une liste deroulante complete |
| `save_custom_app_list_strings_contents(&$contents, $language)` | Sauvegarde le contenu brut du fichier lang |
| `dropdown_item_delete()` | Supprime un item d'une liste |
| `dropdown_item_move_up()` / `dropdown_item_move_down()` | Reordonne les items |
| `dropdown_item_insert()` | Insere un item a une position |
| `dropdown_item_edit()` | Modifie la valeur d'un item |
| `replace_or_add_dropdown_type()` | Remplace ou ajoute une liste dans le fichier |
| `replace_or_add_app_string()` | Remplace ou ajoute une chaine app_strings |
| `dropdown_duplicate_check()` | Supprime les doublons dans le fichier PHP |
| `create_dropdown_html()` | Genere le HTML d'un `<select>` |

## Interactions
- **Appele par :** Module Studio, Dropdown Editor, outils de personnalisation
- **Ecrit dans :** `custom/include/language/*.lang.php`, `custom/modules/*/language/*.lang.php`

---

## Notes
- La fonction `create_field_lang_pak_contents()` utilise un regex pour remplacer une cle existante avant d'en ajouter une nouvelle — risque de faux positifs sur des cles similaires (vigilance sur les noms de cles).
- `dropdown_duplicate_check()` nettoie les entrees dupliquees mais ne conserve que la premiere occurrence.
- Toutes les fonctions invalident le cache apres ecriture pour eviter des incoherences.
