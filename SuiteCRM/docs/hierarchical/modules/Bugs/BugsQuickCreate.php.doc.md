# 📄 BugsQuickCreate.php

**Chemin :** `modules/Bugs/BugsQuickCreate.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Fournit le formulaire de création rapide d'un bug, accessible depuis les sous-panneaux d'autres modules (ex : Cases, Contacts). Permet de créer un bug sans naviguer vers le module Bugs.

## Rôle technique

Classe `BugsQuickCreate` héritant de `QuickCreate` (`include/EditView/QuickCreate.php`). Surcharge la méthode `process()` pour peupler les listes déroulantes de priorité, statut et type, et générer le JavaScript de validation du formulaire via la classe `javascript`.

---

## Dépendances clés

- `include/EditView/QuickCreate.php` — classe parente (require_once)
- `BeanFactory::newBean('Bugs')` — instanciation pour la validation JS
- `javascript` (classe SuiteCRM) — génération des scripts de validation
- `$app_list_strings` — listes déroulantes (`bug_priority_dom`, `bug_status_dom`, `bug_type_dom`)
- `Sugar_Smarty` (`$this->ss`) — assignation des variables template

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `BugsQuickCreate` | classe | Formulaire de création rapide de bug |
| `process()` | méthode | Prépare le template Smarty avec les options de formulaire |

## Consommateurs identifiés

- Framework SugarCRM (chargement automatique via le nom du module + `QuickCreate`)

---

## Relations clés

- **Appelé par :** framework MVC SugarCRM (action QuickCreate)
- **Appelle :** `QuickCreate::process()`, `BeanFactory::newBean('Bugs')`, `javascript`
- **Position dans le flux global :** formulaire inline dans les sous-panneaux, soumission via AJAX (`SUGAR.subpanelUtils.inlineSave`)

---

## Notes

- Support AJAX natif : si `$this->viaAJAX`, les callbacks `saveOnclick`/`cancelOnclick` sont surchargés (ligne 65-68).
- Le nom du formulaire HTML est `bugsQuickCreate` (cohérence requise avec les templates Smarty).
