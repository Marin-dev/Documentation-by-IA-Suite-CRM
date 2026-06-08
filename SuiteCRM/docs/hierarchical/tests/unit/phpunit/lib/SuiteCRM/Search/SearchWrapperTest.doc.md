# SearchWrapperTest.php (unit-test)

**Chemin :** `tests/unit/phpunit/lib/SuiteCRM/Search/SearchWrapperTest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests unitaires de `SearchWrapper`, le facade centralisé de recherche SuiteCRM. Vérifie la sélection du moteur de recherche, la gestion des moteurs invalides et l'interaction avec les moteurs mock.

## Type
unit-test

## Dependances cles
- `SearchTestAbstract` — classe de base de test Search
- `SearchWrapper` — classe testée
- `SearchEngineMock`, `ElasticSearchEngine`, `SearchEngine`, `SearchQuery`
- `SuiteCRM\Search\Exceptions\SearchEngineNotFoundException`
- `Mockery` — mocking
- Framework : PHPUnit
- Namespace : `SuiteCRM\Tests\Unit\lib\SuiteCRM\Search`

## Scenarios couverts
INCONNU dans le détail sans lecture complète — mais le contexte indique :
- Tests de sélection/enregistrement du moteur de recherche
- Tests d'erreur (moteur non trouvé)
- Tests d'exécution de requêtes via le wrapper

## Notes
- Utilise `SearchEngineMock` et `BadMockSearch` pour simuler différents comportements.
- Namespace : `SuiteCRM\Tests\Unit\lib\SuiteCRM\Search`.
