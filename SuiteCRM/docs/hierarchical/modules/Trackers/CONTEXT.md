# 📁 Trackers

**Chemin :** `modules/Trackers/`
**Profondeur :** 2
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce module implémente le système de **tracking d'activité utilisateur** de SuiteCRM : navigation dans les modules (breadcrumb), sessions, métriques de performance et accès aux enregistrements. Il alimente les dashlets "Historique récent" et les statistiques d'usage. L'administrateur peut activer ou désactiver chaque type de monitor depuis le panneau d'administration.

## ⚙️ Responsabilité technique
Architecture basée sur le pattern Singleton (`TrackerManager`) + Strategy (`Monitor`/`BlankMonitor`). `TrackerManager` charge la configuration depuis `config.php`, instancie les monitors et les persiste. `Tracker` est le SugarBean mappant la table `tracker`. Deux stores de persistance : `DatabaseStore` (SQL), `SugarLogStore` (fichier log). `BreadCrumbStack` gère la pile de navigation. `Metric` / `Trackable` sont des interfaces/classes de données. `tracker_monitor.php` est le monitor concret.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `monitor/` | Implémentations des monitors (Monitor, BlankMonitor, tracker_monitor) | — |
| `store/` | Stratégies de persistance (DatabaseStore, SugarLogStore, TrackerQueriesDatabaseStore, TrackerSessionsDatabaseStore) | — |
| `language/` | Libellés i18n (en_us) | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `TrackerManager.php` | Singleton orchestrant l'ensemble des monitors (chargement config, dispatch, pause) | — |
| `Tracker.php` | Entité SugarBean mappant la table `tracker` (user_id, module_name, monitor_id) | — |
| `BreadCrumbStack.php` | Gestion de la pile de navigation récente (breadcrumb) | — |
| `Metric.php` | Classe de données pour une métrique de tracking | — |
| `Trackable.php` | Interface/classe de base pour les éléments trackables | — |
| `config.php` | Configuration des monitors disponibles | — |
| `vardefs.php` | Définition des champs de l'entité Tracker | — |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `populateSeedData.php` | Script de données de test |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Administration` (pour récupérer les settings `tracker_*`) ; `BeanFactory` ; toute vue appelant `TrackerManager::getInstance()`.
- **Expose :** `TrackerManager::getInstance()` utilisé globalement dans les vues pour enregistrer les accès modules/enregistrements.
- **Flux typique :** Utilisateur accède à un enregistrement → la vue appelle `TrackerManager::getInstance()->getMonitor(...)` → le monitor sélectionné (Database ou Log) persiste l'accès → le dashlet "Récemment consulté" lit la table `tracker`.

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le point d'entrée du tracking | `TrackerManager.php` |
| Voir comment les données sont stockées en DB | `store/DatabaseStore.php` |
| Modifier la navigation récente (breadcrumb) | `BreadCrumbStack.php` |
| Configurer les monitors activés | `config.php` |
| Comprendre la structure DB de la table tracker | `vardefs.php` |

---

## ⚠️ Zones INCONNU
- La distinction précise entre `TrackerQueriesDatabaseStore` et `TrackerSessionsDatabaseStore` (tables cibles, fréquence) nécessite investigation dans `store/`.
