# 📄 factories.php

**Chemin :** `Api/V8/Config/services/factories.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre les deux factories de l'API V8 dans le conteneur DI : `ParamsMiddlewareFactory` (création des middlewares de validation de paramètres de routes) et `ValidatorFactory` (création de closures de validation Symfony).

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\Factory` (namespace) | Contient `ParamsMiddlewareFactory` et `ValidatorFactory` |
| `Psr\Container\ContainerInterface` | Accès au conteneur |
| `Api\Core\Loader\CustomLoader` | Fusion avec factories personnalisées |

---

## Factories enregistrées

| Clé DI | Dépendances injectées |
|---|---|
| `ParamsMiddlewareFactory::class` | `$container` (conteneur entier) |
| `ValidatorFactory::class` | `'Validation'` (instance du validateur Symfony) |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **`ParamsMiddlewareFactory`** est consommée dans `routes.php` : `$paramsMiddlewareFactory->bind(Param\XxxParams::class)`
- **`ValidatorFactory`** est consommée par toutes les classes `Param\Options\*` (via injection dans `BaseOption`)

---

## Notes

- `ParamsMiddlewareFactory` reçoit le conteneur complet (pas seulement un service) afin de résoudre dynamiquement n'importe quelle classe `Param\*` au moment de l'appel `bind()`.
- `ValidatorFactory` dépend du service `'Validation'` défini dans `validators.php` (instance `Symfony\Component\Validator\Validator`).
