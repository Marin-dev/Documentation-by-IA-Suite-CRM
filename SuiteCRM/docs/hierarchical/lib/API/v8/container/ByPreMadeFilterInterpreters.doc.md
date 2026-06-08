# Fichier : ByPreMadeFilterInterpreters.php (container)

**Chemin :** `lib/API/v8/container/ByPreMadeFilterInterpreters.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'ByPreMadeFilterInterpreters'` un tableau d'interpréteurs de filtres pré-fabriqués (ex. : "today", "this week"). Actuellement, contient uniquement `Today`.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Type | Contenu |
|---|---|---|
| `ByPreMadeFilterInterpreters` | `ByPreMadeFilterInterpreter[]` | `[Today]` |

---

## Notes

Identique dans le contenu à `ByAttributesFilterInterpreters.php` — les deux enregistrent `Today($container)`. Cela semble être une duplication ou une organisation incomplète.
