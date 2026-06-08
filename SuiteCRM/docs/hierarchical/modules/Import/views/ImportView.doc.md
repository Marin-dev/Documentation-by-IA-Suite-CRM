# ImportView.php

**Chemin :** `modules/Import/views/ImportView.php`
**Type :** PHP - Vue (classe de base)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe de base pour toutes les vues du module Import. Étend `SugarView` et gère la navigation entre les étapes d'import (bouton "Retour"), le titre de page et les instructions. Toutes les vues step1-step4, confirm, error, etc. héritent de cette classe.

## Type
view (base)

## Dépendances clés
- `include/MVC/View/SugarView.php` — classe parente
- `$mod_strings` — traductions du module Import

## Exports / Symboles principaux
- `ImportView` (classe, étend `SugarView`)
  - `$currentStep` — étape courante du wizard
  - `$pageTitleKey` — clé de traduction pour le titre
  - `$instruction` — texte d'instruction affiché
  - Constructeur : gère le bouton "Retour" (redirection vers l'étape précédente)

## Interactions
- **Appelé par :** toutes les vues Import (`view.step1` à `view.step4`, `view.confirm`, `view.error`, `view.dupcheck`, etc.)
- **Appelle :** `SugarView`

## Notes
- La gestion du bouton "Retour" est faite dans le constructeur (ligne 60) via comparaison avec `htmlentities($mod_strings['LBL_BACK'])`.
