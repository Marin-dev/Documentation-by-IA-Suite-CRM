# BaseController.php

## Rôle
Classe abstraite de base dont héritent tous les contrôleurs de l'API V8. Elle fournit deux méthodes utilitaires partagées pour produire des réponses HTTP au format JSON:API (`application/vnd.api+json`).

## Responsabilités
- Définir la constante de media type `application/vnd.api+json` utilisée par toute l'API
- Fournir `generateResponse()` : sérialise n'importe quel objet en JSON (pretty print, unicode non échappé) et positionne les en-têtes `Accept` et `Content-type`
- Fournir `generateErrorResponse()` : construit un objet `ErrorResponse` à partir d'une exception et délègue à `generateResponse()`
- Servir de contrat commun pour tous les contrôleurs enfants

## Dépendances internes
- `Api\V8\JsonApi\Response\ErrorResponse` — objet de réponse d'erreur JSON:API
- `Slim\Http\Response` — objet réponse HTTP du framework Slim

## Exports / Points d'entrée
- `BaseController` (classe abstraite) — classe parente de tous les contrôleurs V8
- `MEDIA_TYPE` (constante publique) — valeur `'application/vnd.api+json'`
- `generateResponse(HttpResponse, mixed, int): HttpResponse` — méthode publique héritée
- `generateErrorResponse(HttpResponse, \Exception, int): HttpResponse` — méthode publique héritée

## Notes techniques
- Utilise l'attribut PHP 8 `#[\AllowDynamicProperties]` pour compatibilité avec les sous-classes qui ajoutent des propriétés dynamiquement
- Les flags JSON `JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` sont appliqués systématiquement à toutes les réponses
- Les en-têtes `Accept` et `Content-type` sont tous deux définis sur `application/vnd.api+json`, conformément à la spécification JSON:API
