# Documentify

## Rôle
Ce dossier contient les "documentifiers" : les convertisseurs de SugarBeans en documents indexables. Leur rôle est de transformer un bean SuiteCRM en un tableau de champs structuré pouvant être soumis à un moteur d'indexation (ElasticSearch, Lucene). Ils gèrent la normalisation des données (téléphones, emails, métadonnées).

## Contenu
| Fichier | Rôle |
|---|---|
| `AbstractDocumentifier.php` | Classe abstraite de base — fournit utilitaires de nettoyage et métadonnées standard |
| `JsonSerializerDocumentifier.php` | Sérialise le bean via `json_encode` de son tableau de champs — documentifier par défaut |
| `SearchDefsDocumentifier.php` | Extrait uniquement les champs définis dans `searchdefs.php` du module |

## Points d'entrée
- `JsonSerializerDocumentifier.php` — utilisé par défaut dans `AbstractIndexer`
- `SearchDefsDocumentifier.php` — utilisé pour des index plus ciblés basés sur les définitions de recherche

## Dépendances clés
- **Dépend de :** `SugarBean`, `SugarEmailAddress`, `AbstractDocumentifier`
- **Utilisé par :** `lib/Search/Index/AbstractIndexer.php` (via `setDocumentifier()`), `ElasticSearchIndexer`

## Notes
- Les documentifiers peuvent être interchangés via `AbstractIndexer::setDocumentifier()`.
- `AbstractDocumentifier` inclut 9 champs de métadonnées standard dans chaque document indexé.
- `SearchDefsDocumentifier` produit des index plus légers mais potentiellement incomplets.
