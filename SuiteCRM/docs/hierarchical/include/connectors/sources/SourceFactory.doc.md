# SourceFactory.php

**Chemin :** `include/connectors/sources/SourceFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique pour instancier un objet source de connecteur a partir de son identifiant (ex: `ext_soap_hoovers`). Charge la classe correspondante via `ConnectorFactory::load()` puis instancie et initialise la source.

## Role technique

Classe statique. Convertit l'identifiant `_`-delimite en chemin de fichier. Charge le fichier de la source de base (`default/source.php`) puis le fichier specifique au connecteur. Instancie la classe et appelle `init()` si `$call_init = true`.

---

## Dependances cles

- **Imports principaux :**
  - `source` (`include/connectors/sources/default/source.php`) — classe de base
  - `ConnectorFactory` — chargement de la classe specifique

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `SourceFactory` | classe statique | Fabrique de sources |
| `getSource(string, bool): ?source` | methode statique | Instancie une source par nom |

- **Consommateurs identifies :** `ConnectorFactory::getInstance()`, `ConnectorUtils`, `ExternalAPIFactory`

## Relations cles

- **Appele par :** `ConnectorFactory::getInstance()`, `ConnectorUtils::getSources()`, `ExternalAPIFactory::filterAPIList()`
- **Appelle :** `ConnectorFactory::load()`, constructeur de la classe specifique
- **Position dans le flux global :** instanciation des sources de connecteurs

---

## Points d'attention

- Retourne `null` en cas d'exception a l'instanciation — l'appelant doit verifier la valeur de retour.
- Protection anti-traversal : `strpos($dir, '..')` (ligne 63).
- `$call_init = false` permet de charger la classe sans l'initialiser (utile pour inspecter les proprietes statiques).
