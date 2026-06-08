# Index

## Rôle
Ce dossier contient l'infrastructure d'indexation du sous-système de recherche SuiteCRM. `AbstractIndexer` définit le contrat commun à tous les indexeurs (index, indexModule, indexBean, removeBean, etc.) et fournit le logging Monolog. Le sous-dossier `Documentify/` contient les convertisseurs de SugarBeans en documents indexables. Des traits utilitaires gèrent le verrouillage, le scheduling et les statistiques d'indexation.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `AbstractIndexer.php` | Classe abstraite de base — contrat d'interface et logging Monolog triple sortie |
| `IndexingLockFileTrait.php` | Trait — gestion du fichier de verrou pour éviter les indexations simultanées |
| `IndexingSchedulerTrait.php` | Trait — scheduling de l'indexation différentielle |
| `IndexingStatisticsTrait.php` | Trait — collecte de statistiques d'indexation (compteurs, durée) |
| `Documentify/` | Convertisseurs SugarBean → documents indexables |

## Points d'entrée
- `AbstractIndexer.php` — étendu par `ElasticSearchIndexer`

## Dépendances clés
- **Dépend de :** `lib/Search/Index/Documentify/`, `lib/Search/SearchWrapper`, `lib/Log/` (handlers Monolog), `Monolog`
- **Utilisé par :** `lib/Search/ElasticSearch/ElasticSearchIndexer.php`, hooks SuiteCRM, commandes Robo ES

## Notes
- Log file par défaut : `search_index.log` à la racine du projet.
- Le documentifier par défaut est `JsonSerializerDocumentifier` — interchangeable via `setDocumentifier()`.
- L'indexation différentielle ne traite que les beans modifiés depuis le dernier index.
