# 📁 ACLRoles

**Chemin :** `modules/ACLRoles/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module ACLRoles gère les rôles du système de contrôle d'accès SuiteCRM. Un rôle définit un ensemble de niveaux d'accès par module et par action. Les rôles sont assignés aux utilisateurs ou aux groupes de sécurité pour contrôler finement leurs permissions sur l'ensemble de l'application.

## ⚙️ Responsabilité technique
Implémente le bean `ACLRole` (hérite de `SugarBean`, table `acl_roles`). Expose des méthodes CRUD pour les rôles et leurs actions associées. La vue classique affiche une matrice de permissions interactive. Le module supporte les appels AJAX pour la mise à jour en temps réel des niveaux d'accès.

---

## 📂 Contenu

### Sous-dossiers
| Dossier | Rôle en une ligne | Détails |
|---|---|---|
| `views/` | Vue matrice des permissions (classique) | [→ CONTEXT](views/CONTEXT.md) |

### Fichiers documentés
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `ACLRole.php` | Bean modèle d'un rôle ACL avec méthodes de gestion | [→ fiche](ACLRole.php.doc.md) |
| `Save.php` | Sauvegarde/création de rôle et mise à jour AJAX des permissions | [→ fiche](Save.php.doc.md) |
| `Delete.php` | Suppression d'un rôle (soft delete + nettoyage des actions) | [→ fiche](Delete.php.doc.md) |

### Fichiers non documentés (volontairement)
| Fichier | Raison |
|---|---|
| — | — |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `SugarBean`, `DBManagerFactory`, `BeanFactory`, tables `acl_roles`, `acl_roles_users`, `acl_roles_actions`
- **Expose :** `ACLRole::getUserRoles()`, `ACLRole::getRoleActions()`, `ACLRole::setAction()` — utilisés par `ACLAction::getUserActions()` et les vues
- **Flux typique :** Admin → vue classique matrice → AJAX Save.php `act_guid_*` → `ACLRole::setAction()` → table `acl_roles_actions`

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre le modèle de données des rôles | [`ACLRole.php`](ACLRole.php.doc.md) |
| Modifier la logique de sauvegarde d'un rôle | [`Save.php`](Save.php.doc.md) |
| Comprendre la suppression d'un rôle | [`Delete.php`](Delete.php.doc.md) |
| Voir l'interface de la matrice de permissions | [`views/view.classic.php`](views/view.classic.php.doc.md) |

---

## ⚠️ Zones INCONNU
- `view.classic.php` : rendu HTML de la matrice non entièrement documenté
- Absence de fichiers `language/`, `metadata/`, `vardefs.php` dans la documentation (peut exister dans le code source)
