# 📄 FilterRepository.php

**Chemin :** `lib/API/JsonApi/v1/Repositories/FilterRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository d'extraction des filtres depuis une requête HTTP. Lit les paramètres `filter[...]` de la query string et les convertit en structures de filtres exploitables via `FilterParser`.

## ⚙️ Rôle technique
`fromRequest(Request $request, array $args): array` lit `$request->getQueryParams()['filter']`, itère sur chaque filtre et appelle `FilterParser::parseFilter()`. Retourne un tableau fusionné de toutes les structures de filtres. Expose aussi `toSuiteBeanResource()` pour instancier `SuiteBeanResource`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Psr\Http\Message\ServerRequestInterface`
  - `SuiteCRM\API\JsonApi\v1\Filters\Parsers\FilterParser`
  - `SuiteCRM\API\JsonApi\v1\Resource\SuiteBeanResource`
  - `Psr\Container\ContainerInterface`
  - `SuiteCRM\API\v8\Exception\BadRequestException`

## 📤 Sorties / Exports
- `FilterRepository` — classe (repository)
  - `fromRequest(Request $request, array $args): array` — structures de filtres parsées
  - `toSuiteBeanResource(): SuiteBeanResource`
- **Consommateurs identifiés :** INCONNU (probablement contrôleurs `lib/API/v8/`)

## 🔗 Relations clés
- **Appelé par :** INCONNU (contrôleurs v8)
- **Appelle :** `FilterParser`, `SuiteBeanResource`
- **Position dans le flux global :** couche d'extraction des filtres entre la requête HTTP et l'interpréteur SQL

---

## 💡 Points d'attention
- `parseFilter()` est appelé avec 3 arguments en ligne 98 mais la méthode n'en accepte que 2 — `$args` est ignoré (signature incompatible silencieuse).
- Si `$queries['filter']` est une chaîne simple (non tableau), elle est retournée telle quelle sans parsing.
