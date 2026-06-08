# view.detail.php

**Chemin :** `modules/Contacts/views/view.detail.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue détail personnalisée du module Contacts. Surcharge la vue détail standard pour : gérer l'affichage conditionnel du portail AOP, injecter le popup de lettre PDF (formLetter), et afficher les champs portail selon la configuration admin.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewDetail` (extend) | Vue détail de base SuiteCRM |
| `modules/AOS_PDF_Templates/formLetter.php` | Popup lettre PDF |
| `BeanFactory::newBean('Administration')` | Vérification paramètre `portal_on` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewDetail` | classe | Vue détail custom Contacts |

---

## Interactions

- **Appelé par :** Framework MVC (action=DetailView)
- **Appelle :** `formLetter::DVPopupHtml()`, admin settings

---

## Points d'attention

- `AOP_PORTAL_ENABLED` est assigné à Smarty — contrôle l'affichage des actions portail dans le template.
- Vérifie deux flags distincts : `enable_portal` et `enable_aop`.
