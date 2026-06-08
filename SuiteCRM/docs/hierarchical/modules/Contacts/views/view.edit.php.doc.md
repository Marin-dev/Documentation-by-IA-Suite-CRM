# Fichier : view.edit.php (Contacts)

**Chemin :** `modules/Contacts/views/view.edit.php`
**Type :** PHP - Vue (edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Surcharge la vue edition standard pour le module Contacts. Masque le panel "Informations Portail" si le portail n'est pas active. Active la compatibilite avec les sous-panels et la creation rapide.

## Role technique

Etend `ViewEdit`. Active `useForSubpanel = true` et `useModuleQuickCreateTemplate = true`. Override `display()` pour masquer conditionnellement le panel portail selon la configuration AOP.

---

## Dependances cles

- `ViewEdit` — classe parente
- `BeanFactory::newBean('Administration')` — lecture config portail (probable)
- `$sugar_config['aop']` — configuration AOP

## Exports / Symboles principaux

- `ContactsViewEdit` — classe
  - `display()` — masque le panel portail si non configure (l.59+)

## Consommateurs identifies

- Framework MVC SuiteCRM (charge pour `action=EditView` du module Contacts)

## Relations cles

- **Position dans le flux :** Formulaire d'edition/creation d'un contact

---

## Points d'attention

- `useModuleQuickCreateTemplate = true` — permet l'utilisation du template de creation rapide.
- Le panel portail est conditionnel — ne pas oublier d'activer AOP pour acceder a ces champs.
