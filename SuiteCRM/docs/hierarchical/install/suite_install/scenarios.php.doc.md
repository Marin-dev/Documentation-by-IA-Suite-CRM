# scenarios.php

**Chemin :** `install/suite_install/scenarios.php`
**Type :** `PHP (configuration — scénarios d'installation)`
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit les scénarios d'installation disponibles dans le wizard SuiteCRM. Chaque scénario active un sous-ensemble de modules et de dashlets adaptés à un usage métier (Sales, Marketing, Finance, etc.). L'utilisateur peut cocher/décocher les scénarios lors de l'installation.

**Type :** config / installer

---

## Dépendances clés
- `$app_strings` — chaînes de traduction pour les titres et descriptions des scénarios
- `return_application_language()` — chargement des chaînes si `$app_strings` est null

## Exports / Symboles principaux
- `$installation_scenarios` — tableau indexé de scénarios, chaque entrée contenant :
  - `key` — identifiant (ex: `'Sales'`, `'Marketing'`, `'Finance'`)
  - `title` — titre localisé
  - `description` — description localisée
  - `groupedTabs` — groupe d'onglets associé
  - `modules` — liste des modules à activer
  - `modulesScenarioDisplayName` — noms affichés des modules
  - `dashlets` — liste des dashlets associés

Scénarios identifiés (partiels, fichier tronqué à 60 lignes) :
- `Sales` : Opportunities, Leads → dashlets MyOpportunities, MyLeads
- `Marketing` : Prospects, ProspectLists, Campaigns, FP_events, FP_Event_Locations
- `Finance` : (modules non lus)

## Interactions
- **Appelé par :**
  - `install/installConfig.php` (ligne 1643)
  - `install/siteConfig_a.php` (ligne 1643 — même logique)
- **Appelle :** `return_application_language()` si nécessaire
- **Position dans le flux global :** configuration des modules activés selon le profil d'utilisation choisi par l'administrateur

---

## Notes
- Scénarios utilisés pour pré-cocher des modules dans la vue `installConfig.php` (section "Choose Scenarios").
- L'admin peut décocher des scénarios avant l'installation pour alléger l'interface.
- Dépend de `$app_strings` avec clés `LBL_SCENARIO_*` (défini dans les fichiers de langue application).
