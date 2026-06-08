# 📁 Documents

**Chemin :** `modules/Documents/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Documents gère la bibliothèque de documents de SuiteCRM. Les documents représentent des fichiers attachés (contrats, présentations, etc.) avec gestion des révisions. Chaque document est lié à un `DocumentRevision` pour suivre l'historique des versions.

## ⚙️ Responsabilité technique
Bean `Document` (hérite de `SugarBean`). Table `documents`. Gestion des révisions via `DocumentRevisions`. Support des documents externes. Interface SOAP via `DocumentSoap`. Dashlet et vue arborescente.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues détail, édition, document externe | [→ CONTEXT](views/CONTEXT.md) |
| `Dashlets/` | Dashlet "Mes documents" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Document.php` | Bean principal des documents | [→ fiche](Document.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `Delete.php` | Suppression d'un document | [→ fiche](Delete.php.doc.md) |
| `GetLatestRevision.php` | Récupération de la dernière révision | [→ fiche](GetLatestRevision.php.doc.md) |
| `DocumentSoap.php` | Interface SOAP | [→ fiche](DocumentSoap.php.doc.md) |
| `TreeData.php` | Données pour la vue arborescente | [→ fiche](TreeData.php.doc.md) |
| `vardefs.php` | Schéma de la table `documents` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `DocumentRevisions` (révisions), `SugarBean`, `UploadFile`
- **Consommé par :** Modules Accounts, Contacts, Opportunities (documents liés), AOD_Index (indexation des révisions)
- **Flux typique :** Upload document → création `Document` + `DocumentRevision` → visible dans les sous-panneaux des enregistrements liés

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
