# json_file.php (Extension CalendarProviders)

**Chemin :** `include/CalendarSync/Extension/CalendarProviders/json_file.php`
**Type :** PHP (fichier de configuration)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fichier d'enregistrement du fournisseur de test "JSON File Calendar". Ce provider est desactive (`enabled: false`) et sert uniquement a des fins de tests de developpement.

## Parametres declares

| Parametre | Valeur |
|---|---|
| `name` | `'Test JSON File Calendar'` |
| `auth_method` | `'api_key'` |
| `enabled` | `false` |
| `class` | `'JsonFileCalendarProvider'` |
| `file` | `'include/CalendarSync/infrastructure/providers/external/JsonFileCalendarProvider.php'` |

## Points d'attention

- Desactive par defaut — ne pas activer en production. Sert uniquement pour les tests.
