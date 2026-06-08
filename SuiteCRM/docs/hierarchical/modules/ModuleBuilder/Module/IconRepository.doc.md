# IconRepository.php

**Chemin :** `modules/ModuleBuilder/Module/IconRepository.php`
**Type :** PHP (helper)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Repository centralisé pour les noms d'icônes des modules dans Studio. Fournit une correspondance module -> nom d'icône CSS/image, avec des cas spéciaux pour certains modules.

## Type
helper

## Dépendances clés
Aucune.

## Exports/Symboles principaux
- `IconRepository` — classe (méthodes statiques)
  - Constantes : `DEFAULT_ICON`, `ICON_LABELS`, `ICON_FIELDS`, `ICON_RELATIONSHIPS`, `ICON_LAYOUTS`, `ICON_SUBPANELS`
  - `getIconName($module)` — retourne le nom d'icône pour un module (fallback : module en lowercase avec `_` -> `-`)
- `$iconNames` — tableau statique privé avec les surcharges spéciales (AOS_Contracts, AOR_Scheduled_Reports, EmailTemplates, Employees, etc.)

## Interactions
- **Appelé par :** `StudioModule::getNodes()`, `StudioModule::getModule()`
- **Appelle :** rien

## Notes
La convention par défaut est `strtolower(str_replace('_', '-', $module))` — ex. `AOS_Contracts` devient `aos-contracts` sans surcharge.
