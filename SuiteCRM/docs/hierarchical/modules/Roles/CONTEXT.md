# 📁 Roles

**Chemin :** `modules/Roles/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Roles gère les rôles utilisateur dans SuiteCRM (distinct des ACLRoles). Ce module représente les rôles au sens fonctionnel (titre, fonction) assignés aux utilisateurs pour les relations (ex : rôle d'un contact dans une opportunité). Complément aux ACLRoles.

## ⚙️ Responsabilité technique
Bean `Role` (hérite de `SugarBean`). CRUD standard avec gestion des relations utilisateurs.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue liste des rôles | [→ CONTEXT](views/CONTEXT.md) |
| `language/` | Traductions anglaises | [→ CONTEXT](language/CONTEXT.md) |
| `metadata/` | Configuration des vues | [→ CONTEXT](metadata/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `Role.php` | Bean principal des rôles | [→ fiche](Role.doc.md) |
| `Save.php` | Sauvegarde d'un rôle | [→ fiche](Save.doc.md) |
| `Delete.php` | Suppression d'un rôle | [→ fiche](Delete.doc.md) |
| `SaveUserRelationship.php` | Sauvegarde relation utilisateur-rôle | [→ fiche](SaveUserRelationship.doc.md) |
| `DeleteUserRelationship.php` | Suppression relation utilisateur-rôle | [→ fiche](DeleteUserRelationship.doc.md) |
| `SubPanelViewUsers.php` | Vue sous-panneau utilisateurs | [→ fiche](SubPanelViewUsers.doc.md) |
| `vardefs.php` | Schéma de la table `roles` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `BeanFactory`
- **Consommé par :** Relations Contacts-Opportunités, ACL system (ACLRoles distinct)
- **Flux typique :** Rôle créé → assigné aux utilisateurs → utilisé dans les relations

---

## ⚠️ Zones INCONNU
- Distinction exacte avec `ACLRoles` non documentée dans ces fiches
