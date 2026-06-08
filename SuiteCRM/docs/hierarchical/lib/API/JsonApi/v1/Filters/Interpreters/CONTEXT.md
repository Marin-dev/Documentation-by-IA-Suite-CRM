# Interpreters

## Rôle
Ce dossier contient les interpréteurs de filtres JSON:API v1 : les classes qui convertissent les structures de filtres parsées en clauses SQL WHERE exploitables. `FilterInterpreter` orchestre la conversion en détectant le type de filtre (par ID, par nom pré-défini, ou par attributs) et en déléguant aux sous-interpréteurs spécialisés.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `FilterInterpreter.php` | Orchestrateur principal — convertit tout type de filtre JSON:API en SQL WHERE |
| `ByIdFilters/` | Interpréteur de filtre par liste d'IDs (`WHERE id IN (...)`) |
| `ByPreMadeFilters/` | Interpréteurs de filtres nommés pré-définis (ex : "Today") |

## Points d'entrée
- `FilterInterpreter.php` — classe centrale, consommée par les repositories et contrôleurs v8

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/`, `lib/API/JsonApi/v1/Filters/Operators/`, `lib/API/JsonApi/v1/Filters/Validators/`, container DI (`FilterOperators`, `ByIdFilterInterpreter`, `ByPreMadeFilterInterpreters`), `\BeanFactory`
- **Utilisé par :** INCONNU — probablement les contrôleurs et repositories de `lib/API/v8/`

## Notes
- Les propriétés statiques de `FilterInterpreter` sont partagées entre instances — attention aux tests.
- Import suspect de `Behat\Gherkin\Filter\FilterInterface` dans du code de production (dette technique).
- `isCustomField()` appelle `\BeanFactory::newBean()` — requiert une connexion BD active.
