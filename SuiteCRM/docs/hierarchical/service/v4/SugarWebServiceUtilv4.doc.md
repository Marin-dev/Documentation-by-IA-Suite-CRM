# SugarWebServiceUtilv4.php

**Chemin :** `service/v4/SugarWebServiceUtilv4.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Helper utilitaire pour la v4 de l'API. Étend `SugarWebServiceUtilv3_1` et ajoute `get_module_view_defs()` pour récupérer les définitions de vues (formulaires, listes) d'un module.

**Type :** helper

---

## Dépendances clés
- `service/v3_1/SugarWebServiceUtilv3_1.php` — classe parente
- `include/MVC/View/SugarView.php` — chargement des métadonnées de vues

---

## Exports/Symboles principaux
- `SugarWebServiceUtilv4` — (étend `SugarWebServiceUtilv3_1`)
  - `get_module_view_defs($moduleName, $type, $view)` — charge les viewdefs d'un module (EditView, DetailView, ListView, etc.)

---

## Interactions
- **Injecté dans :** `SugarWebServiceImplv4::$helperObject`
- **Étendu par :** `SugarWebServiceUtilv4_1`
