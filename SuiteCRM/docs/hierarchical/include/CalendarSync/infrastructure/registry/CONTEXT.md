# 📁 registry

**Chemin :** `include/CalendarSync/infrastructure/registry/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le registre des fournisseurs de calendrier. Il permet la découverte automatique des providers disponibles (Google, CalDAV, JSON, interne SuiteCRM) depuis des fichiers d'extension PHP, et expose des méthodes pour instancier un provider pour un compte donné.

## ⚙️ Responsabilité technique
Pattern Registry avec cache statique de classe. Charge les définitions depuis `include/CalendarSync/Extension/CalendarProviders/` (et `custom/`), maintient un cache statique pour éviter les redécouvertes, et synchronise les types disponibles avec le fichier de langue de l'UI.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarProviderRegistry.php` | Registre central des providers de calendrier — découverte, cache, instanciation | [→ fiche](CalendarProviderRegistry.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `CalendarProviderType`, `CalendarProviderTypeFactory`, `CalendarProviderInstanceFactory`, `ModuleInstaller`, `write_override_label_to_file()`
- **Expose :** `getProviderForAccount()`, `getInternalProviderForAccount()`, `getCalendarSourceTypes()`, `findEnabled()`
- **Flux typique :** `CalendarSyncOrchestrator` appelle `CalendarProviderRegistry::getProviderForAccount()` pour obtenir l'instance du provider externe d'un compte, puis appelle les méthodes CRUD sur ce provider.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre comment les providers sont découverts et mis en cache | [`CalendarProviderRegistry.php`](CalendarProviderRegistry.doc.md) |

---

## ⚠️ Zones INCONNU
- Le `writeCalendarSourceTypesToExtension()` est appelé à chaque instanciation — impact performance si fréquent.
- Cache statique : non réinitialisé en cas de modification de providers sans redémarrage PHP.
