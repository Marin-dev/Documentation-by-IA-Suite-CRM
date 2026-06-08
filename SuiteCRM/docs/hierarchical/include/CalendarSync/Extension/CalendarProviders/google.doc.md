# google.php (Extension CalendarProviders)

**Chemin :** `include/CalendarSync/Extension/CalendarProviders/google.php`
**Type :** PHP (fichier de configuration)
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Fichier d'enregistrement du fournisseur Google Calendar dans le systeme CalendarSync. Declare les metadonnees du provider Google (nom, methode d'authentification, classe, chemin) dans le tableau `$calendarProviders` lu par `CalendarProviderRegistry`.

## Role technique

Fichier de configuration PHP pur — aucune classe, uniquement une affectation dans `$calendarProviders['google']`. Inclus dynamiquement par `CalendarProviderRegistry::discoverProviders()`.

---

## Parametres declares

| Parametre | Valeur |
|---|---|
| `name` | `'Google Calendar'` |
| `auth_method` | `'oauth2'` |
| `enabled` | `true` |
| `class` | `'GoogleCalendarProvider'` |
| `file` | `'include/CalendarSync/infrastructure/providers/external/GoogleCalendarProvider.php'` |

## Relations cles

- **Charge par :** `CalendarProviderRegistry::discoverProviders()`
- **Active :** `GoogleCalendarProvider`

---

## Points d'attention

- Pour desactiver temporairement Google Calendar, mettre `'enabled' => false` dans `custom/include/CalendarSync/Extension/CalendarProviders/google.php` (ne pas modifier le fichier core).
