# QuickSearch.php (quicksearchQuery)

**Chemin :** `modules/Home/QuickSearch.php`
**Type :** PHP - Helper / Service AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Classe de recherche rapide (QuickSearch) répondant aux appels AJAX de `quicksearch.js`. Interroge un ou plusieurs modules SuiteCRM selon des critères de conditions/champs et retourne les résultats en JSON formaté. Gère la recherche de contacts, d'utilisateurs, d'équipes et d'API externes.

## Type
helper / service

## Dépendances clés
- `include/SugarObjects/templates/person/Person.php` — `Person` (formatage nom)
- `include/MVC/SugarModule.php` — `SugarModule::get()->loadBean()`
- `DBManagerFactory` — constructeur de requêtes SQL sécurisé
- `BeanFactory` — instanciation de beans
- `include/externalAPI/ExternalAPIFactory.php` — API externe (méthode `externalApi`)
- `get_user_array()`, `getUserArrayFromFullName()` — utils.php

## Exports / Symboles principaux
- `quicksearchQuery` (classe)
  - `query($args)` — recherche générique multi-modules, renvoie JSON
  - `get_contact_array($args)` — recherche contacts avec formatage nom localisé
  - `get_user_array($args)` — recherche utilisateurs actifs
  - `externalApi($args)` — recherche via API externe
  - Constantes : `CONDITION_CONTAINS`, `CONDITION_LIKE_CUSTOM`, `CONDITION_EQUAL`

## Interactions
- **Appelé par :** `quicksearch.js` (AJAX), INCONNU (dispatcher)
- **Appelle :** `SugarModule`, `DBManagerFactory`, `BeanFactory`, `ExternalAPIFactory`

## Notes
- `constructWhere()` respecte la locale pour le tri nom/prénom des `Person` (ordre configurable).
- Le filtre de résultats (`filterResults`) supprime les doublons exacts.
- `extra_where` permet d'ajouter des conditions SQL supplémentaires aux sous-classes.
