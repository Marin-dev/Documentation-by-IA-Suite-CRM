# include

## Rôle
Dossier racine des bibliothèques partagées de SuiteCRM. Regroupe les modules transversaux utilisés par l'ensemble de l'application : synchronisation calendrier, connecteurs externes, objets framework (config, session, vardefs), formulaires de recherche, et intégrations APIs externes. Ces composants sont inclus par les modules métier et les vues SuiteCRM.

## Contenu
| Dossier | Rôle |
|---|---|
| `CalendarSync/` | Module complet de synchronisation bidirectionnelle de calendriers (DDD, Google/CalDAV) |
| `connectors/` | Système de connecteurs externes pour enrichissement de données (SOAP/REST/XML/EAPM) |
| `SugarObjects/` | Framework SuiteCRM : config, registry, vardefs, session, langue, templates beans |
| `SearchForm/` | Composants de recherche par module et recherche globale (SearchForm2, SugarSpot) |
| `externalAPI/` | Intégrations APIs externes (Google Drive, WebEx, etc.) via le système EAPM |

## Points d'entrée
- `CalendarSync/CalendarSync.php` — façade singleton de la synchronisation calendrier
- `SugarObjects/SugarConfig.php` — accès global à la configuration
- `SugarObjects/VardefManager.php` — chargement des schémas de données modules
- `connectors/ConnectorFactory.php` — instanciation des connecteurs externes
- `externalAPI/ExternalAPIFactory.php` — inventaire et instanciation des APIs externes
- `SearchForm/SearchForm2.php` — formulaire de recherche générique par module

## Dépendances clés
- Dépend de : core SuiteCRM (`BeanFactory`, `DBManagerFactory`, `SugarJobQueue`), module `EAPM`, Smarty
- Utilisé par : l'ensemble des modules métier, vues liste, vues détail, scheduler SuiteCRM

## Notes
- `CalendarSync/` suit une architecture DDD stricte (domain / application / infrastructure)
- `SugarObjects/` contient les composants les plus fondamentaux du framework — à faible instabilité
- `connectors/` et `externalAPI/` partagent le système EAPM pour les credentials utilisateur
- Aucun fichier `.doc.md` directement à la racine de `include/` — tous dans les sous-dossiers
