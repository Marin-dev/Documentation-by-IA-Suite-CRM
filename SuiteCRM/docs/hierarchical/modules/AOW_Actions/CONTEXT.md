# 📁 AOW_Actions

**Chemin :** `modules/AOW_Actions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOW_Actions gère les actions exécutées par les workflows AOW. Chaque action représente une étape du workflow (envoyer un email, modifier un champ, créer un enregistrement, calculer une formule). Les actions sont configurables via l'éditeur de workflow et exécutées dynamiquement.

## ⚙️ Responsabilité technique
Bean `AOW_Action` (hérite de `Basic`). Paramètres sérialisés en `base64(serialize(...))`. Classes d'actions concrètes dans `actions/` héritant de `actionBase`. Chargement dynamique par `AOW_WorkFlow::run_actions()`. Supporte les overrides via `custom/modules/AOW_Actions/actions/`.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `actions/` | Classes d'actions concrètes (SendEmail, ModifyRecord, etc.) | [→ CONTEXT](actions/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOW_Action.php` | Bean action de workflow avec sérialisation des paramètres | [→ fiche](AOW_Action.doc.md) |
| `FormulaCalculator.php` | Calculateur de formules pour les actions de calcul | [→ fiche](FormulaCalculator.doc.md) |
| `actionLines.php` | Helper d'affichage des lignes d'actions dans EditView | [→ fiche](actionLines.doc.md) |
| `actions.php` | Gestion du registre des types d'actions disponibles | [→ fiche](actions.doc.md) |
| `vardefs.php` | Schéma de la table `aow_actions` | [→ fiche](vardefs.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic`, `BeanFactory`, `AOS_PDF_Templates/templateParser.php` (pour emails)
- **Consommé par :** `AOW_WorkFlow::run_actions()` (exécution), `AOW_WorkFlow::save()` (persistance via `save_lines`)
- **Flux typique :** Éditeur workflow → `save_lines()` → sérialisation paramètres → `run_actions()` → chargement dynamique de la classe d'action → `run_action($bean, $params)`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Voir toutes les actions disponibles | [`actions/`](actions/CONTEXT.md) |
| Comprendre le bean action | [`AOW_Action.php`](AOW_Action.doc.md) |
| Voir les calculs de formules | [`FormulaCalculator.php`](FormulaCalculator.doc.md) |

---

## ⚠️ Zones INCONNU
- Formatage complet des paramètres (`fixUpFormatting`) non entièrement documenté
