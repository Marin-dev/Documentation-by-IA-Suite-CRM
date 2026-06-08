# SugarRestRSS.php

**Chemin :** `service/core/REST/SugarRestRSS.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle
Implémentation REST au format RSS 2.0. Transforme une liste d'enregistrements SugarBean en flux RSS XML. Utilisée pour exposer des listes de données CRM sous forme de flux. Ne supporte pas les requêtes entrantes (`serve()` retourne toujours une erreur).

**Type :** service

---

## Dépendances clés
- `service/core/REST/SugarRest.php` — classe parente
- `TimeDate` — formatage des dates HTTP
- Globals `$app_strings`, `$sugar_version`, `$sugar_flavor`, `$sugar_config`

---

## Exports/Symboles principaux
- `SugarRestRSS` — (étend `SugarRest`)
  - `generateResponse($input)` — génère un flux RSS 2.0 à partir de `$input['entry_list']`
  - `serve()` — retourne toujours une erreur (RSS = sortie seulement, pas d'entrée)
  - `fault($errorObject)` — génère un flux RSS avec un item contenant l'erreur
  - `generateResponseHeader($count)`, `generateItems($input)`, `generateItem($item)`, `generateResponseFooter()` — méthodes de génération RSS

---

## Interactions
- **Appelé par :** `SugarRestService->serve()` via `response_type=rss`
- **Appelle :** `TimeDate::httpTime()`, `TimeDate::getInstance()`

---

## Notes
- Utilise des heredoc PHP pour générer le XML RSS (lignes 79-89, 119-128, 133-136)
- Chaque item RSS contient : title (champ `name`), link (URL détail record), description (tous les autres champs), pubDate, guid (id)
- `$app_strings['ERR_RSS_INVALID_INPUT']` / `ERR_RSS_INVALID_RESPONSE` — clés de traduction utilisées pour les erreurs
- `$displayFieldNames` : masque les labels si seulement 2 champs retournés (ligne 110)
