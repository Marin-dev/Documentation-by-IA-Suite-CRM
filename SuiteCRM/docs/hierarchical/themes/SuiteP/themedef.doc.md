# Fichier : themedef.php

**Chemin :** `themes/SuiteP/themedef.php`
**Type :** configuration (theme)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Declare les metadonnees et les options de configuration du theme SuiteP, le theme par defaut de SuiteCRM. Ce fichier est charge par le moteur de themes pour savoir quelles options sont disponibles et configurables pour ce theme.

## Role technique
Expose un tableau PHP `$themedef` contenant le nom, la description, les contraintes de version, et les options configurables (affichage de la barre laterale, sous-theme). Les sous-themes (Dawn, Day, Dusk, Night, Noon) sont peuplees depuis les chaines de traduction `$app_strings` si disponibles.

---

## Dependances cles
- **Imports principaux :**
  - `$app_strings` (global) — chaines de traduction pour les labels des options
- **Variables d'environnement :** aucune
- **Arguments :** aucun (fichier inclus)

## Exports / Symboles principaux
- `$themedef` — tableau (configuration) — descripteur complet du theme SuiteP

## Interactions
- **Appele par :** moteur de themes SuiteCRM (INCONNU : chemin exact non localise ici)
- **Appelle :** rien

---

## Notes
- La garde `sugarEntry` empeche l'acces direct (ligne 41).
- Les 5 sous-themes sont : Dawn (defaut), Day, Dusk, Night, Noon.
- Options configurables : `display_sidebar` (bool), `sub_themes` (select).
- `classic => true` indique compatibilite avec l'ancien mode d'affichage.
- `configurable => true` active le panneau de configuration du theme dans l'admin.
