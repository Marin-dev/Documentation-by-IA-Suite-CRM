# UserPreferencesController.php

## Rôle
Contrôleur HTTP de l'API V8 exposant les préférences d'un utilisateur SuiteCRM. Il délègue à `UserPreferencesService` et retourne les données au format JSON:API.

## Responsabilités
- Recevoir la requête GET pour les préférences d'un utilisateur
- Déléguer à `UserPreferencesService::getUserPreferences()` la récupération des préférences
- Retourner HTTP 200 avec les préférences, ou HTTP 400 en cas d'exception

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\UserPreferencesService` — service métier pour les préférences utilisateur
- `Api\V8\Param\GetUserPreferencesParams` — objet de paramètres typé injecté par `SuiteInvocationStrategy`

## Exports / Points d'entrée
- `UserPreferencesController` (classe) — contrôleur Slim
- `getUserPreferences(Request, Response, array, GetUserPreferencesParams): Response` — action principale

## Notes techniques
- Utilise la garde `sugarEntry` (ligne 43)
- Structure identique aux autres contrôleurs V8 à action unique (ListView, ListViewSearch, User)
