# Fichier : ModulesLib.php

**Chemin :** `lib/API/v8/Library/ModulesLib.php`
**Type :** PHP — service / helper
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Bibliothèque de services pour la gestion des listes de modules dans l'API v8. Fournit la logique de pagination, de tri, de filtrage et de construction des liens de navigation (first/last/prev/next) pour les collections de beans SugarCRM. Délègue la construction des URLs de pagination à une méthode privée.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Psr\Container\ContainerInterface` | Conteneur DI Slim |
| `Psr\Http\Message\ServerRequestInterface` | Requête HTTP PSR-7 |
| `League\Uri\Components\Query` | Construction des query strings de pagination |
| `SuiteCRM\API\JsonApi\v1\Filters\Interpreters\FilterInterpreter` | Interprétation des filtres JSON:API |
| `SuiteCRM\API\JsonApi\v1\Links` | Objet liens JSON:API |
| `SuiteCRM\API\JsonApi\v1\Repositories\FilterRepository` | Extraction de la structure de filtre depuis la requête |
| `SuiteCRM\API\JsonApi\v1\Resource\SuiteBeanResource` | Sérialisation bean → JSON:API |
| `SuiteCRM\API\v8\Exception\BadRequestException` | Erreur filtre inconnu |
| `SuiteCRM\API\v8\Exception\ModuleNotFoundException` | Module inexistant |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ModulesLib` | classe | Helper principal pour listes de modules |
| `generatePaginatedModuleRecords()` | méthode publique | Récupère et sérialise une liste paginée de beans |
| `generatePaginatedLinksFromModuleRecords()` | méthode publique | Construit l'objet `links` (first/last/prev/next/self) |
| `getCurrentUser()` | méthode publique | Retourne l'objet `User` depuis l'attribut OAuth2 de la requête |
| `getSorting()` | méthode protégée | Parse le paramètre `sort` → clause SQL ORDER BY |
| `getModuleList()` | méthode protégée | Orchestre le filtrage et appelle `SugarBean::get_list()` |
| `generatePaginationUrl()` | méthode privée | Construit l'URL de pagination avec query string |

---

## Interactions

**Appelé par :**
- `ModuleController::getModuleRecords()` — utilise `generatePaginatedModuleRecords()` et `generatePaginatedLinksFromModuleRecords()`
- `lib/API/v8/container/ModulesLib.php` (instanciation DI)

**Appelle :**
- `BeanFactory::newBean()` — validation du module
- `SugarBean::get_list()` — requête paginée en base
- Container `ConfigurationManager` (clé `list_max_entries_per_page`)
- Container `DatabaseManager` (quote des champs de tri)
- Container `FilterRepository` et `FilterInterpreter` (filtrage)
- Container `SuiteBeanResource` (sérialisation)
- `Links::get()` (construction liens)

---

## Notes

- **Bug potentiel ligne 352** : dans `generatePaginationUrl()`, `$pagination['page']['limit'] = $offset` au lieu de `$limit` — copié du paramètre offset au lieu de limit.
- Le tri supporte les préfixes `-` (DESC) et `+` (ASC), et ASC par défaut — lignes 246-255. Les valeurs sont quotées via `$db->quote()`.
- `getCurrentUser()` lit `oauth_user_id` depuis les attributs de la requête (injecté par le middleware OAuth2 ResourceServer) — ligne 388.
- Trois stratégies de filtre sont supportées : `ByPreMadeName`, `ById`, `ByAttributes` (ligne 307-318). Tout autre filtre lève `BadRequestException`.
