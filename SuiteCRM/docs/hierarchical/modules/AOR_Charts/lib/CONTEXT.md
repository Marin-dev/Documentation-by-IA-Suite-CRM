# 📁 lib

**Chemin :** `modules/AOR_Charts/lib/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Contient les librairies tierces utilisées par le module AOR_Charts pour le rendu de graphiques. La librairie pChart génère des images PNG à partir des données de rapports.

## ⚙️ Responsabilité technique
Librairie PHP pChart embarquée. Fournit les classes `pData`, `pImage`, `pPie`, `pRadar` pour le rendu de graphiques en images PNG.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `pChart/` | Moteur pChart de génération d'images graphiques | [→ fiche](pChart/pChart.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOR_Chart::buildChartImage()`
- **Expose :** Classes `pData`, `pImage`, `pPie`, `pRadar`

---

## ⚠️ Zones INCONNU
- Contenu détaillé de pChart non entièrement documenté
