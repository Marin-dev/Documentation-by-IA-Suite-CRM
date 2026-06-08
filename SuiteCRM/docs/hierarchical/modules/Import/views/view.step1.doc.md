# view.step1.php

**Chemin :** `modules/Import/views/view.step1.php`
**Type :** PHP - Vue (étape 1 d'import)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Vue de la première étape du wizard d'import. Permet à l'utilisateur de sélectionner le module cible et la source de données (upload fichier ou source externe comme Google). Initialise le processus d'import.

## Type
view

## Dépendances clés
- `modules/Import/views/ImportView.php` — classe parente
- `include/externalAPI/ExternalAPIFactory.php` — sources externes (Google EAPM)
- `modules/Import/Importer.php` — orchestrateur d'import

## Exports / Symboles principaux
- `ImportViewStep1` (classe, étend `ImportView`)
  - `$pageTitleKey` = `'LBL_STEP_1_TITLE'`
  - `$importModule` — module cible d'import
  - `$currentStep` — calculé depuis `$_REQUEST['current_step']`

## Interactions
- **Appelé par :** URL `?module=Import&action=Step1` ou wizard d'import
- **Appelle :** `ExternalAPIFactory`, `Importer`

## Notes
- Gère le cas spécial `from_admin_wizard` (import depuis l'assistant d'administration).
