# externalAPI

## Rôle
Module de gestion des intégrations d'APIs externes de SuiteCRM. Fournit la fabrique centrale (`ExternalAPIFactory`) pour découvrir, instancier et filtrer les API externes disponibles (Google Drive, WebEx, GoToMeeting, etc.) selon les credentials EAPM de l'utilisateur. La sous-couche `Base/` définit le contrat et la classe abstraite commune.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `ExternalAPIFactory.php` | Fabrique statique — inventaire, cache, instanciation et filtrage des APIs externes |
| `Base/` | Interface `ExternalAPIPlugin` + classe abstraite `ExternalAPIBase` (auth EAPM) |

## Points d'entrée
- `ExternalAPIFactory::loadAPI(name)` — instanciation d'une API avec credentials
- `ExternalAPIFactory::listAPI(module)` — liste les APIs disponibles pour un module
- `ExternalAPIFactory::loadFullAPIList()` — inventaire complet (scanne les répertoires)

## Dépendances clés
- Dépend de : `ConnectorUtils`, `SourceFactory`, module `EAPM`, `include/externalAPI/Base/`
- Utilisé par : modules Meetings, Documents, EAPM, toute fonctionnalité d'intégration externe

## Notes
- `ExternalAPIFactory` génère un cache PHP et JS (`cache/include/externalAPI.cache.*`) pour éviter de rescanner les répertoires à chaque requête
- En mode développeur, le cache est forcé à la première invocation uniquement (variable statique `$beenHereBefore`)
- Supporte les overrides custom via `custom/include/externalAPI/`
