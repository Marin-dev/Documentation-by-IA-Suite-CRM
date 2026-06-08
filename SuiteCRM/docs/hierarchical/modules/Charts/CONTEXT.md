# 📁 Charts

**Chemin :** `modules/Charts/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Charts fournit les graphiques commerciaux prédéfinis du tableau de bord SuiteCRM : pipeline par étape de vente, opportunités par source, résultats par mois, ROI des campagnes. Ces graphiques sont affichés comme dashlets.

## ⚙️ Responsabilité technique
Classe `PredefinedChart` comme base. Implémentations des graphiques dans `code/`. Dashlets correspondants dans `Dashlets/`. Utilise les données des modules Opportunities et Campaigns.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlets de graphiques commerciaux | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `code/` | Implémentations des graphiques prédéfinis | [→ CONTEXT](code/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `PredefinedChart.php` | Classe de base des graphiques prédéfinis | [→ fiche](PredefinedChart.doc.md) |
| `DynamicAction.php` | Rendu dynamique des graphiques | [→ fiche](DynamicAction.doc.md) |
| `chartdefs.php` | Définitions des graphiques disponibles | [→ fiche](chartdefs.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module Opportunities, Campaigns (données source), librairies de graphiques
- **Consommé par :** Tableau de bord SuiteCRM (dashlets de graphiques)

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
