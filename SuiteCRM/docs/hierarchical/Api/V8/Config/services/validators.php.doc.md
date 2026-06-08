# 📄 validators.php

**Chemin :** `Api/V8/Config/services/validators.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Enregistre l'instance du validateur Symfony (`Symfony\Component\Validator\Validator`) sous la clé `'Validation'` dans le conteneur DI. Ce validateur est la base de toute validation des paramètres de requête de l'API V8.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\Core\Loader\CustomLoader` | Fusion avec validators personnalisés |
| `Symfony\Component\Validator\ValidatorBuilder` | Builder Symfony pour créer l'instance validator |

---

## Services enregistrés

| Clé DI | Type retourné | Description |
|---|---|---|
| `'Validation'` | `Symfony\Component\Validator\ValidatorInterface` | Instance du validateur Symfony (annotations non activées) |

---

## Particularité technique

Le fichier inclut manuellement le fichier `ValidatorBuilder.php` du vendor Symfony via `include_once` (ligne 5). Cela suggère que l'autoloader n'est peut-être pas disponible au moment du chargement de ce fichier, ou que c'est une protection de compatibilité.

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **Consommé par :** `factories.php` → `ValidatorFactory::class` (qui reçoit `$container->get('Validation')`)
- **Utilisé transitivement par :** toutes les classes `Param\Options\*` via `ValidatorFactory`

---

## Notes

- Le validateur est créé sans activation des annotations Doctrine ni de cache — configuration minimale.
- L'`include_once` manuel est inhabituel et peut indiquer une dette technique ou un problème d'autoloading dans certains contextes.
