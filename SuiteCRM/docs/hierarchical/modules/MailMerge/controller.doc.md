# controller.php

**Chemin :** `modules/MailMerge/controller.php`
**Type :** PHP - Controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Contrôleur du module MailMerge. Gère les actions AJAX pour la recherche de templates et d'enregistrements CRM, en liaison avec les fonctions SOAP helper.

## Type
controller

## Dépendances clés
- `soap/SoapHelperFunctions.php` — fonctions helpers SOAP
- `SugarController` — classe parente
- `$beanList`, `$_REQUEST['qModule']`

## Exports / Symboles principaux
- `MailMergeController` (classe, étend `SugarController`)
  - `action_search()` — recherche AJAX de beans CRM (view = 'ajax')

## Interactions
- **Appelé par :** framework SugarCRM (dispatcher d'actions)
- **Appelle :** `SoapHelperFunctions`

## Notes
- Utilise `$this->view = 'ajax'` pour les réponses AJAX.
