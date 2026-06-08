# 📁 History

**Chemin :** `modules/History/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module History fournit le sous-panneau "Historique" affiché sur les enregistrements CRM. Il agrège les appels, réunions, emails, notes et tâches passés liés à un enregistrement dans une vue consolidée.

## ⚙️ Responsabilité technique
Module de configuration des sous-panneaux uniquement. Pas de bean propre, utilise les beans des modules d'activité.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des sous-panneaux | [→ CONTEXT](metadata/CONTEXT.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Tous les modules ayant un historique (Accounts, Contacts, Opportunities, Cases, etc.)
- **Affiche :** Calls, Meetings, Emails, Notes, Tasks (activités passées)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
