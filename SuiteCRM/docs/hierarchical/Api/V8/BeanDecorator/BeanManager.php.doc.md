# 📄 BeanManager.php

**Chemin :** `Api/V8/BeanDecorator/BeanManager.php`
**Type :** PHP (service central)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service central de l'API V8 pour l'accès et la manipulation des beans SuiteCRM. Encapsule `BeanFactory` (API native SuiteCRM) avec une couche de sécurité (lancement d'exceptions typées), gestion des aliases de modules, et opérations sur les relations entre beans. Injecté dans pratiquement tous les services et contrôleurs de l'API.

**Type :** service

---

## Dépendances clés

| Dépendance | Rôle |
|---|---|
| `\DBManager` | Instance DB pour les requêtes COUNT et vérification de tables |
| `\BeanFactory` | Factory SuiteCRM native pour créer/récupérer des beans |
| `\SugarBean` | Type de base de tous les beans SuiteCRM |
| `\Person` | Sous-classe de SugarBean — utilisée pour filtrage des champs d'acceptation |
| `\Relationship` | Classe SuiteCRM pour récupérer les relations par modules |
| `BeanListRequest` | Builder de requête liste (créé par `getList()`) |
| `array $beanAliases` | Table de correspondance classe → nom module (depuis `beanAliases.php`) |

---

## Constantes

| Constante | Valeur | Description |
|---|---|---|
| `DEFAULT_OFFSET` | `0` | Offset pagination par défaut |
| `DEFAULT_LIMIT` | `-1` | Pas de limite |
| `DEFAULT_ALL_RECORDS` | `-99` | Convention SuiteCRM "tous les enregistrements" |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\BeanDecorator\BeanManager`

| Méthode | Signature | Description |
|---|---|---|
| `newBeanSafe` | `(string $module): \SugarBean` | Crée un nouveau bean, résout les aliases, lève `InvalidArgumentException` si module inconnu |
| `getBean` | `(string $module, ?string $id, array $params, bool $deleted): \SugarBean\|false` | Délègue à `BeanFactory::getBean()` sans sécurité |
| `getBeanSafe` | `(string $module, string $id, array $params, bool $deleted): \SugarBean` | Comme `getBean` mais lève `DomainException` ou `InvalidArgumentException` |
| `getList` | `(string $module): BeanListRequest` | Retourne un builder de requête liste |
| `createRelationshipSafe` | `(\SugarBean $source, \SugarBean $related, string $rel): void` | Crée une relation, lève `RuntimeException` si échec |
| `deleteRelationshipSafe` | `(\SugarBean $source, \SugarBean $related, string $rel): void` | Supprime une relation, lève `RuntimeException` si échec |
| `getLinkedFieldName` | `(\SugarBean $source, \SugarBean $related): string` | Trouve le nom du champ de lien entre deux beans |
| `getLinkedFieldBean` | `(\SugarBean $source, string $linkFieldName): \SugarBean` | Retourne le bean du module lié |
| `countRecords` | `(string $module, string $where): int` | Compte les enregistrements via SQL direct avec LEFT JOIN custom si table existe |
| `getDefaultFields` | `(\SugarBean $bean): array` | Retourne la liste des noms de champs depuis `field_defs` |
| `filterAcceptanceFields` | `(\SugarBean $bean, array $fields): array` | Filtre les champs invalides pour les beans `Person` (exclut les champs `relationship_info`) |

---

## Interactions

- **Enregistré dans :** `Api/V8/Config/services.php` (factory `BeanManager::class`)
- **Injecté dans :** `ListViewSearchService`, `ListViewService`, `LogoutService`, `MetaService`, `ModuleService`, `RelationshipService`, `UserPreferencesService`, `UserService`, toutes les `Param\Options\*`
- **Appelle :** `\BeanFactory`, `\Relationship::retrieve_by_modules`, `$this->db->query/fetchRow/tableExists`

---

## Notes

- `countRecords` fait une requête SQL brute avec JOIN conditionnel sur la table custom (`_cstm`) si elle existe — logique non triviale pour les champs personnalisés SuiteCRM.
- `filterAcceptanceFields` ne filtre que pour les beans `Person` — les autres beans retournent tous les champs sans filtre.
- `getBeanSafe` résout aussi les aliases dans la branche `!$objectName` — logique de résolution en deux passes.
- `getLinkedFieldName` utilise `\Relationship::retrieve_by_modules` dont le comportement exact (retour d'un nom de relation ou d'un objet) n'est pas documenté dans ce fichier — INCONNU le format exact du retour.
- `#[\AllowDynamicProperties]` requis pour PHP 8.2+.
