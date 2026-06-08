# 📁 Groups

**Chemin :** `modules/Groups/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Groups gère les groupes d'utilisateurs (distincts des SecurityGroups). Représente les équipes ou groupes fonctionnels d'utilisateurs.

## ⚙️ Responsabilité technique
Bean `Group` (hérite de `SugarBean`). Module léger.

---

## 📂 Contenu

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Group.php` | Bean groupe d'utilisateurs | [→ fiche](Group.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Gestion des équipes, routing des cas (AOP)

---

## ⚠️ Zones INCONNU
- Distinction exacte avec SecurityGroups INCONNU sans lecture complète
