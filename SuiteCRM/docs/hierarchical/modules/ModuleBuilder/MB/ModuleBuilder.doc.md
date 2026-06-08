# ModuleBuilder.php

**Chemin :** `modules/ModuleBuilder/MB/ModuleBuilder.php`
**Type :** `PHP` — model/helper
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Gestionnaire de niveau supérieur pour les packages ModuleBuilder. Fournit l'accès à la liste des packages existants, charge les instances `MBPackage` en mémoire et expose l'arbre de navigation pour le panneau latéral.

## Rôle technique
Classe `ModuleBuilder` (non instanciée comme singleton — plusieurs instances possibles). Lit le répertoire `custom/modulebuilder/packages` pour découvrir les packages. Délègue toute la logique métier à `MBPackage`. Définit les constantes de chemin `MB_PACKAGE_PATH` et `MB_PACKAGE_BUILD`.

---

## Dépendances clés
- `modules/ModuleBuilder/MB/MBPackage.php` — classe `MBPackage`

## Exports / Symboles principaux
- `MB_PACKAGE_PATH` — constante — chemin `custom/modulebuilder/packages`
- `MB_PACKAGE_BUILD` — constante — chemin `custom/modulebuilder/builds`
- `ModuleBuilder` — classe
  - `getPackageList()` — liste les packages disponibles sur disque
  - `getPackage($name)` — retourne (ou crée) une instance `MBPackage`
  - `getPackageKey($name)` — lit la clé depuis le manifest
  - `getPackageModule($package, $module)` — retourne (référence) un `MBModule`
  - `save()` — sauvegarde tous les packages en mémoire
  - `build()` — construit tous les packages en ZIP
  - `getPackages()` — charge tous les packages depuis le disque
  - `getNodes()` — retourne la structure arbre pour le panneau latéral
  - `getModuleAliases($module)` — (statique) retourne les alias du module (ex. Users ↔ Employees)

## Interactions
- **Appelé par :** `ModuleBuilderController`, `ParserDropDown`, `MBPackageTree`
- **Appelle :** `MBPackage`

## Notes
- `getPackageList()` utilise un cache statique (ligne 64) — le premier appel lit le disque, les suivants retournent le cache.
- `getModuleAliases()` gère uniquement le cas Users/Employees (ligne 166).
