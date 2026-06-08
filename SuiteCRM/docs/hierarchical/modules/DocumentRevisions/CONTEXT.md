# 📁 DocumentRevisions

**Chemin :** `modules/DocumentRevisions/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module DocumentRevisions gère les révisions (versions) des documents dans SuiteCRM. Chaque révision représente une version d'un document avec son fichier physique uploadé, permettant le suivi de l'historique des versions d'un document.

## ⚙️ Responsabilité technique
Bean `DocumentRevision` (hérite de `SugarBean`). Table `document_revisions`. Gère l'upload physique des fichiers. Consommé par le module AOD_Index pour l'indexation des documents.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |
| `subpanels/` | Sous-panneaux directs | [→ CONTEXT](subpanels/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `DocumentRevision.php` | Bean révision de document | [→ fiche](DocumentRevision.php.doc.md) |
| `Forms.php` | Helpers de formulaire | [→ fiche](Forms.php.doc.md) |
| `vardefs.php` | Schéma de la table | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consommé par :** Module `Documents` (révisions liées), `AOD_Index` (indexation du contenu)
- **Flux typique :** Upload fichier → `DocumentRevision` créé → `Document` mis à jour → fichier indexé par AOD

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
