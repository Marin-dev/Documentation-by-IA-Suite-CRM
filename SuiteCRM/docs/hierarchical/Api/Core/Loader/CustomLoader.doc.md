# 📄 CustomLoader.php

**Chemin :** `Api/Core/Loader/CustomLoader.php`
**Type :** `PHP`
**Catégorie :** helper / loader
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Fournit le mécanisme de surcharge et d'extension de la configuration API par des fichiers personnalisés ("custom"). Il permet aux intégrateurs de SuiteCRM de modifier les paramètres de configuration (tableaux) et d'ajouter des routes supplémentaires sans modifier les fichiers du core, en déposant des fichiers dans `custom/application/Ext/Api/V8/`.

## ⚙️ Rôle technique

Classe statique avec deux fonctionnalités principales :
- `mergeCustomArray()` : tente d'inclure un fichier custom qui doit retourner un tableau, puis fusionne ce tableau avec le tableau de base via `arrayMerge()` (fusion profonde récursive supportant tableaux indexés et associatifs).
- `loadCustomRoutes()` : inclut un fichier de routes custom dans le contexte de l'application Slim (`$app` doit être en scope).
- Un code d'erreur statique (`$lastError`) trace le dernier statut sans lever d'exception pour les cas non-bloquants (fichier absent).

---

## 📥 Entrées / Dépendances

- **Imports principaux :**
  - `Exception` (PHP natif) — levée si le fichier custom ne retourne pas un tableau
  - `LoggerManager` (SuiteCRM interne) — log en mode debug si le fichier custom est absent
  - `Slim\App` — paramètre de `loadCustomRoutes()`

## 📤 Sorties / Exports

| Symbole | Type | Rôle |
|---|---|---|
| `ERR_NO_ERROR` | constante int (0) | Pas d'erreur |
| `ERR_FILE_NOT_FOUND` | constante int (1) | Fichier custom absent |
| `ERR_ROUTE_FILE_NOT_FOUND` | constante int (2) | Fichier de routes custom absent |
| `ERR_WRONG_CUSTOM_FORMAT` | constante int (3) | Fichier custom ne retourne pas un tableau |
| `mergeCustomArray($array, $customFile)` | méthode statique | Fusionne un tableau de base avec un fichier custom |
| `loadCustomRoutes(App $app, $customRoutesFile)` | méthode statique | Charge un fichier de routes custom dans l'app Slim |
| `arrayMerge($arrays)` | méthode statique | Fusion profonde de tableaux multidimensionnels |
| `getLastError()` / `setCustomPath()` / `getCustomPath()` | méthodes statiques | Accesseurs utilitaires |

**Consommateurs identifiés dans le repo :**
- `Api/Core/Config/slim.php` — appelle `mergeCustomArray()` pour permettre la surcharge des settings Slim
- Nombreux fichiers dans `Api/V8/Config/services/` — utilisent `mergeCustomArray()` pour chaque service
- `Api/V8/Config/routes.php` — utilise `loadCustomRoutes()`
- `Api/V8/Config/services.php` — utilise `mergeCustomArray()`

## 🔗 Relations clés

- **Appelé par :** `slim.php`, tous les fichiers de services V8, `routes.php`
- **Appelle :** `LoggerManager::getLogger()->debug()`, `file_exists()`, `include`
- **Position dans le flux global :** invoqué pendant le chargement de la configuration, après la détermination des chemins de base

---

## 💡 Points d'attention

- `$lastError` est réinitialisé à chaque appel à `getLastError()` (effet de bord) — appeler `getLastError()` deux fois de suite ne donne pas le même résultat.
- Le chemin custom par défaut est `custom/application/Ext/Api/V8/` — relatif au répertoire de travail courant, qui est modifié par `chdir()` dans `app.php`.
- `loadCustomRoutes()` utilise `include` sans variable de retour — les routes sont enregistrées par effet de bord via la variable `$app` qui doit exister dans le scope appelant.
- La fusion `arrayMerge()` ne gère pas les clés mixtes entier/string de manière standard : les clés entières sont toujours appendées (jamais écrasées).
