# 📄 ApiConfig.php

**Chemin :** `Api/Core/Config/ApiConfig.php`
**Type :** `PHP`
**Catégorie :** config
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel

Classe de configuration centrale de l'API SuiteCRM. Elle déclare les chemins vers les fichiers de configuration Slim, les fichiers de déclaration des services (conteneurs DI) et les fichiers de routes. Elle expose aussi les chemins des clés OAuth2. Elle constitue le point d'entrée de toute configuration du noyau API.

## ⚙️ Rôle technique

Classe statique pure (pas d'instanciation), utilisant des propriétés statiques privées pour centraliser les tableaux de chemins relatifs vers les fichiers de configuration. Les getters statiques permettent aux loaders (`ContainerLoader`, `RouteLoader`) de récupérer ces listes. L'attribut `#[\AllowDynamicProperties]` indique une compatibilité PHP 8.2+.

---

## 📥 Entrées / Dépendances

- **Imports principaux :** aucun (pas d'import externe)
- **Variables d'environnement utilisées :** aucune directement
- **Arguments / paramètres d'entrée :** aucun (configuration inline)

## 📤 Sorties / Exports

| Symbole | Type | Rôle |
|---|---|---|
| `getSlimSettings()` | méthode statique | Retourne `['Api/Core/Config/slim.php']` |
| `getContainers()` | méthode statique | Retourne `['Api/V8/Config/services.php']` |
| `getRoutes()` | méthode statique | Retourne `['Api/V8/Config/routes.php']` |
| `getDebugExceptions()` | méthode statique | Retourne le flag de débogage des exceptions (false par défaut) |
| `OAUTH2_PRIVATE_KEY` | constante | Chemin vers la clé privée OAuth2 : `Api/V8/OAuth2/private.key` |
| `OAUTH2_PUBLIC_KEY` | constante | Chemin vers la clé publique OAuth2 : `Api/V8/OAuth2/public.key` |

**Consommateurs identifiés dans le repo :**
- `Api/Core/Loader/ContainerLoader.php` — appelle `getSlimSettings()` et `getContainers()`
- `Api/Core/Loader/RouteLoader.php` — appelle `getRoutes()`
- `Api/V8/JsonApi/Response/ErrorResponse.php` — utilise `getDebugExceptions()`
- `Api/V8/Config/services/middlewares.php` — référence les constantes OAuth2

## 🔗 Relations clés

- **Appelé par :** `ContainerLoader`, `RouteLoader`, `ErrorResponse`, `middlewares.php`
- **Appelle :** rien
- **Position dans le flux global :** registre de configuration statique, consulté au démarrage de l'application avant toute initialisation de conteneur ou de routes

---

## 💡 Points d'attention

- Le flag `$debugExceptions` est codé en dur à `false` et n'est pas modifiable depuis l'extérieur sans sous-classer ou éditer le fichier directement — pas de configuration dynamique.
- Les chemins dans `$slimSettings`, `$containers` et `$routes` sont relatifs à `$GLOBALS['BASE_DIR']` (résolution effectuée dans `ConfigResolver`).
- Commentaire : `// we still support 5.5.9` suggère une contrainte de compatibilité PHP historique.
