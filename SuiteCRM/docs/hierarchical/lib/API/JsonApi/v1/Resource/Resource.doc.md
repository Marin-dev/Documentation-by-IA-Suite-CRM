# 📄 Resource.php

**Chemin :** `lib/API/JsonApi/v1/Resource/Resource.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Représente une ressource JSON API complète (`{ id, type, attributes, relationships, links, meta }`). Gère la désérialisation depuis un payload JSON API entrant et la sérialisation vers une réponse JSON API sortante, avec filtrage des champs sensibles.

## ⚙️ Rôle technique
Étend `ResourceIdentifier`. Méthodes clés :
- `fromJsonApiRequest(array $data, string $source)` : construit la ressource depuis un payload, valide `type` et `attributes`, parse les relations (to-one et to-many) avec validation complète
- `toJsonApiResponse()` / `toJsonApiResponseWithFields(array $fields)` : sérialise avec filtrage des champs requis. Les attributs `*_file` sont remplacés par `"<OMITTED>"`
- `withRelationship(Relationship)` : ajoute une relation
- `mergeAttributes(Resource)` : fusionne les attributs d'une autre ressource

Filtre les champs configurés dans `$sugar_config['filter_module_fields']`.

---

## 📥 Entrées / Dépendances
- `SuiteCRM\API\JsonApi\v1\Links`
- `SuiteCRM\API\JsonApi\v1\Enumerator\ResourceEnum`
- `SuiteCRM\API\v8\Exception\BadRequestException`, `ConflictException`
- `$sugar_config` (global) — liste des champs filtrés par module

## 📤 Sorties / Exports
- `Resource` — classe (modèle)
  - `fromJsonApiRequest(array, string): self`
  - `toJsonApiResponse(): array`
  - `toJsonApiResponseWithFields(array): array`
  - `withLinks(Links): self`
  - `withRelationship(Relationship): self`
  - `mergeAttributes(Resource): void`
  - `getRelationshipByName(string): array`
  - `getReservedKeywords(): array`
- **Consommateurs identifiés :**
  - `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php` (extension)

## 🔗 Relations clés
- **Étendu par :** `SuiteBeanResource`
- **Étendu de :** `ResourceIdentifier`

---

## 💡 Points d'attention
- La validation des relations dans `fromJsonApiRequest` est stricte : lève `BadRequestException` si `id` ou `type` manquent dans une relation, ou si `attributes` est présent dans les données de relation.
- Les fichiers (`*_file`) sont masqués dans la sortie (`<OMITTED>`) pour éviter les fuites de données binaires.
- Utilise `$GLOBALS['sugar_config']` — couplage fort au contexte global SuiteCRM.
