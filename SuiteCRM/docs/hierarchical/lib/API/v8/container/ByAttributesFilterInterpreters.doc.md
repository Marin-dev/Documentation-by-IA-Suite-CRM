# Fichier : ByAttributesFilterInterpreters.php (container)

**Chemin :** `lib/API/v8/container/ByAttributesFilterInterpreters.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui enregistre dans le container DI sous la clé `'ByAttributesInterpreters'` un tableau d'interpréteurs de filtres par attributs. Actuellement, contient uniquement `Today` (filtre pré-fabriqué).

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Type | Contenu |
|---|---|---|
| `ByAttributesInterpreters` | `ByAttributesFilterInterpreter[]` | `[Today]` |

---

## Notes

Le nom du fichier (`ByAttributesFilterInterpreters`) et la clé container (`ByAttributesInterpreters`) ne correspondent pas exactement. Le contenu (`Today`) ressemble à un filtre pré-fabriqué plutôt qu'à un interpréteur par attribut — possible confusion avec `ByPreMadeFilterInterpreters`.
