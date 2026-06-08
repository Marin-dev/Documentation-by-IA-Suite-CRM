# editviewdefs.php

**Chemin :** `modules/Campaigns/metadata/editviewdefs.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Définit la disposition des champs dans la vue édition du module Campaigns. Note : la vue EditView est redirigée vers WizardHome par le contrôleur — ces defs sont utilisées par le wizard.

## Type

`config` (métadonnées vue)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$viewdefs['Campaigns']['EditView']` | tableau | Disposition champs en vue édition |

---

## Interactions

- **Consommé par :** Framework SuiteCRM, wizard

---

## Points d'attention

- L'action `EditView` est redirigée vers `WizardHome` (voir `controller.php`) — ces defs ont un usage limité.
