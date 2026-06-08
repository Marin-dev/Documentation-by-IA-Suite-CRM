# VarDefHelper.php

## Rôle
Utilitaire simplifiant l'extraction des relations d'un bean SuiteCRM à partir de ses `vardefs`. Il parcourt les champs liés du bean et retourne une map nom-relation vers nom-module.

## Responsabilités
- Appeler `$bean->get_linked_fields()` pour obtenir tous les champs de type lien
- Filtrer les champs qui possèdent une clé `module` et dont la relation peut être chargée (`$bean->load_relationship()`)
- Retourner un tableau associatif `[relationName => moduleName]`

## Dépendances internes
- `\SugarBean` — classe de base SuiteCRM pour tous les modules (paramètre typé en argument)

## Exports / Points d'entrée
- `VarDefHelper` (classe) — enregistrée dans le conteneur DI, consommée par les services ayant besoin de naviguer les relations
- `getAllRelationships(\SugarBean $bean): array` — retourne `[relationName => moduleName]`

## Notes techniques
- `#[\AllowDynamicProperties]`
- `load_relationship()` a un effet de bord : elle charge la relation dans le bean, ce qui peut consommer de la mémoire si appelé sur de nombreux beans
- La méthode ne distingue pas les types de relations (has-one, has-many, many-to-many) ; le type exact est INCONNU sans accéder aux vardefs complets
