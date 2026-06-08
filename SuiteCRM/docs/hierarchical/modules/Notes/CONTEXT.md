# 📁 Notes

**Chemin :** `modules/Notes/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Notes gère les notes et pièces jointes dans SuiteCRM. Une note représente une observation, un commentaire ou un document joint lié à un enregistrement CRM (compte, contact, appel, réunion, tâche). Les notes constituent une partie de l'historique des activités.

## ⚙️ Responsabilité technique
Bean `Note` (hérite de `SugarBean`). Table `notes`. Gestion des pièces jointes upload. Intégration SOAP via `NoteSoap`. Sous-panneau vue spécifique.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `Dashlets/` | Dashlet "Mes notes" | [→ CONTEXT](Dashlets/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Note.php` | Bean principal des notes | [→ fiche](Note.php.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.php.doc.md) |
| `SubPanelView.php` | Vue sous-panneau des notes | [→ fiche](SubPanelView.php.doc.md) |
| `NoteSoap.php` | Interface SOAP pour les notes | [→ fiche](NoteSoap.php.doc.md) |
| `NotesQuickCreate.php` | Création rapide de note | [→ fiche](NotesQuickCreate.php.doc.md) |
| `vardefs.php` | Schéma de la table `notes` | [→ fiche](vardefs.php.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `UploadFile`
- **Consommé par :** Modules Accounts, Contacts, Calls, Meetings, Tasks (notes liées), historique des activités
- **Flux typique :** Création note → liaison avec bean parent → pièce jointe uploadée → visible dans l'historique

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
