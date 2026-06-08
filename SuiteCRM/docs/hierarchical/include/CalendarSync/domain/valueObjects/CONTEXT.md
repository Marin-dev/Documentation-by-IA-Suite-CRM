# 📁 valueObjects

**Chemin :** `include/CalendarSync/domain/valueObjects/`
**Profondeur :** 5
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les value objects du domaine CalendarSync. Actuellement, il héberge `CalendarConnectionTestResult`, qui encapsule le résultat d'un test de connexion à un fournisseur de calendrier externe (succès/échec + message).

## ⚙️ Responsabilité technique
Value objects immuables sans logique métier. Transportent des données structurées entre couches sans effets de bord.

---

## 📂 Contenu

### Sous-dossiers
Aucun.

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarConnectionTestResult.php` | Résultat d'un test de connexion à un provider externe (succès + message) | [→ fiche](CalendarConnectionTestResult.doc.md) |

### Fichiers non documentés (volontairement)
Aucun.

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** rien (value object sans dépendance)
- **Expose :** `CalendarConnectionTestResult` — utilisé par `CalendarSync::testProviderConnectionWithValidation()` et `AbstractCalendarProvider::testCalendarConnection()`
- **Flux typique :** L'utilisateur déclenche un test de connexion depuis l'UI, `CalendarSync` appelle le provider via le registre, le provider retourne un `CalendarConnectionTestResult`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la structure du résultat d'un test de connexion | [`CalendarConnectionTestResult.php`](CalendarConnectionTestResult.doc.md) |

---

## ⚠️ Zones INCONNU
- `CalendarConnectionTestResult` : fiche incomplète — le fichier source n'a pas été entièrement lu. Structure exacte (propriétés, méthodes) à confirmer.
