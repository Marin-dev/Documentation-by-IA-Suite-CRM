# 📁 AOK_KnowledgeBase

**Chemin :** `modules/AOK_KnowledgeBase/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module AOK_KnowledgeBase gère la base de connaissances de SuiteCRM. Il permet de créer, publier et consulter des articles de connaissance avec gestion des statuts (Draft, Published, Expired), des révisions, d'un auteur et d'un approbateur. Les articles sont organisés par catégories (`AOK_Knowledge_Base_Categories`).

## ⚙️ Responsabilité technique
Bean `AOK_KnowledgeBase` héritant de `AOK_KnowledgeBase_sugar` (Module Builder). Table `aok_knowledgebase`. Vue détail personnalisée pour décoder les entités HTML du champ `description`. Dashlet générique pour le tableau de bord.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues personnalisées (détail avec décodage HTML) | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet liste des articles KB | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `AOK_KnowledgeBase.php` | Bean article de base de connaissances | [→ fiche](AOK_KnowledgeBase.doc.md) |
| `vardefs.php` | Schéma de la table `aok_knowledgebase` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation du module | [→ fiche](Menu.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| `AOK_KnowledgeBase_sugar.php` | Classe générée automatiquement |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Basic`/SugarBean, `AOK_Knowledge_Base_Categories` (relation catégorie)
- **Consommé par :** Module Cases (INCONNU exact), interface d'administration
- **Flux typique :** Admin crée un article → workflow d'approbation → statut Published → visible dans les vues et dashlets

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle d'un article KB | [`AOK_KnowledgeBase.php`](AOK_KnowledgeBase.doc.md) |
| Voir le schéma de données | [`vardefs.php`](vardefs.doc.md) |
| Modifier la vue détail (rendu HTML) | [`views/view.detail.php`](views/view.detail.doc.md) |

---

## ⚠️ Zones INCONNU
- Lien exact avec le module Cases non documenté
- Logique de workflow d'approbation non identifiée dans le code source lu
