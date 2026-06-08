# 📄 RelationshipService.php

**Chemin :** `Api/V8/Service/RelationshipService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service de gestion des relations entre beans SuiteCRM dans l'API V8. Expose quatre opérations : lecture des beans liés (avec pagination et tri), création d'une relation automatique (détection du lien), création d'une relation par nom de lien explicite, et suppression d'une relation. Vérifie les droits ACL à chaque opération.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Création/suppression de relations, résolution de beans |
| `Api\V8\JsonApi\Helper\{Attribute,Pagination}ObjectHelper` | Construction des réponses JSON:API |
| `Api\V8\JsonApi\Response\{DataResponse, DocumentResponse, LinksResponse, MetaResponse}` | Réponses JSON:API |
| `Api\V8\Param\{Create,CreateByLink,Delete,Get}RelationshipParams` | Paramètres validés par route |
| `Slim\Http\Request` | Requête Slim pour pagination links |
| `\SugarBean`, `\DomainException` | API SuiteCRM native |
| `SuiteCRM\Exception\AccessDeniedException` | Exception ACL |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\RelationshipService`

| Méthode | Signature | Description |
|---|---|---|
| `getRelationship` | `(GetRelationshipParams, Request): DocumentResponse` | Retourne les beans liés avec pagination |
| `createRelationship` | `(CreateRelationshipParams): DocumentResponse` | Crée une relation (détection automatique du lien) |
| `createRelationshipByLink` | `(CreateRelationshipByLinkParams): DocumentResponse` | Crée une relation via lien nommé explicitement |
| `deleteRelationship` | `(DeleteRelationshipParams): DocumentResponse` | Supprime une relation |

---

## Flux des méthodes

### `getRelationship`
1. Vérifie ACL `view` + `list` sur `sourceBean`
2. Récupère les beans liés via `$sourceBean->$linkFieldName->getBeans($linkParams)` avec sort, filter, limit, offset
3. Filtre les beans liés sans accès ACL
4. Calcule la pagination via `$sourceBean->_get_num_rows_in_query` si `size > 0`
5. Retourne `DocumentResponse` avec données + meta pagination + links

### `createRelationship`
1. Vérifie ACL sur source et related
2. Détecte le `linkFieldName` via `BeanManager::getLinkedFieldName`
3. Appelle `BeanManager::createRelationshipSafe`

### `createRelationshipByLink`
1. Vérifie ACL sur source et related
2. Utilise le `linkFieldName` fourni explicitement
3. Appelle `BeanManager::createRelationshipSafe`
4. Retourne les métadonnées détaillées (sourceModule, relatedModule, ids, linkName)

### `deleteRelationship`
1. Vérifie ACL `view` + `edit` + `list` sur source
2. Récupère tous les beans liés via `get_linked_beans`
3. Vérifie ACL `view` + `list` sur le premier bean lié
4. Filtre pour trouver le `relatedBeanId` → `DomainException` si non lié
5. Appelle `BeanManager::deleteRelationshipSafe`

---

## Interactions

- **Appelé par :** `RelationshipController` (routes `/V8/module/{moduleName}/{id}/relationships/...`)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`

---

## Notes

- `getRelationship` utilise `$sourceBean->_get_num_rows_in_query` (méthode interne SugarBean préfixée `_`) — API non publique, potentiellement instable.
- La vérification ACL sur `deleteRelationship` vérifie uniquement le premier bean lié (`reset($relatedBeans)`) — les autres beans liés ne sont pas vérifiés individuellement.
- `createRelationshipByLink` est la variante plus "verbale" : fournit les labels traduits des modules dans la réponse meta (via `translate()`).
