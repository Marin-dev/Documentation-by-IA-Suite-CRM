# Fichier : cookie.php (container)

**Chemin :** `lib/API/v8/container/cookie.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `Slim\Http\Cookies` à partir des cookies de la requête courante et l'enregistre dans le container DI sous la clé `'cookie'`. Permet aux services d'accéder aux cookies de la requête.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `cookie` | `Slim\Http\Cookies` | Gestionnaire de cookies HTTP |

---

## Interactions

- **Consomme :** `$container->get('request')` (objet requête Slim)
- **Consommé par :** INCONNU — aucun consommateur direct identifié dans `lib/API/v8/`
