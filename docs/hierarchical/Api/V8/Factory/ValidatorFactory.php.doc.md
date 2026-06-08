# ValidatorFactory.php

## Rôle
Factory utilitaire qui produit des closures de validation réutilisables à partir de contraintes Symfony Validator. Ces closures sont utilisées dans les classes `BaseParam` pour valider les valeurs de paramètres individuels.

## Responsabilités
- Encapsuler le `ValidatorInterface` de Symfony pour éviter de le passer partout
- `createClosure()` : créer une closure qui valide une valeur scalaire contre un ensemble de contraintes
- `createClosureForIterator()` : créer une closure qui valide chaque élément d'un tableau ou d'un `Iterator` contre les mêmes contraintes
- Gérer optionnellement la valeur `null` (argument `$allowNull`)

## Dépendances internes
- `Symfony\Component\Validator\Validator\ValidatorInterface` — validateur Symfony injecté par DI
- `Symfony\Component\Validator\Constraint` — contraintes passées en argument lors de l'appel

## Exports / Points d'entrée
- `ValidatorFactory` (classe) — factory enregistrée dans le conteneur DI
- `createClosure(array $constraints, bool $allowNull = false): \Closure` — retourne `true` si valide, `false` sinon
- `createClosureForIterator(array $constraints, bool $allowNull = false): \Closure` — variante pour les valeurs itérables

## Notes techniques
- `#[\AllowDynamicProperties]`
- Les closures retournées sont des booléens (pas des listes de violations), ce qui simplifie leur usage dans les classes `Param` mais perd le détail des erreurs de validation
- `createClosureForIterator` retourne `false` si la valeur n'est ni un tableau ni un `Iterator`, rendant la contrainte stricte sur le type
