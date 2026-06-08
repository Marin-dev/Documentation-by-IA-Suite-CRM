# 📁 AOW_Conditions

**Chemin :** `modules/AOW_Conditions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOW_Conditions gère les conditions de déclenchement des workflows AOW. Chaque condition définit une règle à vérifier sur un enregistrement CRM (ex : "Statut = Fermé", "Champ modifié"). L'ensemble des conditions doit être satisfait pour déclencher le workflow.

## ⚙️ Responsabilité technique
Bean `AOW_Condition` (hérite de `Basic`). `save_lines()` parse le POST et sérialise les valeurs Date/Multi/module_path en base64. Supporte les conditions sur modules liés via `module_path`. Le type `Any_Change` est uniquement évaluable en hook (pas en scheduler).

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOW_Condition.php` | Bean condition de workflow | [→ fiche](AOW_Condition.doc.md) |
| `conditionLines.php` | Helper d'affichage des conditions dans EditView | [→ fiche](conditionLines.doc.md) |
| `vardefs.php` | Schéma de la table `aow_conditions` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOW_WorkFlow::save()` (via `save_lines`), `build_flow_query_where()`, `check_valid_bean()`
- **Flux typique :** Save workflow → `AOW_Condition::save_lines()` → conditions persistées → execution → `build_flow_query_where()` ou `check_valid_bean()` évalue les conditions

---

## ⚠️ Zones INCONNU
- `Any_Change` : non évaluable par le scheduler, uniquement disponible en hook after_save
