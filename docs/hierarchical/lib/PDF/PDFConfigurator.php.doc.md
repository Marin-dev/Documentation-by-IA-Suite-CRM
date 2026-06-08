# PDFConfigurator.php

## Rôle
Classe fluente permettant de modifier et sauvegarder la configuration du moteur PDF actif dans les paramètres globaux de SuiteCRM.

## Responsabilités
- Définir le moteur PDF par défaut dans `$sugar_config['pdf']['defaultEngine']`
- Persister la configuration via `Configurator::saveConfig()`

## Dépendances internes
- `Configurator` (`modules/Configurator/Configurator.php`) — accès et sauvegarde de la config globale

## Exports / Points d'entrée
- `PDFConfigurator::make()` — factory statique (fluent)
- `PDFConfigurator::setEngine(string)` — définit le moteur PDF
- `PDFConfigurator::save()` — persiste la configuration

## Notes techniques
- Pattern fluent : chaque méthode retourne `$this`
- Lance `InvalidArgumentException` si le nom du moteur est vide
- Utilisé depuis les interfaces d'administration pour changer le moteur PDF actif
