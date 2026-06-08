# 📁 AOK_Knowledge_Base_Categories

**Chemin :** `modules/AOK_Knowledge_Base_Categories/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOK_Knowledge_Base_Categories gère les catégories de la base de connaissances SuiteCRM. Il permet d'organiser les articles `AOK_KnowledgeBase` en catégories hiérarchiques pour faciliter la navigation et la recherche.

## ⚙️ Responsabilité technique
Bean `AOK_Knowledge_Base_Categories` (hérite de `AOK_Knowledge_Base_Categories_sugar`, Module Builder). Table `aok_knowledge_base_categories`. Classe de personnalisation vide. Dashlet générique pour le tableau de bord.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet liste des catégories KB | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOK_Knowledge_Base_Categories.php` | Bean catégorie KB (classe de personnalisation vide) | [→ fiche](AOK_Knowledge_Base_Categories.doc.md) |
| `vardefs.php` | Schéma de la table catégories KB | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** `AOK_KnowledgeBase` (relation catégorie)
- **Flux typique :** Article KB → associé à une ou plusieurs catégories → navigation dans la KB par arborescence de catégories

---

## ⚠️ Zones INCONNU
- Type exact de la relation avec `AOK_KnowledgeBase` (many-to-many ou one-to-many) non confirmé
