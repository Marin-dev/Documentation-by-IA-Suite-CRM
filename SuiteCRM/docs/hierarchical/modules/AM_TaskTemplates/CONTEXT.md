# 📁 AM_TaskTemplates

**Chemin :** `modules/AM_TaskTemplates/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AM_TaskTemplates gère les tâches modèles utilisées dans les templates de projets (`AM_ProjectTemplates`). Chaque tâche modèle définit les caractéristiques d'une tâche type (nom, durée, priorité, prédécesseurs, jalon) qui sera copiée en `ProjectTask` lors de la création d'un projet.

## ⚙️ Responsabilité technique
Bean `AM_TaskTemplates` (hérite de `AM_TaskTemplates_sugar`, classe vide réservée aux personnalisations). Table `am_tasktemplates` lue par `Project::save()` via SQL direct (non via BeanFactory). Champs copiés tels quels vers `ProjectTask`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet tableau de bord pour les tâches modèles | [→ CONTEXT](Dashlets/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AM_TaskTemplates.php` | Bean tâche modèle (classe vide pour personnalisation) | [→ fiche](AM_TaskTemplates.php.doc.md) |
| `vardefs.php` | Schéma de la table `am_tasktemplates` | [→ fiche](vardefs.php.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AM_TaskTemplates_sugar.php` | Classe générée automatiquement par Module Builder |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AM_ProjectTemplates` (relation many-to-many), `SugarBean`
- **Consommé par :** `Project::save()` (SQL direct pour créer des `ProjectTask`), `AM_ProjectTemplatesController::action_create_project()`
- **Flux typique :** Template de projet sélectionné → `Project::save()` lit les `AM_TaskTemplates` via SQL → crée des `ProjectTask` pour le nouveau projet

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir le schéma des tâches modèles | [`vardefs.php`](vardefs.php.doc.md) |
| Personnaliser le bean tâche modèle | [`AM_TaskTemplates.php`](AM_TaskTemplates.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `Project::save()` lit les tâches via SQL brut (contournant les hooks bean) — risque si le schéma change
- Classe `AM_TaskTemplates` vide : toute personnalisation doit être ajoutée ici
