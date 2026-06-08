# FormatterFactory.php

**Chemin :** `include/connectors/formatters/FormatterFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique de formateurs pour les connecteurs externes. Un formateur controle la presentation des donnees d'un connecteur dans les vues SuiteCRM (hover links, boutons de fusion). Utilise un formateur specifique au connecteur si disponible, sinon le formateur par defaut.

## Role technique

Classe statique avec cache `$formatter_map`. Similaire a `FilterFactory` mais pour les formateurs. Cherche un fichier `{connector}_formatter.php` dans `modules/Connectors/connectors/formatters/`, puis configure le template TPL associe.

---

## Dependances cles

- **Imports principaux :**
  - `formatter` (`include/connectors/formatters/default/formatter.php`) — classe de base formateur
  - `ConnectorFactory` — chargement et instance du composant

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `FormatterFactory` | classe statique | Fabrique de formateurs |
| `getInstance(string, string): formatter` | methode statique | Retourne/cree le formateur cache |

- **Consommateurs identifies :** `ConnectorUtils::updateMetaDataFiles()`, `ConnectorUtils::getViewDefs()`

## Relations cles

- **Appele par :** `ConnectorUtils` lors de la mise a jour des vues
- **Appelle :** `ConnectorFactory::load()`, `ConnectorFactory::getInstance()`
- **Position dans le flux global :** rendu des donnees connecteur dans les vues SuiteCRM

---

## Points d'attention

- La condition ligne 99 (`if ("modules/Connectors/...")`) est toujours vraie (string non vide) — bug potentiel : le template par defaut est toujours tente meme si le fichier n'existe pas.
