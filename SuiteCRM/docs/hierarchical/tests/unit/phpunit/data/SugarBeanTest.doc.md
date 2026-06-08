# SugarBeanTest.php (unit-test)

**Chemin :** `tests/unit/phpunit/data/SugarBeanTest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Suite de tests unitaires très exhaustive couvrant les méthodes de la classe `SugarBean` : construction, champs personnalisés, valeurs par défaut, métadonnées, relations, ownership, requêtes de sous-panneaux, et clonage.

## Type
unit-test

## Dependances cles
- `SuitePHPUnitFrameworkTestCase` — classe de base
- `SugarBeanMock` — mock de SugarBean
- `BeanFactory`, `DBManagerFactory`
- `SuiteValidator`, `DynamicField`, `Link2`, `aSubPanel`
- Includes : `SubPanelDefinitions.php`, `ProspectLink.php`, `AM_ProjectTemplates_sugar.php`
- Framework : PHPUnit

## Scenarios couverts
- `testConstruct` : vérifie l'état d'initialisation du bean (`db`, `module_name`, `required_fields`, `custom_fields`, `column_fields`, `field_defs`, `optimistic_lock`, etc.) pour `AM_ProjectTemplates` et `Users`
- `testSetupCustomFields` : vérification du chemin `base_path` selon le module
- `testBeanImplements` : retourne `false` pour une interface inexistante
- `testPopulateDefaultValues` : avec et sans force, avec/sans field_defs
- `testParseDateDefault` : parsing de dates avec/sans heure, avec séparateurs `&`
- `testRemoveRelationshipMeta` / `testCreateRelationshipMeta` : vérifications des logs fataux selon les paramètres
- `testGetUnionRelatedList` : pagination de liste unifiée (différents états de session, types de sous-panneaux)
- `testBuildSubQueriesForUnion` : construction de sous-requêtes pour union
- `testProcessUnionListQuery` : marqué `markTestIncomplete` — dépendance environnement
- `testRetrieveParentFields` : récupération des champs parent avec différents cas limites
- `testGetAuditEnabledFieldDefinitions` : vérifie les champs audités du module Contacts
- `testIsOwner` : ownership selon `assigned_user_id` et `created_by`
- `testGetCustomTableName` / `testGetTableName` / `testGetObjectName` : vérification des noms de table et d'objet
- `testGetIndices` : structure des index du module Contacts
- `testGetPrimaryFieldDefinition` / `testGetFieldDefinition` / `testGetFieldValue` : accès aux définitions de champs
- `testUnPopulateDefaultValues` : remise à zéro des valeurs par défaut
- `testClone` : clone de bean avec reset des relations chargées
- `testGetLinkedFields` / `testGetFieldDefinitions` / `testLoadRelationship` / `testGetLinkedBeans` : relations et champs liés

## Notes
- `testProcessUnionListQuery` est marqué `markTestIncomplete` (ligne 721) : non exécuté.
- La couverture est très large mais certains cas (ex: `testGetUnionRelatedList` avec `type=collection`) reposent sur des inserts SQL directs dans la table `contacts`.
- Le fichier fait ~2793 lignes — une des suites de tests les plus volumineuses du projet.
