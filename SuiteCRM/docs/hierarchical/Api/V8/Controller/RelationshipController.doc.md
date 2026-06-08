# 📄 RelationshipController.php

**Chemin :** `Api/V8/Controller/RelationshipController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 gérant les opérations sur les relations entre enregistrements de modules SuiteCRM. Permet de lire, créer (via deux méthodes) et supprimer des relations.

## ⚙️ Rôle technique
Hérite de `BaseController`. Expose quatre actions correspondant aux opérations CRUD sur les relationships JSON:API. Délègue entièrement à `RelationshipService`. Distingue deux modes de création : par paramètres directs (`createRelationship`) et par lien (`createRelationshipByLink`).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\CreateRelationshipParams` — paramètres de création de relation
  - `Api\V8\Param\CreateRelationshipByLinkParams` — paramètres de création de relation via lien
  - `Api\V8\Param\DeleteRelationshipParams` — paramètres de suppression de relation
  - `Api\V8\Param\GetRelationshipParams` — paramètres de lecture de relation
  - `Api\V8\Service\RelationshipService` (`Api/V8/Service/RelationshipService.php`) — service métier des relations
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim

## 📤 Sorties / Exports
- `RelationshipController` — classe contrôleur
  - `getRelationship(Request, Response, array, GetRelationshipParams): Response` — GET relation (HTTP 200)
  - `createRelationship(Request, Response, array, CreateRelationshipParams): Response` — POST création (HTTP 201)
  - `createRelationshipByLink(Request, Response, array, CreateRelationshipByLinkParams): Response` — POST création via lien (HTTP 201)
  - `deleteRelationship(Request, Response, array, DeleteRelationshipParams): Response` — DELETE suppression (HTTP 200)

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — routes exactes non visibles dans ce fichier)
- **Appelle :** `RelationshipService::getRelationship()`, `createRelationship()`, `createRelationshipByLink()`, `deleteRelationship()`
- **Position dans le flux global :** gestion des associations entre entités CRM dans le modèle JSON:API

---

## 💡 Points d'attention
- La distinction entre `createRelationship` et `createRelationshipByLink` correspond probablement à deux endpoints REST différents (INCONNU — routes non visibles ici) ; la sémantique exacte de la différence est dans `RelationshipService`.
- `getRelationship` transmet l'objet `$request` complet au service, ce qui peut servir à la pagination.
