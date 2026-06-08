# view.edit.php

**Chemin :** `modules/Contacts/views/view.edit.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue édition personnalisée du module Contacts. Masque le panneau "Portal Information" si le portail n'est pas activé. En mode duplication, réinitialise les champs portail. Injecte la validation JavaScript du nom d'utilisateur portail.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `ViewEdit` (extend) | Vue édition de base SuiteCRM |
| `BeanFactory::newBean('Administration')` | Vérification paramètre `portal_on` |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ContactsViewEdit` | classe | Vue édition custom Contacts |

---

## Interactions

- **Appelé par :** Framework MVC (action=EditView)
- **Appelle :** `Contact.js` (validation portail)

---

## Points d'attention

- Si `isDuplicate=true`, les champs portail sont réinitialisés (ligne 76-84) — un contact dupliqué ne copie pas ses credentials portail.
- Utilise `$this->useForSubpanel = true` et `$this->useModuleQuickCreateTemplate = true` pour activer la création rapide depuis sous-panneau.
