# TreeData.php

## Rôle
Point d'entrée HTTP pour les requêtes de données arborescentes (listes hiérarchiques). Il route les appels vers la fonction appropriée du fichier `TreeData.php` du module cible, en fonction des paramètres `module` et `function` de la requête.

## Responsabilités
- Extraire et classifier les paramètres de la requête (`PARAMT_*` pour le niveau arbre, `PARAMN_*` pour le niveau nœud)
- Valider que le module demandé est dans la liste blanche `$TreeDataFunctions`
- Appeler dynamiquement (`call_user_func`) la fonction autorisée du fichier `modules/{module}/TreeData.php`
- Retourner le résultat brut (echo)

## Dépendances internes
- `include/entryPoint.php` — initialisation du contexte Sugar
- `include/modules.php` — liste `$beanList` des modules disponibles
- `modules/{modulename}/TreeData.php` — fichier de données arborescentes du module cible (chargé dynamiquement)

## Exports / Points d'entrée
- Aucun export PHP. Point d'entrée HTTP direct.
- Paramètres requis : `module` (nom du module), `function` (nom de la fonction à appeler)
- Paramètres optionnels : préfixés `PARAMT_` (paramètres arbre) et `PARAMN_` (paramètres nœud)

## Notes techniques
- Liste blanche explicite des modules et fonctions autorisés (lignes 99-141) : `ProductTemplates`, `ProductCategories`, `KBTags`, `KBDocuments`, `Forecasts`, `Documents`
- L'appel dynamique via `call_user_func` est sécurisé par cette liste blanche
- Protégé par `sugarEntry`
- Les fonctions sont appelées statiquement (sans instance d'objet)
