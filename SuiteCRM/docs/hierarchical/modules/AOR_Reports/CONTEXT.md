# 📁 AOR_Reports

**Chemin :** `modules/AOR_Reports/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOR_Reports (Advanced OpenReports) est le moteur de rapports configurables de SuiteCRM. Il permet de créer des rapports personnalisés sur n'importe quel module avec sélection de colonnes, filtres, agrégations, tri et groupement. Les résultats sont affichables en HTML, exportables en CSV et PDF, et visualisables sous forme de graphiques.

## ⚙️ Responsabilité technique
Bean `AOR_Report` (hérite de `Basic`) qui construit dynamiquement des requêtes SQL (SELECT/JOIN/WHERE/GROUP BY/ORDER BY). Dépend de `AOR_Fields`, `AOR_Conditions`, `AOR_Charts` pour les lignes enfants. Protège les accès via `ACLController`. Utilisé par le scheduler `AOR_Scheduled_Reports` pour l'envoi automatique.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition du rapport | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet tableau de bord pour les rapports | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOR_Report.php` | Bean principal du moteur de rapports | [→ fiche](AOR_Report.doc.md) |
| `aor_utils.php` | Utilitaires : fonctions SQL autorisées, périodes | [→ fiche](aor_utils.doc.md) |
| `controller.php` | Contrôleur MVC du module | [→ fiche](controller.doc.md) |
| `vardefs.php` | Schéma de la table `aor_reports` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `AOR_Fields`, `AOR_Conditions`, `AOR_Charts`, `ACLController`, `BeanFactory`, `SuiteCRM\CleanCSV`
- **Consommé par :** `AOR_Scheduled_Reports` (envoi planifié), `AORReportsDashlet`, interface admin
- **Flux typique :** Utilisateur définit rapport (champs + conditions + graphiques) → `AOR_Report::build_report_query()` → requête SQL → `build_report_html()` → affichage

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre la construction des requêtes SQL | [`AOR_Report.php`](AOR_Report.doc.md) |
| Voir les fonctions SQL autorisées | [`aor_utils.php`](aor_utils.doc.md) |
| Comprendre le contrôleur (export CSV/PDF) | [`controller.php`](controller.doc.md) |

---

## ⚠️ Zones INCONNU
- `module_path` sérialisé en `base64(serialize(...))` — désérialisation avec `['allowed_classes' => false]`
- `queryWhereRepair` boucle jusqu'à 100 itérations pour nettoyer les parenthèses vides
