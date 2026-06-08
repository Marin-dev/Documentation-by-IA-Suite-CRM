# 📁 css

**Chemin :** `themes/SuiteP/css/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient les ressources CSS du thème SuiteP. Le fichier documenté (`colourSelector.php`) est un générateur de CSS dynamique censé personnaliser les couleurs du thème selon la configuration admin. Il est actuellement non fonctionnel (bloc de personnalisation commenté).

## ⚙️ Responsabilité technique
`colourSelector.php` est un fichier PHP servi directement via HTTP avec l'en-tête `Content-Type: text/css`. Il lit `config.php` et `config_override.php` pour accéder aux paramètres de thème. En l'état, il ne produit aucun CSS utile.

---

## 📂 Contenu

### Sous-dossiers
_(aucun)_

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `colourSelector.php` | Générateur CSS dynamique de couleurs SuiteP (actuellement non fonctionnel) | [→ fiche](colourSelector.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `config.php`, `config_override.php` (racine)
- **Appelé par :** navigateur via `<link href=".../colourSelector.php">` dans les templates du thème SuiteP

---

## ⚠️ Zones INCONNU
- `colourSelector.php` : TODO non résolu — personnalisation des couleurs (`navbar`) non implémentée (bloc commenté)
- Autres fichiers CSS statiques dans ce dossier : non documentés
