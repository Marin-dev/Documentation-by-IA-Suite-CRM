# Fichier : view.detail.php (Contacts)

**Chemin :** `modules/Contacts/views/view.detail.php`
**Type :** PHP - Vue (detail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue detail standard pour le module Contacts. Controle l'affichage des champs portail (AOP) selon la configuration, active le popup de publipostage PDF, et verifie si le portail global est actif.

## Role technique

Etend `ViewDetail`. Override `display()` pour : verifier la configuration AOP (`enable_portal`, `enable_aop`), assigner `AOP_PORTAL_ENABLED` au template Smarty, initialiser `formLetter::DVPopupHtml()` pour le PDF, et verifier `Administration::portal_on`.

---

## Dependances cles

- `ViewDetail` — classe parente
- `modules/AOS_PDF_Templates/formLetter.php` — popup PDF
- `BeanFactory::newBean('Administration')` — lecture de la config portail
- `$sugar_config['aop']` — configuration AOP

## Exports / Symboles principaux

- `ContactsViewDetail` — classe
  - `display()` — affichage conditionnel des champs portail et initialisation PDF (l.56)

## Consommateurs identifies

- Framework MVC SuiteCRM (charge pour `action=DetailView` du module Contacts)

## Relations cles

- **Appelle :** `formLetter::DVPopupHtml('Contacts')`, `Administration->retrieveSettings()`
- **Position dans le flux :** Affichage principal d'un contact

---

## Points d'attention

- Les champs portail ne s'affichent que si `AOP_PORTAL_ENABLED = true` ET `PORTAL_ENABLED = true` — double condition.
- `formLetter::DVPopupHtml` ajoute le bouton de publipostage PDF en JavaScript.
