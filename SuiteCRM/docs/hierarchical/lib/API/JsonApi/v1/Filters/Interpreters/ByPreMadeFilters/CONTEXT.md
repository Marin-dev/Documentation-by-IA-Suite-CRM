# ByPreMadeFilters

## Rôle
Ce dossier regroupe les filtres pré-définis nommés de l'API JSON:API v1. Chaque classe représente un filtre métier nommé (ex : "Today") que le client peut appeler par son nom dans la requête, sans avoir à construire lui-même la clause SQL sous-jacente. Ces filtres facilitent les cas d'usage courants.

## Contenu
| Fichier | Rôle |
|---|---|
| `Today.php` | Filtre pré-défini "Today" — retourne `date_entered >= "YYYY-MM-DDTHH:MM:SS+TZ"` depuis minuit |

## Points d'entrée
- `Today.php` — filtre pré-défini disponible, enregistré dans le container DI sous `ByPreMadeFilterInterpreters`

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/Filters/Interfaces/ByPreMadeFilterInterpreter`, `\DateTime` (PHP natif)
- **Utilisé par :** `lib/API/JsonApi/v1/Filters/Interpreters/FilterInterpreter.php`

## Notes
- La timezone utilisée est celle du serveur PHP — des décalages peuvent survenir si le serveur est en UTC et la BD en heure locale.
- Seul `date_entered` est filtré (pas `date_modified`).
- D'autres filtres pré-définis pourraient être ajoutés dans ce dossier (ex : "ThisWeek", "LastMonth").
