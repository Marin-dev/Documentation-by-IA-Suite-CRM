# 📄 ModuleController.php

**Chemin :** `Api/V8/Controller/ModuleController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur CRUD principal de l'API V8. Il gère les opérations de lecture, création, mise à jour et suppression d'enregistrements sur n'importe quel module SuiteCRM exposé par l'API.

## ⚙️ Rôle technique
Hérite de `BaseController`. Expose cinq actions correspondant aux opérations CRUD REST : GET (enregistrement unique), GET (liste), POST (création), PATCH/PUT (mise à jour), DELETE. Chaque action délègue à `ModuleService` et retourne une réponse JSON:API. Les codes de retour sont 200 (lecture/suppression), 201 (création/mise à jour) ou 400 (erreur).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\CreateModuleParams` — paramètres de création
  - `Api\V8\Param\DeleteModuleParams` — paramètres de suppression
  - `Api\V8\Param\GetModuleParams` — paramètres de lecture d'un enregistrement
  - `Api\V8\Param\GetModulesParams` — paramètres de lecture de liste
  - `Api\V8\Param\UpdateModuleParams` — paramètres de mise à jour
  - `Api\V8\Service\ModuleService` (`Api/V8/Service/ModuleService.php`) — service métier CRUD
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim

## 📤 Sorties / Exports
- `ModuleController` — classe contrôleur
  - `getModuleRecord(Request, Response, array, GetModuleParams): Response` — GET un enregistrement (HTTP 200)
  - `getModuleRecords(Request, Response, array, GetModulesParams): Response` — GET liste d'enregistrements (HTTP 200)
  - `createModuleRecord(Request, Response, array, CreateModuleParams): Response` — POST création (HTTP 201)
  - `updateModuleRecord(Request, Response, array, UpdateModuleParams): Response` — PATCH mise à jour (HTTP 201)
  - `deleteModuleRecord(Request, Response, array, DeleteModuleParams): Response` — DELETE suppression (HTTP 200)

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — routes exactes non visibles dans ce fichier)
- **Appelle :** `ModuleService::getRecord()`, `ModuleService::getRecords()`, `ModuleService::createRecord()`, `ModuleService::updateRecord()`, `ModuleService::deleteRecord()`
- **Position dans le flux global :** contrôleur central de l'API REST V8 pour la manipulation des données CRM

---

## 💡 Points d'attention
- `updateModuleRecord` retourne HTTP 201 (Created) au lieu de 200 (OK) — comportement potentiellement non conforme à la sémantique REST standard (PATCH devrait retourner 200 ou 204).
- `getModuleRecords` transmet l'objet `$request` complet au service (pour accès aux query params de pagination/filtrage), contrairement à `getModuleRecord` qui ne passe que le chemin URI.
- Toutes les exceptions sont converties en 400, sans distinction entre erreurs métier (404, 422) et erreurs serveur (500).
