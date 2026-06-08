# BasicSearch

## Rôle
Ce dossier contient le moteur de recherche basique de SuiteCRM. Il offre une recherche simplifiée sans indexation, s'appuyant directement sur des requêtes SQL basiques. C'est le moteur de repli minimal lorsqu'aucun autre moteur n'est configuré.

## Contenu
| Fichier | Rôle |
|---|---|
| `BasicSearchEngine.php` | Implémentation de la recherche basique — requêtes SQL simples sans index |

## Points d'entrée
- `BasicSearchEngine.php` — instancié par `SearchWrapper` quand le moteur "basic" est sélectionné

## Dépendances clés
- **Dépend de :** `lib/Search/SearchEngine.php` (classe abstraite parente)
- **Utilisé par :** `lib/Search/SearchWrapper.php`

## Notes
- Performances limitées sur de gros volumes — pas d'indexation.
- Moteur de repli recommandé uniquement pour les installations de petite taille ou les environnements de test.
