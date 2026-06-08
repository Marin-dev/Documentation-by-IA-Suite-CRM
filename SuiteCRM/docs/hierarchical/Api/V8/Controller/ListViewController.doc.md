# 📄 ListViewController.php

**Chemin :** `Api/V8/Controller/ListViewController.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Contrôleur de l'API V8 exposant l'endpoint de récupération des définitions de colonnes d'une vue liste (list view) pour un module SuiteCRM donné.

## ⚙️ Rôle technique
Hérite de `BaseController`. Contient une seule action `getListViewColumns` qui délègue à `ListViewService::getListViewDefs()` et retourne une réponse JSON:API 200 ou 400 en cas d'erreur. L'objet `ListViewColumnsParams` est injecté via la `SuiteInvocationStrategy` (quatrième argument).

---

## 📥 Entrées / Dépendances
- **Imports principaux :**
  - `Api\V8\Param\ListViewColumnsParams` — paramètres validés de la requête (module cible, etc.)
  - `Api\V8\Service\ListViewService` (`Api/V8/Service/ListViewService.php`) — service métier pour les vues listes
  - `Slim\Http\Request` / `Slim\Http\Response` — objets HTTP Slim
- **Garde d'entrée :** vérifie `sugarEntry` (ligne 43-45)

## 📤 Sorties / Exports
- `ListViewController` — classe contrôleur
  - `getListViewColumns(Request, Response, array, ListViewColumnsParams): Response` — retourne les définitions de colonnes JSON:API

## 🔗 Relations clés
- **Appelé par :** routeur Slim (INCONNU — route exacte non visible dans ce fichier)
- **Appelle :** `ListViewService::getListViewDefs($params)`
- **Position dans le flux global :** point d'entrée HTTP pour les métadonnées de vues listes

---

## 💡 Points d'attention
- Toutes les exceptions sont attrapées et converties en réponse 400 ; aucune distinction entre erreurs métier et erreurs système.
- L'injection de `ListViewColumnsParams` dépend de la `SuiteInvocationStrategy` et du `ParamsMiddleware`.
