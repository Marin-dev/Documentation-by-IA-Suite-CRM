# 📁 Tasks

**Chemin :** `modules/Tasks/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Tasks gère les tâches dans SuiteCRM. Une tâche représente une action à effectuer avec une date d'échéance et un statut. Les tâches sont liées aux enregistrements CRM et apparaissent dans le calendrier. Elles font partie du sous-panneau "Activités".

## ⚙️ Responsabilité technique
Bean `Task` (hérite de `SugarBean`). Table `tasks`. Vue édition personnalisée. Dashlet et vue liste dédiés.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes tâches" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Task.php` | Bean principal des tâches | [→ fiche](Task.php.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.php.doc.md) |
| `TasksQuickCreate.php` | Création rapide de tâche | [→ fiche](TasksQuickCreate.php.doc.md) |
| `MyTasks.php` | Helper pour "Mes tâches" | [→ fiche](MyTasks.php.doc.md) |
| `vardefs.php` | Schéma de la table `tasks` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`
- **Consommé par :** Module Calendar (affichage comme activité), Accounts/Contacts/Leads (relations), AM_ProjectTemplates (tâches projet)
- **Flux typique :** Création tâche → liaison enregistrement parent → apparaît dans calendrier et sous-panneau Activités

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
