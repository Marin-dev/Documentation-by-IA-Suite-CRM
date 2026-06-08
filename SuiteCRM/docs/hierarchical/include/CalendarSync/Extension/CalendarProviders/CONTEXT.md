# 📁 CalendarProviders

**Chemin :** `include/CalendarSync/Extension/CalendarProviders/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les fichiers d'enregistrement des fournisseurs de calendrier disponibles dans SuiteCRM. Chaque fichier déclare les métadonnées d'un provider (nom, méthode d'authentification, classe PHP, chemin, statut d'activation) dans le tableau `$calendarProviders` lu par `CalendarProviderRegistry`.

## ⚙️ Responsabilité technique
Fichiers de configuration PHP purs (pas de classes). Inclus dynamiquement par `CalendarProviderRegistry::discoverProviders()`. La surcharge via `custom/include/CalendarSync/Extension/CalendarProviders/` est supportée.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `google.php` | Enregistrement du provider Google Calendar (OAuth2, activé) | [→ fiche](google.doc.md) |
| `caldav_basic.php` | Enregistrement du provider CalDAV avec authentification basique (activé) | [→ fiche](caldav_basic.doc.md) |
| `json_file.php` | Enregistrement du provider JSON de test (désactivé — développement uniquement) | [→ fiche](json_file.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** rien (fichiers de configuration)
- **Expose :** entrées dans `$calendarProviders` — lues par `CalendarProviderRegistry`
- **Flux typique :** Au démarrage du registry, `discoverProviders()` inclut chacun de ces fichiers, peuplant le tableau des providers disponibles.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Ajouter ou désactiver Google Calendar | [`google.php`](google.doc.md) |
| Ajouter ou désactiver CalDAV | [`caldav_basic.php`](caldav_basic.doc.md) |
| Comprendre le provider de test JSON | [`json_file.php`](json_file.doc.md) |

---

## ⚠️ Zones INCONNU
- Pour désactiver un provider sans modifier le code core, créer/modifier le fichier correspondant dans `custom/include/CalendarSync/Extension/CalendarProviders/`.
- `json_file.php` est désactivé par défaut — ne pas activer en production.
