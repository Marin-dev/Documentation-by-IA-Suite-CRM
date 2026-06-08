# 📁 views

**Chemin :** `modules/AM_ProjectTemplates/views/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les vues du module AM_ProjectTemplates. Fournit l'interface d'affichage du diagramme de Gantt pour les templates de projets.

## ⚙️ Responsabilité technique
Classe PHP héritant de `ViewDetail`, intègre des assets CSS/JS spécifiques et injecte des données JSON pour le rendu du diagramme de Gantt côté client.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| — | Aucun sous-dossier | — |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `view.ganttchart.php` | Vue du diagramme de Gantt d'un template de projet | [→ fiche](view.ganttchart.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AM_ProjectTemplates` bean, `DBManagerFactory`, assets JS/CSS `modules/AM_ProjectTemplates/js/`
- **Appelé par :** `AM_ProjectTemplatesController::action_view_GanttChart()`
- **Flux typique :** Requête `action=view_GanttChart` → contrôleur → `view.ganttchart.php` → rendu HTML + données JSON

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Modifier la vue Gantt du template | [`view.ganttchart.php`](view.ganttchart.php.doc.md) |

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
