# BeanFactoryTest.php (unit-test)

**Chemin :** `tests/unit/phpunit/data/BeanFactoryTest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests unitaires couvrant les méthodes de résolution de beans du `BeanFactory` : instanciation, chargement de fichiers, résolution de classe (core vs. custom), récupération de métadonnées, et support des classes personnalisées créées par extension.

## Type
unit-test

## Dependances cles
- `BeanFactoryTestCase` — classe de base (gestion des extensions temporaires)
- `BeanFactory` — classe testée
- Framework : PHPUnit
- Data provider : `moduleConfigProvider()` (par défaut module `Accounts` uniquement)

## Scenarios couverts
- `testNewBean` : vérifie que `BeanFactory::newBean()` retourne le bean core, puis le bean custom après ajout d'extension
- `testGetBean` : idem pour `BeanFactory::getBean()`
- `testGetBeanMeta` : vérifie les métadonnées (className, objectName, classFile, customBeanName, customClassFile)
- `testGetBeanClass` / `testGetBeanName` / `testGetObjectName` / `testGetBeanFile` : vérification des résolveurs de classe, nom, objet, fichier (core puis custom)
- `testLoadBeanFile` : vérifie que le fichier de classe est chargé et que la classe existe

## Notes
- Plusieurs méthodes `TODO` listées dans le fichier : `convertParams`, `testInitBeanRegistry`, `testHasEncodeFlag`, `testHasDeletedFlag`, `testRegisterBean`, `testUnregisterBean` — non couverts.
- La pattern setup/teardown (`removeCoreModuleExtension` / `addCoreModuleExtension`) garantit l'isolation mais écrit sur le filesystem.
- `testAllModules = false` par héritage : seul Accounts est testé par défaut.
