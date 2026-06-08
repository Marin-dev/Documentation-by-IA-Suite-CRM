# 📁 AOR_Conditions

**Chemin :** `modules/AOR_Conditions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOR_Conditions gère les conditions de filtrage des rapports AOR. Chaque condition représente une ligne de filtre (ex : "Montant > 1000", "Statut = Fermé") avec support des opérateurs logiques, parenthèses et conditions paramétrables par l'utilisateur.

## ⚙️ Responsabilité technique
Bean `AOR_Condition` (hérite de `Basic`). `save_lines()` parse le POST pour créer/modifier/supprimer les conditions. Les valeurs de type tableau (Date, Multi, Period) sont sérialisées en `base64(serialize(...))`. Gestion des parenthèses avec validation de cohérence ouverture/fermeture.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises du module | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOR_Condition.php` | Bean condition de filtrage d'un rapport | [→ fiche](AOR_Condition.doc.md) |
| `conditionLines.php` | Helper d'affichage des lignes de conditions dans EditView | [→ fiche](conditionLines.doc.md) |
| `vardefs.php` | Schéma de la table `aor_conditions` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic`, `BeanFactory`, données POST de l'EditView AOR_Reports
- **Consommé par :** `AOR_Report::save()` (via `save_lines`), `AOR_Report::build_report_query_where()`
- **Flux typique :** Sauvegarde rapport → `AOR_Condition::save_lines($post, $report)` → création des enregistrements de conditions → `build_report_query_where()` génère la clause WHERE SQL

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle d'une condition | [`AOR_Condition.php`](AOR_Condition.doc.md) |
| Voir comment les conditions s'affichent en édition | [`conditionLines.php`](conditionLines.doc.md) |

---

## ⚠️ Zones INCONNU
- `conditionLines.php` : contenu exact non lu
- Gestion de la parenthèse : lève une Exception si incohérence — comportement utilisateur non documenté
