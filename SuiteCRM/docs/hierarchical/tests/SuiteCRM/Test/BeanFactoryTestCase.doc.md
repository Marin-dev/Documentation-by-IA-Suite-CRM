# BeanFactoryTestCase.php (helper / classe de base)

**Chemin :** `tests/SuiteCRM/Test/BeanFactoryTestCase.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Classe de base spécialisée pour les tests portant sur le `BeanFactory` et le mécanisme d'extension de beans (customisation de modules). Elle expose des utilitaires pour créer, compiler et supprimer des extensions de module temporaires pendant les tests, et fournit un data provider listant tous les modules ou un module unique.

## Type
helper / classe de base de test unitaire

## Dependances cles
- `SuitePHPUnitFrameworkTestCase` — classe parente
- `SugarBean` — vérification d'instance
- `SuiteCRM\Exception\Exception`
- Globals PHP : `$beanList`, `$customBeanList`, `$objectList`, `$customObjectList`, `$beanFiles`, `$customBeanFiles`
- `include/modules.php` — rechargement des globals de modules

## Scenarios couverts
Infrastructure de test :
- `moduleConfigProvider()` : data provider Codeception/PHPUnit pour itérer sur tous les modules ou un module unique
- `addCoreModuleExtension()` : crée dynamiquement une classe custom `TestCustomXxx` et son extension dans `custom/Extension/`
- `removeCoreModuleExtension()` / `removeCoreModuleAllExtension()` : nettoyage des extensions temporaires
- `compileIncludeExtFiles()` : recompile le fichier `modules.ext.php`
- `refreshModuleGlobals()` : recharge les globals de modules depuis `include/modules.php`

## Notes
- `testAllModules = false` par défaut : seul le module `Accounts` est testé. Mettre `true` pour couvrir tous les modules.
- La création de fichiers dans `custom/Extension/` implique des droits d'écriture sur le filesystem cible.
- Consommé par `BeanFactoryTest.php`.
