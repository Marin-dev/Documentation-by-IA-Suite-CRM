# 📁 AOD_IndexEvent

**Chemin :** `modules/AOD_IndexEvent/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOD_IndexEvent représente les événements d'indexation du moteur de recherche full-text AOD (Advanced OpenDiscovery). **Déprécié depuis v7.12.0** avec l'ensemble du module AOD.

## ⚙️ Responsabilité technique
Bean vide `AOD_IndexEvent` héritant de `AOD_IndexEvent_sugar` (généré automatiquement). Aucune logique métier ajoutée.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOD_IndexEvent.php` | Bean événement d'indexation (déprécié) | [→ fiche](AOD_IndexEvent.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AOD_IndexEvent_sugar.php` | Classe générée automatiquement |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Moteur AOD_Index (exclu de l'indexation, blacklisté dans `AOD_Index::isModuleSearchable()`)
- **Flux typique :** N/A — déprécié

---

## ⚠️ Zones INCONNU
- Module entièrement déprécié depuis v7.12.0
- Consommateurs exacts non identifiés depuis la dépréciation
