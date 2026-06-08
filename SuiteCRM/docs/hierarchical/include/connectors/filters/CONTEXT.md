# 📁 filters

**Chemin :** `include/connectors/filters/`
**Profondeur :** 4
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Ce dossier contient le système de filtres pour les connecteurs SuiteCRM. Un filtre transforme ou valide les données provenant d'une source externe avant qu'elles ne soient mappées vers un bean SuiteCRM.

## ⚙️ Responsabilité technique
`FilterFactory` est une classe statique avec cache. Elle cherche un filtre spécifique au connecteur, puis se replie sur le filtre par défaut. La classe de base `filter` est dans `default/filter.php` (non documenté dans ce périmètre).

---

## 📂 Contenu

### Sous-dossiers
Aucun documenté (dossier `default/` présent mais non documenté dans ce périmètre).

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `FilterFactory.php` | Fabrique de filtres — filtre spécifique ou filtre par défaut | [→ fiche](FilterFactory.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `default/filter.php` | Classe de base — hors périmètre de cette vague |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `ConnectorFactory`, classe `filter` (default)
- **Expose :** `FilterFactory::getInstance()` — utilisé lors du mapping de données connecteur
- **Flux typique :** Lors de l'application d'un connecteur, `FilterFactory::getInstance()` retourne le filtre approprié qui transforme les données avant leur injection dans le bean.

---

## ⚠️ Zones INCONNU
- Consommateurs de `FilterFactory` non identifiés précisément.
- Classe de base `default/filter.php` non documentée.
