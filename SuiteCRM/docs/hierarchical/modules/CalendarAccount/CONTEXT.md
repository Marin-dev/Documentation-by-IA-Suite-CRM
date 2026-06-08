# 📁 CalendarAccount

**Chemin :** `modules/CalendarAccount/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module CalendarAccount gère les comptes de synchronisation calendrier (Google Calendar, Outlook, etc.) pour les utilisateurs SuiteCRM. Permet de configurer la synchronisation bidirectionnelle des événements entre SuiteCRM et des services calendrier externes.

## ⚙️ Responsabilité technique
Bean `CalendarAccount` (hérite de `SugarBean`). Services dédiés pour ACL et validation. Vues CRUD standard.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition | [→ CONTEXT](views/CONTEXT.md) |
| `services/` | Services ACL et validation | [→ CONTEXT](services/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `CalendarAccount.php` | Bean compte de synchronisation calendrier | [→ fiche](CalendarAccount.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** APIs Google Calendar, Outlook (via EAPM)
- **Consommé par :** Module Calendar (synchronisation des événements)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
