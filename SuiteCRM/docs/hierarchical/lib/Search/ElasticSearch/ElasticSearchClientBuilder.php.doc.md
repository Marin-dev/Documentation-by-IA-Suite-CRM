# ElasticSearchClientBuilder.php

**Chemin :** `lib/Search/ElasticSearch/ElasticSearchClientBuilder.php`
**Type :** PHP — Service / Factory
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Factory pour la creation du client Elasticsearch configure. Lit la configuration de connexion depuis `$sugar_config` et construit un client pret a l'emploi.

## Role technique
Classe statique. Met en cache les hotes dans `$hosts`. Lit `$sugar_config['search']['ElasticSearch']['host/user/pass']`. Sanitize les URLs (ajout de scheme http si absent, parsing URL). Par defaut : `127.0.0.1`.

---

## Dependances cles
- `Elasticsearch\ClientBuilder` — SDK Elasticsearch PHP
- `$sugar_config` global — cles `search.ElasticSearch.host/user/pass`

## Exports / Symboles principaux
- `ElasticSearchClientBuilder` — classe factory statique
  - `static getClient(): \Elasticsearch\Client`
  - `static sanitizeHost($host): array` — validation et normalisation de l'hote

- **Consommateurs identifies :**
  - `lib/Search/ElasticSearch/ElasticSearchEngine.php`
  - `lib/Search/ElasticSearch/ElasticSearchIndexer.php`

## Relations cles
- **Position dans le flux global :** couche d'acces Elasticsearch

---

## Points d'attention
- Config attendue dans `$sugar_config['search']['ElasticSearch']` : `host`, `user` (optionnel), `pass` (optionnel).
- Si `user` est vide, connexion sans authentification.
- Si scheme est `http`, il est retire du tableau d'hote merge (ligne 108-110).
