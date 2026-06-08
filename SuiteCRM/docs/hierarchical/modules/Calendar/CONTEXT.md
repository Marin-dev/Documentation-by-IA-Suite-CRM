# 📁 Calendar

**Chemin :** `modules/Calendar/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Calendar gère le calendrier utilisateur dans SuiteCRM. Il affiche les activités (Réunions, Appels, Tâches, Événements FP_events) selon différentes vues (jour, semaine, mois, vue partagée). Il supporte les préférences utilisateur pour les heures d'affichage et la vue partagée multi-utilisateurs.

## ⚙️ Responsabilité technique
`Calendar.php` orchestre le chargement des activités via `CalendarActivity`. `CalendarDisplay` et `CalendarGrid` gèrent le rendu HTML/Smarty. Vues AJAX pour les interactions dynamiques. Dashlet calendrier pour le tableau de bord. Contrainte 1970-2037 (timestamp Unix 32 bits).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues AJAX/JSON du calendrier | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet calendrier | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Calendar.php` | Orchestrateur principal du calendrier | [→ fiche](Calendar.doc.md) |
| `CalendarActivity.php` | Requêtes DB pour charger les activités | [→ fiche](CalendarActivity.doc.md) |
| `CalendarDisplay.php` | Rendu HTML/Smarty du calendrier | [→ fiche](CalendarDisplay.doc.md) |
| `CalendarGrid.php` | Construction de la grille du calendrier | [→ fiche](CalendarGrid.doc.md) |
| `CalendarUtils.php` | Utilitaires de calcul de dates | [→ fiche](CalendarUtils.doc.md) |
| `controller.php` | Contrôleur MVC du module | [→ fiche](controller.doc.md) |
| `processScreenSize.php` | Gestion de la taille d'écran | [→ fiche](processScreenSize.doc.md) |
| `action_view_map.php` | Mapping actions → vues | [→ fiche](action_view_map.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Modules Meetings, Calls, Tasks, FP_events (activités à afficher)
- **Consommé par :** Tableau de bord (`CalendarDashlet`), module iCals
- **Flux typique :** Requête calendrier → `Calendar` → `CalendarActivity::get_activities()` → `CalendarDisplay` → rendu Smarty

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'orchestration du calendrier | [`Calendar.php`](Calendar.doc.md) |
| Voir comment les activités sont chargées | [`CalendarActivity.php`](CalendarActivity.doc.md) |
| Comprendre le rendu du calendrier | [`CalendarDisplay.php`](CalendarDisplay.doc.md) |

---

## ⚠️ Zones INCONNU
- Validation d'année limitée à 1970-2037 (contrainte timestamp Unix 32 bits)
- `process_sync_to_outlook('all')` : peut être très lourd sur de grandes instances
