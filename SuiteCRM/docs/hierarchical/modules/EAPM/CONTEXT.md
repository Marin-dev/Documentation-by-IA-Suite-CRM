# 📁 EAPM

**Chemin :** `modules/EAPM/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module EAPM (External Accounts Plugin Manager) gère les comptes de services externes intégrés à SuiteCRM (Google Drive, GoToMeeting, WebEx, etc.). Permet aux utilisateurs de configurer leurs identifiants pour les services externes utilisés dans les réunions et le calendrier.

## ⚙️ Responsabilité technique
Bean `EAPM` (hérite de `SugarBean`). Consommé par le module Calendar (réunions externes) et les connecteurs d'API.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `EAPM.php` | Bean compte de service externe | [→ fiche](EAPM.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `CheckLogins.php` | Vérification des identifiants | [→ fiche](CheckLogins.php.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `Meeting::save()` (réunions GoToMeeting/WebEx), module Calendar
- **Consomme :** `ExternalAPIFactory`

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
