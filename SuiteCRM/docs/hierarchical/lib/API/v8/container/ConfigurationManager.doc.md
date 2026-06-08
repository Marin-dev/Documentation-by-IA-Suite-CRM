# Fichier : ConfigurationManager.php (container)

**Chemin :** `lib/API/v8/container/ConfigurationManager.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory minimaliste qui expose la variable globale `$sugar_config` dans le container DI sous la clé `'ConfigurationManager'`. Permet aux services d'injecter la configuration SuiteCRM sans dépendance directe aux globals PHP.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `ConfigurationManager` | `$sugar_config` (global) | Tableau de configuration SuiteCRM |

---

## Paramètres clés utilisés par les consommateurs

| Clé | Usage |
|---|---|
| `site_url` | Construction des URLs dans les réponses API |
| `list_max_entries_per_page` | Limite par défaut de pagination |

---

## Interactions

**Consommé par :** `ModuleController`, `ModulesLib`, `SchemaController` — via `$this->containers->get('ConfigurationManager')`
