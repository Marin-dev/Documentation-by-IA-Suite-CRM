# Fichier : ServerRequestInterface.php (container)

**Chemin :** `lib/API/v8/container/ServerRequestInterface.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `Psr\Http\Message\ServerRequestInterface::class` la **requête** (`request`) du container Slim.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `Psr\Http\Message\ServerRequestInterface::class` | `$container->get('request')` | Objet requête Slim (PSR-7) |

---

## Notes

**Point d'attention :** `ResponseInterface.php` enregistre également sous la même clé `ServerRequestInterface::class` mais retourne `$container->get('response')`. Si les deux fichiers sont chargés, le dernier chargé écrase le premier — comportement potentiellement instable selon l'ordre de chargement.
