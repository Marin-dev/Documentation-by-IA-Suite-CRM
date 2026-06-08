# 📁 Employees

**Chemin :** `modules/Employees/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Employees gère la liste des employés dans SuiteCRM. Il représente les utilisateurs actifs en tant qu'employés visibles dans l'annuaire interne de l'entreprise.

## ⚙️ Responsabilité technique
Bean `Employee` (hérite de `User`). Module de vue sur les utilisateurs actifs avec module Studio dédié.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vues liste, détail, édition | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Employee.php` | Bean employé (hérite de User) | [→ fiche](Employee.doc.md) |
| `EmployeeStatus.php` | Gestion du statut employé | [→ fiche](EmployeeStatus.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Save.php` | Action de sauvegarde | [→ fiche](Save.doc.md) |
| `EmployeesStudioModule.php` | Module Studio pour les employés | [→ fiche](EmployeesStudioModule.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** Module `Users` (hérite de User)
- **Consommé par :** Annuaire interne, sélection d'utilisateurs

---

## ⚠️ Zones INCONNU
Aucun INCONNU notable.
