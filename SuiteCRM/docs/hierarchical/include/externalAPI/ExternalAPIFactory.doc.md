# ExternalAPIFactory.php

**Chemin :** `include/externalAPI/ExternalAPIFactory.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fabrique de decouverte et d'instanciation des API externes de SuiteCRM (Google Drive, WebEx, GoToMeeting, etc.). Permet de lister les APIs disponibles par module ou fonctionnalite, de filtrer celles dont l'utilisateur a les credentials, et d'en charger une instance initialisee avec les informations d'authentification EAPM.

## Role technique

Classe statique. `loadFullAPIList()` scanne les repertoires `include/externalAPI/` et `custom/include/externalAPI/` a la recherche de classes `ExtAPI{Name}.php`. Construit et met en cache un fichier PHP (`cache/include/externalAPI.cache.php`) et un fichier JS. `loadAPI()` charge l'API et lui injecte les credentials EAPM de l'utilisateur courant. `filterAPIList()` supprime les APIs dont le connecteur associe est desactive ou sans credentials OAuth configures.

---

## Dependances cles

- **Imports principaux :**
  - `ConnectorUtils` — verification d'activation EAPM
  - `SourceFactory` — verification des credentials OAuth du connecteur
  - `EAPM` (module) — chargement des credentials utilisateur
  - `ExternalAPIBase` (`include/externalAPI/Base/ExternalAPIBase.php`) — classe de base des APIs

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `ExternalAPIFactory` | classe statique | Fabrique d'APIs externes |
| `loadFullAPIList(bool, bool): array` | methode | Inventaire complet de toutes les APIs |
| `filterAPIList(array): array` | methode | Filtre les APIs desactivees/sans credentials |
| `loadAPI(string, bool): ExternalAPIBase|false` | methode | Instancie une API avec credentials |
| `listAPI(string, bool): array` | methode | Liste les APIs pour un module |
| `getModuleDropDown(string, bool, bool): array` | methode | Tableau cle=>label pour select UI |
| `clearCache(): void` | methode | Supprime le cache fichier |

- **Consommateurs identifies :** modules Meetings, Documents, module EAPM, toute fonctionnalite d'integration externe

## Relations cles

- **Appele par :** modules qui proposent des intégrations externes (Meetings, Cases, Documents)
- **Appelle :** `ConnectorUtils::eapmEnabled()`, `SourceFactory::getSource()`, `EAPM::getLoginInfo()`
- **Position dans le flux global :** point d'entree unique pour toutes les integrations API externes

---

## Points d'attention

- `loadFullAPIList()` utilise `rename()` pour une ecriture atomique du cache (ecriture dans un tmp puis renommage) — robuste contre les lectures partielles.
- En mode developpeur, force une reconstruction a la premiere invocation de la requete seulement (variable statique `$beenHereBefore` — ligne 98).
- Le fichier de cache JS (`externalAPI.cache.js`) est genere en parallele du PHP — les clients JS peuvent l'interroger directement.
- `listAPI()` filtre sur `supportedModules` : si le tableau est vide dans la definition, l'API n'apparait dans aucun module.
