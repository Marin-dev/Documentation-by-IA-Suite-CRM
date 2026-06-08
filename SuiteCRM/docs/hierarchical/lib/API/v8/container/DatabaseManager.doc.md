# Fichier : DatabaseManager.php (container)

**Chemin :** `lib/API/v8/container/DatabaseManager.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui expose l'instance singleton de `DBManagerFactory` dans le container DI sous la clé `'DatabaseManager'`. Fournit l'accès à la base de données SuiteCRM aux services API.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `DatabaseManager` | `DBManagerFactory::getInstance()` | Gestionnaire de BDD SuiteCRM (singleton) |

---

## Interactions

**Consommé par :** `ModulesLib::getSorting()` — pour quoter les noms de champs dans les clauses ORDER BY.
