# PDFConfigurator.php

**Chemin :** `lib/PDF/PDFConfigurator.php`
**Type :** PHP — Service / Fluent API
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Service de configuration du moteur PDF par defaut. Permet de modifier et de sauvegarder le choix du moteur PDF dans la configuration SuiteCRM de maniere fluide.

## Role technique
Encapsule un objet `Configurator` (module Administration). Methodes fluentes (retournent `$this`). Factory statique `make()`. La methode `setEngine()` ecrit dans `$configurator->config['pdf']['defaultEngine']` ; `save()` appelle `$configurator->saveConfig()`.

---

## Dependances cles
- `Configurator` (modules/Configurator/Configurator.php) — gestion de la config SuiteCRM
- `InvalidArgumentException` (PHP natif)

## Exports / Symboles principaux
- `PDFConfigurator` — classe service
  - `static make(): PDFConfigurator` — factory
  - `setEngine(string $engine): PDFConfigurator` — fluent setter
  - `save(): PDFConfigurator` — persiste la config

## Relations cles
- **Appele par :** INCONNU (vraisemblablement depuis l'interface d'administration PDF)
- **Appelle :** `Configurator::saveConfig()`

---

## Points d'attention
- Lancer `save()` ecrit dans `config_override.php` (comportement de `Configurator`).
