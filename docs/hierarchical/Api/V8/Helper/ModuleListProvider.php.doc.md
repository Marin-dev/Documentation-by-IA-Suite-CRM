# ModuleListProvider.php

## Rôle
Fournisseur de la liste des modules SuiteCRM accessibles à l'utilisateur courant. Il interroge les ACL SuiteCRM, filtre les modules invisibles, et enrichit chaque entrée avec les droits d'accès et le libellé traduit.

## Responsabilités
- Appeler `query_module_access_list()` pour obtenir la liste brute des modules accessibles
- Filtrer via `ACLController::filterModuleList()` les modules interdits par ACL
- Supprimer les modules déclarés invisibles (`$modInvisList`)
- Enrichir chaque module avec ses actions autorisées (`ACLAction::getUserActions()`)
- Ajouter le libellé traduit depuis `$app_list_strings['moduleList']`

## Dépendances internes
- Globals SuiteCRM : `$current_user`, `$app_list_strings`, `$modInvisList`
- Fonctions globales SuiteCRM : `query_module_access_list()`, `is_admin()`
- Classes statiques SuiteCRM : `ACLController::filterModuleList()`, `ACLAction::getUserActions()`
- Constante SuiteCRM : `ACL_ALLOW_ENABLED`

## Exports / Points d'entrée
- `ModuleListProvider` (classe) — enregistrée dans le conteneur DI, consommée par `MetaService`
- `getModuleList(): array` — retourne un tableau associatif `[moduleName => ['label' => ..., 'access' => [...]]]`

## Notes techniques
- `#[\AllowDynamicProperties]`
- Forte dépendance aux globals SuiteCRM : cette classe ne peut fonctionner qu'en contexte SuiteCRM complet, avec `$current_user` et `$app_list_strings` initialisés
- Ligne 149 : `is_admin(is_admin($current_user))` est une double invocation potentiellement redondante — `is_admin()` retourne un booléen, donc appeler `is_admin(true/false)` peut produire un comportement inattendu (dette technique probable)
- Les modules sans action accessible (`count($access) === 0`) sont exclus du résultat final
