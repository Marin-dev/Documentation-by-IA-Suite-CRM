# EmployeesStudioModule.php

**Chemin :** `modules/Employees/EmployeesStudioModule.php`
**Type :** PHP - Modèle (module Studio)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe Studio spécialisée pour le module Employees. Désactive la création de relations avec d'autres modules (sous-panneaux) et supprime l'onglet "Relationships" dans Studio, car les employés ne doivent pas être reliés à d'autres modules.

## Type
model

## Dépendances clés
- `modules/ModuleBuilder/Module/StudioModule.php` — classe parente

## Exports / Symboles principaux
- `EmployeesStudioModule` (classe, étend `StudioModule`)
  - `getProvidedSubpanels()` — retourne `false` (aucun sous-panneau fourni)
  - `getModule()` — supprime l'onglet "Relationships" de la liste des modules Studio

## Interactions
- **Appelé par :** Studio (ModuleBuilder) lors de la gestion du module Employees
- **Appelle :** `StudioModule::getModule()`, `translate('LBL_RELATIONSHIPS')`

## Notes
- Commentaire en code : "Much like pointy haired bosses, other modules should not be able to relate to Employees."
- Particularité métier : les employés sont des utilisateurs, pas des entités CRM relationnelles.
