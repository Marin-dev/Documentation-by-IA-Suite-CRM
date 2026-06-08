# AOD

## Rôle
Ce dossier contient le moteur de recherche basé sur AOD (Advanced Open Discovery), qui utilise Apache Lucene via la bibliothèque PHP Zend_Search_Lucene. Il s'agit du moteur de recherche plein texte historique de SuiteCRM, basé sur des index Lucene locaux stockés sur le système de fichiers.

## Contenu
| Fichier | Rôle |
|---|---|
| `LuceneSearchEngine.php` | Implémentation du moteur de recherche AOD/Lucene — interroge les index Lucene locaux |

## Points d'entrée
- `LuceneSearchEngine.php` — instancié par `SearchWrapper` quand le moteur AOD est sélectionné

## Dépendances clés
- **Dépend de :** `lib/Search/SearchEngine.php` (classe abstraite parente), bibliothèque Zend_Search_Lucene (legacy), beans SuiteCRM `AOD_Index`
- **Utilisé par :** `lib/Search/SearchWrapper.php`

## Notes
- Moteur legacy basé sur des index fichiers locaux — performances limitées sur de gros volumes.
- Les index Lucene sont gérés par le module AOD (modules/AOD_Index/).
- Pour une meilleure scalabilité, préférer ElasticSearch.
