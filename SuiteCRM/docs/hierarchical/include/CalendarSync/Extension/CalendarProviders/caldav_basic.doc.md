# caldav_basic.php (Extension CalendarProviders)

**Chemin :** `include/CalendarSync/Extension/CalendarProviders/caldav_basic.php`
**Type :** PHP (fichier de configuration)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fichier d'enregistrement du fournisseur CalDAV (authentification basique) dans le systeme CalendarSync. Declare les metadonnees du provider CalDAV dans le tableau `$calendarProviders` lu par `CalendarProviderRegistry`.

## Role technique

Fichier de configuration PHP pur. Inclus dynamiquement par `CalendarProviderRegistry::discoverProviders()`.

---

## Parametres declares

| Parametre | Valeur |
|---|---|
| `name` | `'CalDAV'` |
| `auth_method` | `'basic'` |
| `enabled` | `true` |
| `class` | `'CalDAVProvider'` |
| `file` | `'include/CalendarSync/infrastructure/providers/external/CalDAVProvider.php'` |

## Relations cles

- **Charge par :** `CalendarProviderRegistry::discoverProviders()`
- **Active :** `CalDAVProvider`

---

## Points d'attention

- Auth `basic` : necessite `username` et `password` — champs sensibles a proteger dans la configuration du compte.
