# Step3.php

**Chemin :** `modules/MailMerge/Step3.php`
**Type :** PHP - Vue (étape 3 de la fusion)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Troisième étape du wizard de fusion de courrier. Charge les modules supportés et les requêtes de fusion pour afficher les enregistrements disponibles.

## Type
view

## Dépendances clés
- `include/JSON.php`
- `modules/MailMerge/modules_array.php` — liste des modules
- `modules/MailMerge/merge_query.php` — requêtes SQL
- `$app_strings`, `$app_list_strings`

## Exports / Symboles principaux
Aucune classe. Script procédural.

## Interactions
- **Appelé par :** `index.php` (dispatch par `$_REQUEST['step']`)
- **Appelle :** `modules_array.php`, `merge_query.php`
