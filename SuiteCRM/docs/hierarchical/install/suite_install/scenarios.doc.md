# Fichier : scenarios.php

**Chemin :** `install/suite_install/scenarios.php`
**Type :** configuration (scenarios d'installation)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel
Definit les scenarios predetermines proposes a l'utilisateur pendant l'installation pour preconfigurer SuiteCRM selon son usage metier (Sales, Marketing, Finance, etc.). Chaque scenario active un sous-ensemble de modules et de dashlets.

## Role technique
Peuple le tableau `$installation_scenarios` avec des structures decrivant chaque scenario : cle, titre (traduit via `$app_strings`), description, onglets actives, modules inclus et dashlets configures.

---

## Dependances cles
- **Imports principaux :**
  - `$app_strings` (global) — chaines de traduction pour les titres/descriptions
  - `return_application_language($current_language)` — si `$app_strings` est null

## Exports / Symboles principaux
- `$installation_scenarios` — tableau — liste des scenarios avec structure :
  - `key` — identifiant
  - `title` — titre traduit
  - `description` — description traduite
  - `groupedTabs` — cle groupe d'onglets
  - `modules` — modules a activer
  - `modulesScenarioDisplayName` — noms affichables des modules
  - `dashlets` — dashlets a configurer

**Scenarios definis (partiels) :**
- `Sales` — Opportunities + Leads
- `Marketing` — Prospects, ProspectLists, Campaigns, FP_events, FP_Event_Locations
- `Finance` — (contenu non lu entierement)

## Interactions
- **Appele par :**
  - `install/installConfig.php` (ligne 1643)
  - `install.php` (INCONNU : verification)
- **Appelle :** rien

---

## Notes
- Les labels sont extraits de `$app_strings` — la traduction depend de la langue selectionnee.
- Les scenarios sont presentes comme checkboxes dans `installConfig.php` (selectionnes par defaut).
- INCONNU : combien de scenarios au total (liste non completement lue).
