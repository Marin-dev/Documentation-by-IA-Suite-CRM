# 📁 AM_ProjectTemplates

**Chemin :** `modules/AM_ProjectTemplates/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AM_ProjectTemplates gère les modèles de projets réutilisables dans SuiteCRM. Un template définit une structure de projet (tâches, ressources, dépendances) qui peut être copiée lors de la création d'un nouveau projet. Il supporte le calcul des dates selon les heures ouvrables (AOBH_BusinessHours).

## ⚙️ Responsabilité technique
Bean `AM_ProjectTemplates` (hérite de `AM_ProjectTemplates_sugar`). Le contrôleur gère la création d'un projet à partir du template avec sélection des tâches à copier. La vue principale est un diagramme de Gantt interactif avec assets JS/CSS dédiés. Architecture miroir du module `Project`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet tableau de bord pour les templates | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `views/` | Vue Gantt du template de projet | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AM_ProjectTemplates.php` | Bean modèle de projet réutilisable | [→ fiche](AM_ProjectTemplates.php.doc.md) |
| `controller.php` | Contrôleur MVC : vue Gantt et création de projet depuis template | [→ fiche](controller.php.doc.md) |
| `Save.php` | Point d'entrée action Save, redirige vers Gantt | [→ fiche](Save.php.doc.md) |
| `vardefs.php` | Schéma de la table `am_projecttemplates` | [→ fiche](vardefs.php.doc.md) |
| `gantt.php` | Classe helper de rendu du diagramme Gantt | [→ fiche](gantt.php.doc.md) |
| `project_table.php` | Rendu HTML du tableau de tâches (INCONNU partiel) | [→ fiche](project_table.php.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.php.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AM_ProjectTemplates_sugar.php` | Classe générée automatiquement par Module Builder |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOBH_BusinessHours` (calcul des dates), module `Project` (création de projets), `AM_TaskTemplates` (tâches liées)
- **Expose :** Templates réutilisables pour `Project::save()`, dashlet tableau de bord
- **Flux typique :** Utilisateur choisit un template → `controller::action_create_project()` → copie des tâches `AM_TaskTemplates` → instancie un `Project` → sauvegarde

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la logique de création de projet depuis template | [`controller.php`](controller.php.doc.md) |
| Voir le bean et la synchronisation des ressources | [`AM_ProjectTemplates.php`](AM_ProjectTemplates.php.doc.md) |
| Consulter le schéma de données | [`vardefs.php`](vardefs.php.doc.md) |
| Modifier le rendu Gantt | [`views/view.ganttchart.php`](views/view.ganttchart.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `AM_ProjectTemplates::save()` et `controller::action_create_project()` : duplication de logique de calcul de dates avec `Project::save()` — risque de divergence
- `echo $sql;` dans `AM_ProjectTemplates::save()` (lignes 148, 171) : sortie HTML non voulue en production
- `project_table.php` : contenu non entièrement lu
