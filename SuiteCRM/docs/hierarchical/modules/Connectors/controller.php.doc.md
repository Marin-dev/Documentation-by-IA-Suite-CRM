# controller.php

**Chemin :** `modules/Connectors/controller.php`
**Type :** controller

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Contrôleur MVC du module Connectors. Gère les actions de configuration des connecteurs (propriétés, mapping, recherche, affichage).

## Type

controller

---

## Dépendances clés

- `SugarController` (`include/MVC/Controller/SugarController.php`) — classe parente
- `SourceFactory` (`include/connectors/sources/SourceFactory.php`)
- `ConnectorFactory` (`include/connectors/ConnectorFactory.php`)

## Exports / Symboles principaux

- `ConnectorsController` — classe — contrôleur du module Connectors

## Interactions

- **Appelé par :** framework SugarCRM (dispatcher MVC)
- **Appelle :** SourceFactory, ConnectorFactory

## Notes

- Gestionnaire central pour toutes les actions admin des connecteurs.
