# 📄 SuiteBeanResource.php

**Chemin :** `lib/API/JsonApi/v1/Resource/SuiteBeanResource.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Adaptateur bidirectionnel entre un `SugarBean` SuiteCRM et une ressource JSON API. Permet de :
1. Convertir un `SugarBean` → réponse JSON API (`fromSugarBean`)
2. Convertir un payload JSON API → `SugarBean` sauvegardé en BD (`toSugarBean`)
3. Gérer les fichiers binaires (upload/download base64)

## ⚙️ Rôle technique
Étend `Resource`. Méthodes principales :
- `fromSugarBean(\SugarBean $bean)` : mappe `field_defs` → `attributes`, convertit les datetimes en ISO 8601 (ATOM), encode les fichiers en base64, génère les liens de relations via `Links`
- `toSugarBean()` : crée ou charge un bean via `BeanFactory`, mappe les attributs, sauvegarde le bean, gère les relations to-one/to-many (ajout/suppression) et les champs de table pivot `meta.middle_table`
- `fromJsonApiRequest()` : délègue à `Resource::fromJsonApiRequest()` puis convertit en `SuiteBeanResource`
- `withRelationship()` : surcharge pour injecter dans `relationships[name]['data']`

Filtre les champs sensibles (`filter_module_fields`), les champs non API-visibles (`api-visible: false`), et les champs `sensitive: true`.

---

## 📥 Entrées / Dépendances
- `SuiteCRM\API\JsonApi\v1\Enumerator\RelationshipType`
- `SuiteCRM\API\JsonApi\v1\Links`
- `SuiteCRM\API\JsonApi\v1\Repositories\RelationshipRepository`
- `SuiteCRM\API\v8\Controller\ApiController`
- `SuiteCRM\Enumerator\ExceptionCode`
- `ConfigurationManager`, `DateTimeConverter`, `Links`, `ResourceIdentifier` (depuis container)
- `\BeanFactory`, `\UploadFile`, `\UploadStream`, `\DocumentRevision` (classes SugarCRM natives)
- `$current_user` (global) — pour l'upload de fichiers

## 📤 Sorties / Exports
- `SuiteBeanResource` — classe (modèle/adaptateur)
  - `fromSugarBean(\SugarBean $bean, string $source): self`
  - `toSugarBean(): \SugarBean`
  - `fromJsonApiRequest(array $data, string $source): self`
  - `withRelationship(Relationship): self`
- **Consommateurs identifiés :** INCONNU (contrôleurs `lib/API/v8/`)

## 🔗 Relations clés
- **Étendu de :** `Resource`
- **Appelle :** `BeanFactory`, `UploadFile`, `RelationshipRepository`, `Links`
- **Position dans le flux global :** couche de traduction centrale entre l'API JSON et la couche données SugarCRM

---

## 💡 Points d'attention
- `toSugarBean()` appelle `$sugarBean->save()` — effet de bord direct en BD à l'exécution.
- La gestion des fichiers (`retrieveFileFromBean`, `saveFileToBean`) charge le fichier entier en mémoire — risque avec les fichiers volumineux.
- Ligne 409 : référence à `$toManyRelationship` (variable de la boucle précédente) dans le bloc `TO_ONE` — potentiel bug de variable hors portée.
- Les champs de type `relate` et `link` sont ignorés lors du mappage `toSugarBean()`.
