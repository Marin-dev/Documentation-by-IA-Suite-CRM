# Fichier : FieldViewer.php

**Chemin :** `modules/DynamicFields/FieldViewer.php`
**Type :** PHP — Helper de vue (rendu formulaire Studio)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere le HTML du formulaire de configuration d'un champ dynamique dans Studio. Pour chaque type de champ, retourne le formulaire de parametrage correspondant (options, longueur, valeur par defaut, etc.) affiche lors de la creation ou modification d'un champ custom.

## Role technique

Classe `FieldViewer` utilisant `Sugar_Smarty`. La methode `getLayout($vardef)` dispatche selon `$vardef['type']` vers le template Smarty ou le fichier PHP adequat dans `modules/DynamicFields/templates/Fields/Forms/`. Assigne les variables Smarty (`vardef`, `MOD`, `APP`, `range_search_option_enabled`) avant l'affichage.

---

## Dependances principales

| Import | Role |
|---|---|
| `Sugar_Smarty` | Rendu templates |
| Templates `.tpl` dans `templates/Fields/Forms/` | Formulaires par type |
| Fichiers PHP dans `templates/Fields/Forms/` | Logique PHP pour types complexes (date, enum, etc.) |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `FieldViewer` | classe | Generateur de formulaires Studio |
| `FieldViewer::getLayout($vardef)` | methode | Retourne le HTML du formulaire de configuration pour un type de champ |

## Types de champs geres

address, bool, int, float, decimal, date, datetimecombo/datetime, varchar/char, text, enum, multienum, radioenum, dynamicenum, relate, url, iframe, html, phone, currency, image, encrypt, wysiwyg, parent.

---

## Relations cles

- **Appele par :** Studio (INCONNU exact — probablement `ModuleBuilder` ou vues Studio)
- **Appelle :** templates Smarty `.tpl` et fichiers PHP dans `templates/Fields/Forms/`

---

## Points d'attention

- L'option `range_search_option_enabled` est activee uniquement si `$_REQUEST['view_package']` est vide (= en Studio, pas en ModuleBuilder), ligne 61.
- Les types `datetimecombo` et `datetime` partagent le meme formulaire.
- Le type `varchar` par defaut si `$vardef['type']` est vide (ligne 53).
