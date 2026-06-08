# 📄 ModuleService.php

**Chemin :** `Api/V8/Service/ModuleService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service principal de gestion des enregistrements de modules SuiteCRM dans l'API V8. Implémente les 4 opérations CRUD (lecture d'un enregistrement, liste, création, mise à jour, suppression) avec contrôle d'accès ACL, pagination JSON:API, gestion des fichiers attachés (Notes, Documents), et filtrage par email.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\{BeanListResponse, BeanManager}` | Accès et liste des beans |
| `Api\V8\JsonApi\Helper\{Attribute,Pagination,Relationship}ObjectHelper` | Construction des réponses JSON:API |
| `Api\V8\JsonApi\Response\{DataResponse, DocumentResponse, MetaResponse}` | Réponses JSON:API |
| `Api\V8\Param\{Create,Delete,Get,GetModules,Update}ModuleParams` | Paramètres validés par route |
| `BeanFactory`, `DocumentRevision`, `SugarBean` | API SuiteCRM native |
| `SuiteCRM\Exception\AccessDeniedException` | Exception ACL |
| `Slim\Http\Request` | Requête Slim |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\ModuleService`

| Méthode | Signature | Description |
|---|---|---|
| `getRecord` | `(GetModuleParams, $path): DocumentResponse` | Lecture d'un enregistrement unique |
| `getRecords` | `(GetModulesParams, Request): DocumentResponse` | Lecture paginée d'une liste |
| `createRecord` | `(CreateModuleParams, Request): DocumentResponse` | Création d'un enregistrement |
| `updateRecord` | `(UpdateModuleParams, Request): DocumentResponse` | Mise à jour d'un enregistrement |
| `deleteRecord` | `(DeleteModuleParams): DocumentResponse` | Suppression (soft-delete) |
| `getDataResponse` | `(SugarBean, ?array $fields, ?string $path): DataResponse` | Builder de réponse pour un bean |
| `processAttributes` | `(&SugarBean, array): bool` (protected) | Applique les attributs au bean, détecte upload fichier |
| `setRecordUpdateParams` | `(SugarBean, array): void` (protected) | Configure les flags de mise à jour bean |
| `addFileToNote` | `(string $beanId, array): void` (protected) | Écrit le fichier en upload pour Notes |
| `addFileToDocument` | `(SugarBean, array): void` (private) | Écrit le fichier et crée la révision Document |

---

## Comportements non-évidents

### Gestion des emails dans `getRecords`
Si le filtre `WHERE` contient `email1` ou `email2` et que le bean possède ces propriétés, une requête SQL spéciale est construite avec JOIN sur `email_addresses` et `email_addr_bean_rel` (lignes 131-188). Sinon, le path standard via `BeanListRequest` est utilisé.

### Upload de fichiers
- `createRecord` détecte `filename` dans les attributs → `processAttributes` retourne `true`
- Si module `Notes` → `addFileToNote` (écrit en `upload/{beanId}`)
- Si module `Documents` → `addFileToDocument` (crée une révision `DocumentRevision`)
- Contenu encodé en base64 dans `filecontents`

### Contrôle ACL
- `getRecord`, `getRecords` : `ACLAccess('view')`
- `createRecord`, `updateRecord` : `ACLAccess('save')`
- `updateRecord` + `deleted=true` : `ACLAccess('delete')` supplémentaire
- `deleteRecord` : `ACLAccess('delete')`

---

## Interactions

- **Appelé par :** `ModuleController` (routes CRUD `/V8/module`)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`
- **Appelle :** `BeanManager`, `BeanFactory`, `AttributeObjectHelper`, `RelationshipObjectHelper`, `PaginationObjectHelper`

---

## Notes

- Commentaire ligne 104 : "this whole method should split into separated classes later" — dette technique majeure dans `getRecords`.
- `$sugar_config['upload_badext']` (global PHP) est utilisé pour valider les extensions de fichiers uploadés.
- Bug potentiel ligne 329 : `$Revision->doc_url = $this->doc_url` — `$this->doc_url` n'existe pas dans `ModuleService` (probablement une erreur de copier-coller depuis une autre classe).
- Pagination : calculée seulement si `$data` est non-vide ET `$limit !== DEFAULT_LIMIT`.
