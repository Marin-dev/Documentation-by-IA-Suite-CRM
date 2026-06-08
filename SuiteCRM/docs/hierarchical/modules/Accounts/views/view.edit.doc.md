# Fichier : view.edit.php

**Chemin :** `modules/Accounts/views/view.edit.php`
**Type :** `PHP`
**Categorie :** view (edition)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Vue d'edition d'un compte. Active le mode sous-panneau et le template Quick Create pour permettre la creation et l'edition inline depuis d'autres modules.

## Role technique

Classe `AccountsViewEdit` heritant de `ViewEdit`. Constructeur uniquement : positionne `$this->useForSubpanel = true` et `$this->useModuleQuickCreateTemplate = true`. Aucune logique specifique supplementaire.

---

## Dependances cles

| Dependance | Role |
| --- | --- |
| `ViewEdit` | Classe parente (framework) |

## Exports / Symboles principaux

| Symbole | Type | Role |
| --- | --- | --- |
| `AccountsViewEdit` | classe | Vue edition Account |

## Relations cles

- **Appele par :** Framework SuiteCRM (routing action=EditView, module=Accounts)
- **Position dans le flux :** formulaire de creation/modification d'un compte

---

## Points d'attention

- Classe tres legere : toute la logique est dans `ViewEdit` du framework.
- `useForSubpanel = true` permet l'utilisation de ce formulaire depuis les sous-panneaux d'autres modules.
- `useModuleQuickCreateTemplate = true` active le template Quick Create du module.
