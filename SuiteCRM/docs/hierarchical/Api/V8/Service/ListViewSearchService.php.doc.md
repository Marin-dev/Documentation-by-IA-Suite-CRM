# 📄 ListViewSearchService.php

**Chemin :** `Api/V8/Service/ListViewSearchService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service responsable de la récupération et de la mise en forme des définitions de recherche (search defs) d'un module SuiteCRM. Retourne la structure de filtres de recherche (basic / advanced) avec les libellés traduits dans la langue de l'utilisateur, au format JSON:API.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans (déclaré mais non utilisé directement dans les méthodes publiques) |
| `Api\V8\JsonApi\Response\{AttributeResponse, DataResponse, DocumentResponse}` | Construction des réponses JSON:API |
| `Api\V8\Param\ListViewSearchParams` | Paramètres validés de la requête |
| `SearchForm` | Classe SuiteCRM pour récupérer les search defs (include_once ligne 60) |
| `SuiteCRM\LangText` | Traduction des libellés |
| `ListViewFacade` | Récupère les colonnes de la list view (include_once ligne 61) |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\ListViewSearchService`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(BeanManager $beanManager)` | Injection du BeanManager |
| `getListViewSearchDefs` | `(ListViewSearchParams $params): JsonSerializable` | Point d'entrée principal — retourne la structure de search defs traduite |
| `getDataTranslated` | `(LangText, array, string, string, array): array` (protected) | Traduit les libellés d'une section (basic/advanced/fields) |

---

## Structure de réponse retournée par `getListViewSearchDefs`

```
DocumentResponse
  └─ DataResponse (type: 'SearchDefs', id: null)
       └─ AttributeResponse
            ├─ module: string
            ├─ templateMeta: array
            ├─ basic: array (champs de recherche basique avec labels traduits)
            ├─ advanced: array (champs de recherche avancée avec labels traduits)
            └─ fields: array (définitions de champs avec vnames traduits)
```

---

## Interactions

- **Appelé par :** `ListViewSearchController::getModuleSearchDefs` (INCONNU — déduction par le routage)
- **Appelle :** `SearchForm::retrieveSearchDefs`, `ListViewFacade::getDisplayColumns`, `LangText::getText`
- **Consommé dans DI :** `Api/V8/Config/services/services.php`

---

## Notes

- `include_once` aux lignes 60-61 pour `SearchForm` et `ListViewFacade` — ces classes ne sont pas autoloadées via Composer, elles requièrent un include manuel.
- `getDataTranslated` est une méthode protected (non testable unitairement sans sous-classe) qui itère sur les sections du tableau et remplace les labels.
- Avertissement logger si un label de traduction est introuvable (ligne 108 : `\LoggerManager::getLogger()->warn(...)`).
- `guard` `sugarEntry` présent (ligne 56-58) — protection SuiteCRM standard contre l'appel direct.
- Le constructeur déclare des paramètres supplémentaires dans le phpdoc (`$attributeHelper`, `$relationshipHelper`, `$paginationHelper`) non présents dans la signature réelle — vestige de refactoring.
