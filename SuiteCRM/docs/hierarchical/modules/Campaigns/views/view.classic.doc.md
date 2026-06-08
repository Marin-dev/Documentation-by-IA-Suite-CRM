# view.classic.php

**Chemin :** `modules/Campaigns/views/view.classic.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Vue "classique" du module Campaigns utilisée pour inclure les fichiers PHP legacy (wizard, diagnostics, etc.) dans le contexte MVC SuiteCRM. Sert de pont entre l'ancien système d'affichage et le framework MVC.

## Type

`view`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `SugarView` (extend) | Vue de base SuiteCRM |
| `include/MVC/View/SugarView.php` | Inclusion explicite |
| `SugarController::getActionFilename()` | Résolution du nom de fichier action |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `CampaignsViewClassic` | classe | Vue classique générique du module |

---

## Interactions

- **Appelé par :** Actions wizard (WizardHome, WizardMarketing, CampaignDiagnostic, etc.)
- **Appelle :** Fichiers PHP action du module (ex. `WizardHome.php`)

---

## Points d'attention

- Cherche d'abord dans `custom/modules/Campaigns/` avant `modules/Campaigns/` — surcharge possible sans modifier le core.
- `_getModuleTitleParams()` fournit les titres de page pour chaque action wizard.
