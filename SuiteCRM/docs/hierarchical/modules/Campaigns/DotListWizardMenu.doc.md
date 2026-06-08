# DotListWizardMenu.php

**Chemin :** `modules/Campaigns/DotListWizardMenu.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Composant d'interface pour le menu de navigation étape-par-étape (wizard) des campagnes. Génère le HTML de la barre de progression (liste `<ul class="progression">`) utilisée dans les wizards de création/édition de campagne. Peut optionnellement activer les liens de navigation vers les étapes.

**Type :** helper / composant UI

---

## Dépendances clés

- `modules/Campaigns/tpls/progressStepsStyle.html` (chargé avec `file_get_contents`)

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `DotListWizardMenu` | classe | Génère le HTML de la barre de progression du wizard |
| `__construct($mod_strings, $steps, $showLinks)` | méthode | Construit le HTML à partir des étapes passées ; `$showLinks` active les liens |
| `__toString()` | méthode | Retourne le HTML généré, utilisable directement dans `echo` |
| `getWizardMenuItemHTML($i, $label, $link)` | méthode privée | Génère le HTML d'un item de navigation |
| `getWizardMenuHTML($innerHTML)` | méthode privée | Enveloppe les items dans le container HTML de progression |

---

## Interactions

**Appelle :**
- `file_get_contents()` pour charger `tpls/progressStepsStyle.html`

**Appelée par :** INCONNU — probablement utilisée dans les wizards `WizardNewsletter.php`, `WizardMarketing.php` et similaires.

**Position dans le flux global :** Composant d'affichage dans les wizards de campagne.

---

## Notes

- Les étapes numérotées >= 4 ne reçoivent un lien que si `marketing_id` est présent dans les paramètres de l'URL (ligne 27-29) — comportement lié au wizard de marketing.
- `__toString()` permet d'utiliser l'objet directement dans les templates : `echo new DotListWizardMenu(...)`.
