# 📁 Bugs

**Chemin :** `modules/Bugs/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Bugs gère les signalements de défauts dans SuiteCRM. Il représente un bug/défaut remonté par un client ou une équipe interne, avec suivi de statut, priorité, type, version concernée et version de correction. Les bugs sont liés aux comptes, contacts et cas.

## ⚙️ Responsabilité technique
Bean `Bug` (hérite de `SugarBean`). Table `bugs`. Numéro de bug auto-incrémenté. Cache statique pour les releases. Supporte l'import CSV, les SecurityGroups et les ACL.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail et édition | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes bugs" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Bug.php` | Bean principal du module Bugs | [→ fiche](Bug.doc.md) |
| `BugsQuickCreate.php` | Formulaire de création rapide de bug | [→ fiche](BugsQuickCreate.doc.md) |
| `vardefs.php` | Schéma de la table `bugs` | [→ fiche](vardefs.doc.md) |
| `field_arrays.php` | Tableaux de champs pour l'export/import | [→ fiche](field_arrays.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`, `Releases` (releases actives pour dropdowns)
- **Consommé par :** Modules Accounts, Contacts, Cases (relations), `MyBugsDashlet`
- **Flux typique :** Signalement bug → sauvegarde → liens avec compte/contacts créés → suivi de statut

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
