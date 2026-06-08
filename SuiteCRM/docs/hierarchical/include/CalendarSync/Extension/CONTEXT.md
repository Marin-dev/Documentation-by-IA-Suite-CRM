# 📁 Extension

**Chemin :** `include/CalendarSync/Extension/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les fichiers d'extension du module CalendarSync. Il suit le pattern d'extension SuiteCRM (fichiers inclus dynamiquement) pour déclarer les fournisseurs de calendrier disponibles. C'est le point de configuration extensible des providers, surchargeable via `custom/`.

## ⚙️ Responsabilité technique
Dossier de configuration pure — fichiers PHP inclus dynamiquement par `CalendarProviderRegistry`. Extensible sans modification du code core via `custom/include/CalendarSync/Extension/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarProviders/` | Fichiers de déclaration des providers de calendrier (Google, CalDAV, JSON test) | [→ CONTEXT](CalendarProviders/CONTEXT.md) |

### Fichiers documentés
Aucun fichier directement dans `Extension/`.

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** rien (configuration pure)
- **Expose :** déclarations de providers dans `$calendarProviders` — consommées par `CalendarProviderRegistry`
- **Flux typique :** `CalendarProviderRegistry::discoverProviders()` parcourt ce dossier et `custom/` pour charger tous les providers disponibles.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir quels providers sont déclarés | [`CalendarProviders/`](CalendarProviders/CONTEXT.md) |
| Ajouter un nouveau provider | Créer un fichier dans `custom/include/CalendarSync/Extension/CalendarProviders/` |

---

## ⚠️ Zones INCONNU
Aucun.
