# Fichier : ResponseInterface.php (container)

**Chemin :** `lib/API/v8/container/ResponseInterface.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `Psr\Http\Message\ServerRequestInterface::class` la **réponse** (`response`) du container Slim. Attention : le nom de fichier est `ResponseInterface.php` mais la clé est `ServerRequestInterface::class` — il s'agit probablement d'une erreur de mapping ou d'un fichier qui retourne la réponse sous une mauvaise clé.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `Psr\Http\Message\ServerRequestInterface::class` | `$container->get('response')` | Objet réponse Slim (PSR-7) |

---

## Notes

**Point d'attention :** le nom de fichier `ResponseInterface.php` laisse attendre une binding de `ResponseInterface`, mais la clé utilisée est `ServerRequestInterface::class`. Cela peut être une erreur ou un artefact de développement. `ServerRequestInterface.php` fait la même chose mais avec `$container->get('request')`. Cette duplication/confusion peut causer des bugs si un service résout `ServerRequestInterface` et obtient la réponse au lieu de la requête.
