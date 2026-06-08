# SearchThrowableHandler.php

**Chemin :** `lib/Search/UI/SearchThrowableHandler.php`
**Type :** PHP — Service (gestion d'erreurs)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Gestionnaire d'exceptions et d'erreurs du framework de recherche. En mode developpeur, affiche une page d'erreur detaillee (Whoops) avec le contexte de la requete. En production, affiche un message utilisateur localise.

## Role technique
Classe. Methode `handle()` : logue l'erreur via `SuiteLogger`, en mode developpeur utilise `Whoops\Run` avec `PrettyPageHandler` (inclut la `SearchQuery` et le statut `SearchWrapper` comme contexte), sinon affiche un message HTML simple.

---

## Dependances cles
- `SuiteCRM\Utility\SuiteLogger`
- `SuiteCRM\Search\{Exceptions\*, SearchQuery, SearchWrapper}`
- `Whoops\{Run, Handler\PrettyPageHandler}`
- `$sugar_config['developerMode']`
- `$mod_strings` (labels traduits)

## Exports / Symboles principaux
- `SearchThrowableHandler` — classe
  - `handle(): void`

## Relations cles
- **Appele par :** modules/controllers lors du catch d'une exception de recherche

---

## Points d'attention
- `developerMode` dans `$sugar_config` active la page Whoops detaillee.
- Le mapping exception -> message utilisateur (ligne 119) couvre : `SearchUserFriendlyException`, `SearchInvalidRequestException`, `SearchEngineNotFoundException`, `NoNodesAvailableException`, `SearchException`, `Missing404Exception`.
- Utilise `$mod_strings` — necessite l'initialisation des langues.
