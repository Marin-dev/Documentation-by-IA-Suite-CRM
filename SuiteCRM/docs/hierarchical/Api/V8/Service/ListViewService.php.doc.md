# 📄 ListViewService.php

**Chemin :** `Api/V8/Service/ListViewService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service responsable de la récupération et de la mise en forme des colonnes de la list view d'un module SuiteCRM. Retourne la liste des colonnes avec leurs métadonnées (label traduit, largeur, lien, tri) au format compatible avec l'interface Angular `ListViewColumnInterface`.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans |
| `Api\V8\JsonApi\Helper\{Attribute,Pagination,Relationship}ObjectHelper` | Injectés mais non utilisés dans les méthodes actuelles |
| `Api\V8\JsonApi\Response\AttributeResponse` | Réponse contenant les colonnes |
| `Api\V8\Param\ListViewColumnsParams` | Paramètres validés |
| `ListViewFacade` | Récupère les colonnes de la list view (include_once ligne 56) |
| `SuiteCRM\LangText` | Traduction des labels |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\ListViewService`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(BeanManager, AttributeObjectHelper, RelationshipObjectHelper, PaginationObjectHelper)` | Injection des 4 dépendances |
| `getListViewDefs` | `(ListViewColumnsParams $params): JsonSerializable` | Retourne les colonnes de list view avec labels traduits |

**Constante de classe :**
`$listViewColumnInterface` — template de structure de colonne (fieldName, width, label, link, default, module, id, sortable, customCode)

---

## Structure de réponse retournée par `getListViewDefs`

```
AttributeResponse
  └─ array de colonnes :
       ├─ fieldName: string
       ├─ width: string
       ├─ label: string (traduit)
       ├─ link: bool
       ├─ default: bool
       ├─ module: string
       ├─ id: string
       ├─ sortable: bool
       └─ customCode: string (déprécié)
```

---

## Interactions

- **Appelé par :** `ListViewController::getListViewColumns` (INCONNU — déduction par routage)
- **Appelle :** `BeanFactory::getBean`, `ListViewFacade::getDisplayColumns`, `LangText::getText`
- **Consommé dans DI :** `Api/V8/Config/services/services.php`

---

## Notes

- `include_once` ligne 56 pour `ListViewFacade` — pas d'autoloading Composer.
- `guard` `sugarEntry` présent (ligne 52-54).
- Les helpers `attributeHelper`, `relationshipHelper`, `paginationHelper` sont injectés mais **non utilisés** dans le code actuel — présence anticipée pour extension future ou vestige de refactoring.
- `customCode` est marqué `// deprecated from legacy (using only on PHP front-end)` ligne 82.
- TODO commenté ligne 146 : validation des colonnes de list view à implémenter.
- Fallback de traduction ligne 141 : si `$text->getText($column['label'])` échoue, tente `$text->getText($bean->field_name_map[strtolower($key)]['vname'])`.
