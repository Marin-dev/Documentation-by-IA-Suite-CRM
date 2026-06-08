# 📁 AOW_Processed

**Chemin :** `modules/AOW_Processed/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOW_Processed gère la traçabilité des exécutions de workflows AOW. Chaque enregistrement représente une exécution d'un workflow sur un bean CRM, avec son statut (Running, Complete, Failed). Permet d'éviter les double-exécutions quand `multiple_runs = false`.

## ⚙️ Responsabilité technique
Bean `AOW_Processed` (hérite de `Basic`). Classe sans logique métier. Créé/mis à jour par `AOW_WorkFlow::run_actions()`. Utilisé par `build_flow_query_where()` pour filtrer les enregistrements déjà traités.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue liste des exécutions | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet des exécutions | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOW_Processed.php` | Bean traçabilité d'exécution de workflow | [→ fiche](AOW_Processed.doc.md) |
| `vardefs.php` | Schéma de la table `aow_processed` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Créé/mis à jour par :** `AOW_WorkFlow::run_actions()`
- **Lu par :** `AOW_WorkFlow::build_flow_query_where()` (filtre records déjà traités), `check_valid_bean()`
- **Flux typique :** Workflow exécuté → création `AOW_Processed` (Running) → actions exécutées → statut mis à jour (Complete/Failed)

---

## ⚠️ Zones INCONNU
- `multiple_runs = true` : multiplication des enregistrements sans nettoyage automatique
