# sitemap.php

**Chemin :** `modules/Home/sitemap.php`
**Type :** PHP - Vue
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Génère et affiche le plan du site (sitemap) de SuiteCRM en popup. Parcourt tous les modules accessibles à l'utilisateur et construit un tableau de liens par module à partir de leurs fichiers `Menu.php`. Le résultat est rendu via un template Smarty (`sitemap.tpl`).

## Type
view

## Dépendances clés
- `include/utils.php` — utilitaires généraux
- `include/modules.php` — liste des modules
- `Sugar_Smarty` — moteur de templates
- `query_module_access_list()` — liste des modules accessibles à l'utilisateur
- `$_SESSION['SM_ARRAY']` — cache de la structure du sitemap

## Exports / Symboles principaux
- `sm_build_array()` (fonction locale) — construit le tableau associatif `module => liens` en itérant sur les `Menu.php` de chaque module. Met le résultat en cache dans `$_SESSION['SM_ARRAY']`.

## Interactions
- **Appelé par :** action `sitemap` du module Home (URL `?module=Home&action=sitemap`)
- **Appelle :** `Menu.php` de chaque module, `return_module_language()`, `return_app_list_strings_language()`

## Notes
- Supporte un template custom via `custom/modules/Home/sitemap.tpl`.
- La liste des modules est filtrée par les droits de l'utilisateur via `query_module_access_list()`.
- La session est utilisée comme cache pour éviter de recharger tous les menus à chaque appel.
