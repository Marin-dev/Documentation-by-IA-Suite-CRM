# 📁 SchedulersJobs

**Chemin :** `modules/SchedulersJobs/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module représente les **jobs de la file d'attente** du planificateur (Schedulers). Chaque `SchedulersJob` est un travail unitaire créé par un scheduler ou par un client externe, avec un statut (queued, running, done), une résolution (success, failure, partial) et une cible d'exécution (URL ou nom de fonction). Il gère le rejeu en cas d'échec (`requeue`, `retry_count`) et l'historique des messages.

## ⚙️ Responsabilité technique
La classe `SchedulersJob` étend `Basic` et mappe une table de file d'attente. Elle définit des constantes de statut (`JOB_STATUS_*`) et de résolution (`JOB_SUCCESS`, `JOB_FAILURE`, etc.). Le module ne possède pas de vue propre (pas de controller ni de views) — il est manipulé programmatiquement par le système de planification. Un sous-panneau `metadata/subpanels/default.php` l'expose depuis le module `Schedulers`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Libellés i18n (en_us) | — |
| `metadata/subpanels/` | Définition sous-panneau pour Schedulers | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `SchedulersJob.php` | Entité de file d'attente des jobs planifiés (statuts, résolutions, retry, target) | — |
| `vardefs.php` | Définition des champs de l'entité | — |
| `field_arrays.php` | Tableaux de colonnes DB | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `metadata/subpanels/default.php` | Définition de sous-panneau standard |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module `Schedulers` (qui crée les jobs) ; système cron (`run_job.php`) qui exécute les jobs.
- **Expose :** Entité `SchedulersJob` et ses constantes de statut/résolution, utilisées par l'infrastructure de planification.
- **Flux typique :** Un scheduler déclenche la création d'un `SchedulersJob` (status=queued) → `run_job.php` le récupère, l'exécute (status=running) → met à jour la résolution (success/failure) → (optionnel) requeue si `$requeue=true`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre les statuts et résolutions d'un job | `SchedulersJob.php` |
| Consulter la structure DB de la table des jobs | `vardefs.php` |
| Voir comment les jobs sont exposés dans l'UI Schedulers | `metadata/subpanels/default.php` |

---

## ⚠️ Zones INCONNU
- Le mécanisme exact de `requeue` et la gestion de `failure_count` vs `retry_count` nécessitent investigation dans le code d'exécution (`run_job.php`, hors module).
