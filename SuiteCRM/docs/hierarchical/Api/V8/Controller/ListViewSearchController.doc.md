# 📄 ListViewSearchController.php

**Chemin :** `Api/V8/Controller/ListViewSearchController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 exposant l'endpoint de récupération des définitions de recherche d'une vue liste (search defs) pour un module SuiteCRM donné.

## ⚙️ Rôle technique
Hérite de `BaseController`. Contient une seule action `getModuleSearchDefs` qui délègue à `ListViewSearchService::getListViewSearchDefs()` et retourne une réponse JSON:API 200 ou 400 en cas d'erreur. L'objet `ListViewSearchParams` est injecté comme quatrième argument via la `SuiteInvocationStrategy`.

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\ListViewSearchParams` — paramètres validés de la requête
  - `Api\V8\Service\ListViewSearchService` (`Api/V8/Service/ListViewSearchService.php`) — service métier pour la recherche dans les vues listes
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Garde d'entrée :** vérifie `sugarEntry` (ligne 43-45)

## 📤 Sorties / Exports
- `ListViewSearchController` — classe contrôleur
  - `getModuleSearchDefs(Request, Response, array, ListViewSearchParams): Response` — retourne les définitions de recherche JSON:API

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — route exacte non visible dans ce fichier)
- **Appelle :** `ListViewSearchService::getListViewSearchDefs($params)`
- **Position dans le flux global :** point d'entrée HTTP pour les métadonnées de recherche des vues listes

---

## 💡 Points d'attention
- Structure identique à `ListViewController` ; les deux contrôleurs suivent le même patron de délégation vers un service.
- Toutes les exceptions sont converties en réponse 400 sans distinction de type d'erreur.
