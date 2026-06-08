# ModuleController.php

## Rôle
Contrôleur HTTP de l'API V8 implémentant les opérations CRUD sur les enregistrements des modules SuiteCRM. C'est le contrôleur central de l'API REST, couvrant la lecture, création, mise à jour et suppression d'enregistrements.

## Responsabilités
- `getModuleRecord()` : récupérer un enregistrement unique d'un module (HTTP GET, retourne 200)
- `getModuleRecords()` : récupérer une liste d'enregistrements d'un module avec filtres/pagination (HTTP GET, retourne 200)
- `createModuleRecord()` : créer un nouvel enregistrement (HTTP POST, retourne 201)
- `updateModuleRecord()` : mettre à jour un enregistrement existant (HTTP PATCH/PUT, retourne 201)
- `deleteModuleRecord()` : supprimer un enregistrement (HTTP DELETE, retourne 200)
- Déléguer chaque opération à `ModuleService` et normaliser les réponses HTTP

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\ModuleService` — service métier pour les opérations CRUD sur les modules
- `Api\V8\Param\GetModuleParams` — paramètres pour la lecture d'un enregistrement
- `Api\V8\Param\GetModulesParams` — paramètres pour la lecture de plusieurs enregistrements
- `Api\V8\Param\CreateModuleParams` — paramètres pour la création
- `Api\V8\Param\UpdateModuleParams` — paramètres pour la mise à jour
- `Api\V8\Param\DeleteModuleParams` — paramètres pour la suppression

## Exports / Points d'entrée
- `ModuleController` (classe) — contrôleur Slim principal de l'API V8
- `getModuleRecord(Request, Response, array, GetModuleParams): Response`
- `getModuleRecords(Request, Response, array, GetModulesParams): Response`
- `createModuleRecord(Request, Response, array, CreateModuleParams): Response`
- `updateModuleRecord(Request, Response, array, UpdateModuleParams): Response`
- `deleteModuleRecord(Request, Response, array, DeleteModuleParams): Response`

## Notes techniques
- `createModuleRecord` et `updateModuleRecord` retournent tous deux HTTP 201 (conformément à JSON:API pour les créations/modifications)
- `getModuleRecord` transmet `$request->getUri()->getPath()` au service, probablement pour construire les liens `self` de la réponse JSON:API
- `getModuleRecords` transmet l'objet `$request` complet au service (pour accès aux query params de pagination/filtre)
- Toutes les exceptions sont capturées et converties en 400 sans distinction de type (pas de gestion différenciée 404/422/500)
