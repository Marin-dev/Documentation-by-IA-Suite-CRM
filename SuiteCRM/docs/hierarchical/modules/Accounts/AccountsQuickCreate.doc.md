# Fichier : AccountsQuickCreate.php

**Chemin :** `modules/Accounts/AccountsQuickCreate.php`
**Type :** `PHP`
**Categorie :** view (quick create)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere l'affichage du formulaire de creation rapide de compte (Quick Create), accessible depuis les sous-panneaux et le tableau de bord. Adapte les callbacks JavaScript selon le mode (AJAX inline ou standard).

## Role technique

Classe `AccountsQuickCreate` heritant de `QuickCreate`. Surcharge `process()` pour assigner les callbacks JavaScript specifiques au formulaire `accountsQuickCreate` (save/cancel inline via `SUGAR.subpanelUtils`). Genere et injecte le script de validation des champs requis via la classe `javascript`.

---

## Dependances cles

| Dependance | Chemin | Role |
| --- | --- | --- |
| `QuickCreate` | `include/EditView/QuickCreate.php` | Classe parente |
| `javascript` | framework | Generation du script de validation des champs |
| `BeanFactory` | framework | Creation d'un bean Account pour la validation |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AccountsQuickCreate` | classe | Vue Quick Create pour le module Accounts |
| `process($checkFormName, $formName)` | methode | Surcharge : configure le JS AJAX inline save/cancel |

## Relations cles

- **Appele par :** Framework SuiteCRM (via le registre des vues Quick Create du module)
- **Appelle :** `QuickCreate::process()`, `javascript->addAllFields()`
- **Position dans le flux :** rendu du mini-formulaire de creation rapide dans les sous-panneaux

---

## Points d'attention

- En mode AJAX (`$this->viaAJAX`), les callbacks utilisent `SUGAR.subpanelUtils.inlineSave` et `cancelCreate` avec le sous-panneau `subpanel_accounts` code en dur (ligne 63).
- Le nom de formulaire `accountsQuickCreate` est code en dur dans les callbacks JS.
- Globals necessaires : `$current_user`, `$timedate`, `$app_list_strings`, `$current_language`, `$mod_strings`.
