# 📁 Schedulers

**Chemin :** `modules/Schedulers/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Schedulers gère les tâches planifiées (cron jobs) de SuiteCRM. Chaque scheduler définit une fonction PHP à exécuter selon un intervalle cron étendu (format `min::hr::dates::mon::days`). Déclenche les envois planifiés de rapports, les workflows batch, les emails, etc.

## ⚙️ Responsabilité technique
Bean `Scheduler` (hérite de `SugarBean`). Table `schedulers`. `fireQualified()` vérifie si l'heure courante correspond à l'intervalle. `checkPendingJobs()` soumet les jobs qualifiés dans `SugarJobQueue`. Format cron maison avec `::` comme séparateur.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail, édition, liste | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Scheduler.php` | Bean planificateur de tâche | [→ fiche](Scheduler.doc.md) |
| `_AddJobsHere.php` | Registre des tâches planifiées disponibles | [→ fiche](_AddJobsHere.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `EditView.php` | Vue d'édition (legacy) | [→ fiche](EditView.doc.md) |
| `vardefs.php` | Schéma de la table `schedulers` | [→ fiche](vardefs.doc.md) |
| `field_arrays.php` | Tableaux de champs | [→ fiche](field_arrays.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SchedulersJob`, `SugarJobQueue`, `BeanFactory`, `TimeDate`
- **Consommé par :** `cron.php` (exécution périodique) via `checkPendingJobs()`
- **Flux typique :** `cron.php` → `Scheduler::checkPendingJobs()` → jobs qualifiés → `SugarJobQueue::submitJob()` → exécution

---

## ⚠️ Zones INCONNU
- Format cron maison (`::`) différent du cron Unix standard — parseur complexe
- `catch_up` : comportement non documenté entièrement
- `SugarJobQueue` : implémentation exacte non lue
