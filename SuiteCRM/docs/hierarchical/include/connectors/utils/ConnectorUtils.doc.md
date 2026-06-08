# ConnectorUtils.php

**Chemin :** `include/connectors/utils/ConnectorUtils.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Classe utilitaire centrale pour la gestion et la configuration des connecteurs externes dans SuiteCRM. Permet de lister les connecteurs disponibles, de gerer les configurations d'affichage par module, de mettre a jour les vues Detail (ajout/suppression du bouton hover connector), et d'installer/desinstaller des connecteurs.

## Role technique

Classe statique avec cache `$connectors_cache`. Lit et ecrit dans `custom/modules/Connectors/metadata/` (fichiers `connectors.php`, `display_config.php`, `searchdefs.php`, `mergeviewdefs.php`). Manipule les `viewdefs` des modules pour inserer/retirer les champs hover connecteur. Supporte les templates (`TEMPLATE_URL`).

---

## Dependances cles

- **Imports principaux :**
  - `ConnectorFactory` — instances de connecteurs
  - `SourceFactory` — instances de sources
  - `FormatterFactory` — formatage des donnees connecteur
  - `MetaParser` (`include/SugarFields/Parsers/MetaParser.php`) — parsing des panneaux de vue
  - Fonctions globales : `write_array_to_file()`, `findAllFiles()`, `mkdir_recursive()`

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ConnectorUtils` | classe statique | Utilitaires connecteurs |
| `getConnectors(bool): array` | methode | Liste tous les connecteurs |
| `getConnector(string, bool): ?array` | methode | Donnees d'un connecteur par ID |
| `getDisplayConfig(bool): array` | methode | Config d'affichage par module |
| `getModuleConnectors(string): array` | methode | Connecteurs d'un module |
| `isModuleEnabled(string): bool` | methode | Module active pour connecteurs |
| `isSourceEnabled(string): bool` | methode | Source active dans au moins un module |
| `getViewDefs(?array): array` | methode | Defs de vue de merge |
| `getSearchDefs(bool): array` | methode | Defs de recherche |
| `updateMetaDataFiles(): bool` | methode | Mise a jour des detailviewdefs |
| `installSource(string): bool` | methode | Installation d'un connecteur |
| `uninstallSource(string): bool` | methode | Desinstallation |
| `getConnectorButtonScript(array, Smarty): string` | methode | HTML du bouton connecteur |
| `getConnectorStrings(string, string): array` | methode | Chaines de langue d'un connecteur |
| `eapmEnabled(string, bool): bool` | methode | Verif si EAPM active |

- **Consommateurs identifies :** vues d'administration Connectors, `ExternalAPIFactory`, modules Connectors

## Relations cles

- **Appele par :** administration des connecteurs, vues DetailView des modules actives
- **Appelle :** `ConnectorFactory`, `SourceFactory`, `FormatterFactory`, fonctions d'ecriture fichier
- **Position dans le flux global :** couche de configuration et de meta-donnees du systeme de connecteurs

---

## Points d'attention

- `getMergeViewDefs()` est marquee `@deprecated` (remplacee par `getViewDefs()`).
- `updateMetaDataFiles()` modifie les fichiers `detailviewdefs.php` des modules concernes et supprime le cache Smarty — impact direct sur l'affichage utilisateur.
- `setHoverField()` est declaree `public function` sans `static` mais `removeHoverField()` est `public static` — incoherence, `setHoverField` doit etre appelee sur instance ou corrigee.
- En mode developpeur (`inDeveloperMode()`), force le rechargement a chaque appel.
