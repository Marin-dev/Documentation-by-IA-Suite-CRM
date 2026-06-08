# 📄 MetaService.php

**Chemin :** `Api/V8/Service/MetaService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service de métadonnées de l'API V8. Expose trois types d'informations : la liste des modules disponibles, la liste des champs d'un module (vardefs filtrés), et le schéma Swagger de l'API. Vérifie les droits d'accès ACL de l'utilisateur courant avant de retourner les données de champs.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Instanciation des beans pour les vardefs |
| `Api\V8\Helper\ModuleListProvider` | Fournit la liste des modules |
| `Api\V8\JsonApi\Response\{AttributeResponse, DataResponse, DocumentResponse}` | Construction des réponses JSON:API |
| `Api\V8\Param\GetFieldListParams` | Paramètres validés pour `/meta/fields/{moduleName}` |
| `Slim\Http\Request` | Objet requête Slim |
| `SuiteCRM\Exception\{Exception, NotAllowedException, NotFoundException}` | Exceptions métier |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\MetaService`

| Méthode | Visibilité | Description |
|---|---|---|
| `getModuleList(Request $request)` | public | Retourne la liste des modules disponibles |
| `getFieldList(Request $request, GetFieldListParams $params)` | public | Retourne les champs vardefs filtrés du module |
| `getSwaggerSchema()` | public | Lit et retourne `Api/docs/swagger/swagger.json` |
| `checkIfUserHasModuleAccess(string $module)` | private | Vérifie ACL via `query_module_access_list` + `ACLController::filterModuleList` |
| `buildFieldList(string $module)` | private | Construit le tableau de champs en filtrant les vardefs |
| `pruneVardef(array $def)` | private | Filtre un vardef pour ne garder que les champs autorisés |

**Champs vardefs exposés :** `type`, `dbType`, `source`, `relationship`, `default`, `len`, `precision`, `comment`, `required`, `vname`

---

## Interactions

- **Appelé par :** `MetaController` (routes `GET /V8/meta/modules`, `GET /V8/meta/fields/{moduleName}`, `GET /V8/meta/swagger.json`)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`
- **Appelle :** `query_module_access_list`, `\ACLController::filterModuleList`, `BeanManager::newBeanSafe`
- **Lit le fichier :** `Api/docs/swagger/swagger.json`

---

## Notes

- `getSwaggerSchema` retourne directement `json_decode($swaggerFile, true)` (pas un `DocumentResponse`) — incohérence avec les autres méthodes qui retournent des `DocumentResponse`.
- `pruneVardef` ajoute `required: false` si absent et `dbType` copié depuis `type` si absent — normalisation des champs incomplets.
- Vérification ACL uniquement pour `getFieldList` — `getModuleList` ne vérifie pas les droits individuels sur chaque module.
- `$allowedVardefFields` est une whitelist statique privée — pour ajouter un champ vardef exposé, il faut modifier ce fichier.
- Variables globales utilisées : `$current_user` (global PHP SuiteCRM) dans `checkIfUserHasModuleAccess`.
