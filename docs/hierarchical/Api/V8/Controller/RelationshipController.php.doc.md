# RelationshipController.php

## Rôle
Contrôleur HTTP de l'API V8 gérant les relations entre enregistrements de modules SuiteCRM. Il expose des endpoints pour lire, créer (via deux méthodes) et supprimer des relations.

## Responsabilités
- `getRelationship()` : lire les enregistrements liés via une relation (HTTP GET, retourne 200)
- `createRelationship()` : créer une relation entre deux enregistrements (HTTP POST, retourne 201)
- `createRelationshipByLink()` : créer une relation via un nom de lien SuiteCRM (HTTP POST, retourne 201)
- `deleteRelationship()` : supprimer une relation existante (HTTP DELETE, retourne 200)
- Déléguer chaque opération à `RelationshipService` et normaliser les réponses HTTP

## Dépendances internes
- `Api\V8\Controller\BaseController` — classe parente (génération de réponses)
- `Api\V8\Service\RelationshipService` — service métier gérant les relations SuiteCRM
- `Api\V8\Param\GetRelationshipParams` — paramètres pour la lecture
- `Api\V8\Param\CreateRelationshipParams` — paramètres pour la création standard
- `Api\V8\Param\CreateRelationshipByLinkParams` — paramètres pour la création par lien
- `Api\V8\Param\DeleteRelationshipParams` — paramètres pour la suppression

## Exports / Points d'entrée
- `RelationshipController` (classe) — contrôleur Slim pour les relations
- `getRelationship(Request, Response, array, GetRelationshipParams): Response`
- `createRelationship(Request, Response, array, CreateRelationshipParams): Response`
- `createRelationshipByLink(Request, Response, array, CreateRelationshipByLinkParams): Response`
- `deleteRelationship(Request, Response, array, DeleteRelationshipParams): Response`

## Notes techniques
- La distinction entre `createRelationship` et `createRelationshipByLink` reflète deux approches de l'API SuiteCRM : la première utilise probablement des IDs, la seconde un nom de lien défini dans les `vardefs`. Le comportement exact est INCONNU sans lire `RelationshipService`
- `getRelationship` passe l'objet `$request` complet au service (pour accès aux query params de pagination éventuelle)
