# controller.php

**Chemin :** `modules/Home/controller.php`
**Type :** PHP - Controller
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Contrôleur principal du module Home. Gère les actions AJAX liées à l'édition en ligne (inline editing) de champs : récupération du HTML d'un champ éditable, sauvegarde d'une valeur, récupération de la valeur affichée et des règles de validation, génération du JS QuickSearch pour les champs relate.

## Type
controller

## Dépendances clés
- `include/InlineEditing/InlineEditing.php` — fonctions `getEditFieldHTML`, `saveField`, `getDisplayValue`
- `BeanFactory` (global) — chargement des beans par module/id
- `include/TemplateHandler/TemplateHandler.php` — génération du code QuickSearch JS
- `SugarController` (classe parente)
- `$beanFiles`, `$beanList` (globaux)

## Exports / Symboles principaux
- `HomeController` (classe) — étend `SugarController`
  - `action_getEditFieldHTML()` — renvoie le HTML du champ en mode édition (AJAX)
  - `action_saveHTMLField()` — sauvegarde la valeur d'un champ (AJAX)
  - `action_getDisplayValue()` — renvoie la valeur affichée après save (AJAX)
  - `action_getValidationRules()` — renvoie JSON avec type, required, label du champ
  - `action_getRelateFieldJS()` — génère le JS QuickSearch pour un champ relate

## Interactions
- **Appelé par :** framework SuiteCRM (dispatcher d'actions via URL `?module=Home&action=*`)
- **Appelle :** `InlineEditing.php`, `TemplateHandler`, `BeanFactory`

## Notes
- Toutes les actions lisent `$_REQUEST` directement — pas de validation explicite des entrées côté serveur au-delà de la vérification de présence.
- `action_getValidationRules` gère un cas spécial pour `email1`/`email2` (type forcé à "email").
